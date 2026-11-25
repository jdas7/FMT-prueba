from pathlib import Path

from frecuencia.contador import analizar, formatear

EJEMPLO = Path(__file__).resolve().parents[1] / "frecuencia" / "ejemplo.txt"

SALIDA_EJEMPLO = """\
14 words
99 characters
farmatodo: 6
cuida: 3
salud: 2
tu: 2
toda: 1\
"""


def test_ejemplo_del_enunciado():
    texto = EJEMPLO.read_text(encoding="utf-8")
    assert formatear(analizar(texto)) == SALIDA_EJEMPLO


def test_empate_se_ordena_alfabeticamente():
    resultado = analizar("beta alfa beta alfa gamma")
    assert resultado.frecuencias == (("alfa", 2), ("beta", 2), ("gamma", 1))


def test_saltos_de_linea_no_cuentan_como_caracteres():
    texto = "ab cd\r\nab"
    resultado = analizar(texto)
    assert resultado.palabras == 3
    assert resultado.caracteres == len("ab cdab")


def test_texto_vacio():
    resultado = analizar("")
    assert resultado.palabras == 0
    assert resultado.caracteres == 0
    assert resultado.frecuencias == ()
    assert formatear(resultado) == "0 words\n0 characters"
