from __future__ import annotations

import random
import string

_LETRAS = string.ascii_lowercase


def generar_texto_aleatorio(
    minimo_palabras: int = 1,
    maximo_palabras: int = 30,
    minimo_letras: int = 3,
    maximo_letras: int = 12,
) -> str:
    """Texto aleatorio de palabras"""
    cantidad = random.randint(minimo_palabras, maximo_palabras)
    palabras = [
        "".join(random.choices(_LETRAS, k=random.randint(minimo_letras, maximo_letras)))
        for _ in range(cantidad)
    ]
    return " ".join(palabras)


def generar_texto_sin_sentido(lineas: int = 12) -> str:
    """palabras random sin contexto"""
    return "\n".join(
        "".join(random.choices(_LETRAS, k=random.randint(6, 40)))
        for _ in range(lineas)
    )


def contar_palabras(texto: str) -> int:
    return len(texto.split())


def contar_caracteres(texto: str) -> int:
    return len(texto)
