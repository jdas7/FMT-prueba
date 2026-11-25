from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Resultado:
    palabras: int
    caracteres: int
    frecuencias: tuple[tuple[str, int], ...]


def analizar(texto: str) -> Resultado:
    """Cuenta palabras, caracteres y frecuencias de un bloque de texto."""
    caracteres = len(texto.replace("\n", "").replace("\r", ""))
    tokens = texto.split()
    conteo = Counter(tokens)
    frecuencias = tuple(sorted(conteo.items(), key=lambda item: (-item[1], item[0])))
    return Resultado(palabras=len(tokens), caracteres=caracteres, frecuencias=frecuencias)


def formatear(resultado: Resultado) -> str:
    """Arma la salida: totales y el histograma palabra: frecuencia."""
    lineas = [
        f"{resultado.palabras} words",
        f"{resultado.caracteres} characters",
    ]
    lineas.extend(f"{palabra}: {cantidad}" for palabra, cantidad in resultado.frecuencias)
    return "\n".join(lineas)


def main(argv: list[str] | None = None) -> int:
    argumentos = list(sys.argv[1:] if argv is None else argv)
    if len(argumentos) != 1:
        print("Uso: python -m frecuencia.contador <archivo>", file=sys.stderr)
        return 1
    texto = Path(argumentos[0]).read_text(encoding="utf-8")
    print(formatear(analizar(texto)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
