from __future__ import annotations
import re
from playwright.sync_api import Page, Locator


class WordCounterPage:
    URL = "https://wordcounter.net/"
    AVISO_ERRORES_ESCRITURA = "Your text might contain writing issues"

    def __init__(self, page: Page) -> None:
        self.page = page

    def abrir(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.page.locator("body").wait_for(state="visible")

    def _campo_texto(self) -> Locator:
        selectores = ["textarea", '[contenteditable="true"]', "#textarea", "#text"]
        for selector in selectores:
            locator = self.page.locator(selector).first
            try:
                if locator.count() > 0 and locator.is_visible():
                    return locator
            except Exception:
                continue
        raise AssertionError(
            "No se encontró el campo de entrada. Inspecciona el DOM de WordCounter "
            "y actualiza WordCounterPage._campo_texto()."
        )

    def ingresar_texto(self, texto: str) -> None:
        self._campo_texto().fill(texto)
        self.page.wait_for_timeout(300)

    def _texto_visible(self) -> str:
        return self.page.locator("body").inner_text()

    @staticmethod
    def _extraer_numero(texto: str, patrones: list[str], concepto: str) -> int:
        for patron in patrones:
            match = re.search(patron, texto, flags=re.IGNORECASE | re.MULTILINE)
            if match:
                return int(match.group(1).replace(",", ""))
        raise AssertionError(
            f"No se pudo identificar el contador de {concepto}. "
            "Actualiza los localizadores/expresiones del Page Object según el DOM actual."
        )

    def obtener_numero_palabras(self) -> int:
        # El encabezado es "4 words 19 characters": el número va delante de la etiqueta.
        texto = self._texto_visible()
        return self._extraer_numero(texto, [
            r"\b([\d,]+)\s+words\b",
        ], "palabras")

    def obtener_numero_caracteres(self) -> int:
        texto = self._texto_visible()
        return self._extraer_numero(texto, [
            r"\b([\d,]+)\s+characters\b",
        ], "caracteres")

    def obtener_keyword_density(self, limite: int = 3) -> list[tuple[str, int]]:
        filas: list[tuple[str, int]] = []
        items = self.page.locator("#kwd-accordion-data .list-group-item")
        items.first.wait_for(state="attached")
        for item in items.all():
            palabra = (item.locator(".word").text_content() or "").strip()
            badge = (item.locator(".badge").text_content() or "").strip()
            match = re.match(r"(\d+)", badge)
            if palabra and match:
                filas.append((palabra, int(match.group(1))))
            if len(filas) >= limite:
                break
        if not filas:
            raise AssertionError(
                "No se encontraron filas en #kwd-accordion-data. "
                "Inspecciona Keyword Density y ajusta obtener_keyword_density()."
            )
        return filas

    def esperar_aviso_errores_escritura(self) -> None:
        aviso = self.page.locator("#gly-cta-1")
        aviso.wait_for(state="visible", timeout=10000)
        texto = aviso.inner_text()
        if self.AVISO_ERRORES_ESCRITURA not in texto:
            raise AssertionError(
                "No apareció el aviso de errores de escritura "
                f"({self.AVISO_ERRORES_ESCRITURA!r}). Texto visible: {texto!r}"
            )
