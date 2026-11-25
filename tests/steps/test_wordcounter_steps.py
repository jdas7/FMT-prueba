import re

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from helpers.texto import (
    contar_caracteres,
    contar_palabras,
    generar_texto_aleatorio,
    generar_texto_sin_sentido,
)

scenarios("wordcounter.feature")


@given("que el usuario abre la página de WordCounter")
def abrir_wordcounter(wordcounter):
    wordcounter.abrir()


@when(parsers.parse('el usuario ingresa el texto "{texto}"'))
def ingresar_texto(wordcounter, texto):
    wordcounter.ingresar_texto(texto)


@when(parsers.re(r"el usuario ingresa el texto\n(?P<texto>.*)", flags=re.DOTALL))
def ingresar_texto_multilinea(wordcounter, texto):
    wordcounter.ingresar_texto(texto)


@when(parsers.parse('reemplaza el texto por "{texto}"'))
def reemplazar_texto(wordcounter, texto):
    wordcounter.ingresar_texto(texto)


@when("el usuario ingresa un texto vacío")
def ingresar_texto_vacio(wordcounter):
    wordcounter.ingresar_texto("")


@pytest.fixture
def texto_aleatorio():
    return generar_texto_aleatorio()


@pytest.fixture
def texto_sin_sentido():
    return generar_texto_sin_sentido()


@when("el usuario ingresa un texto aleatorio")
def ingresar_texto_aleatorio(wordcounter, texto_aleatorio):
    wordcounter.ingresar_texto(texto_aleatorio)


@when("el usuario ingresa un texto sin sentido")
def ingresar_texto_sin_sentido(wordcounter, texto_sin_sentido):
    wordcounter.ingresar_texto(texto_sin_sentido)


@then(parsers.parse("el contador de palabras debe mostrar {esperado:d}"))
def validar_palabras(wordcounter, esperado):
    actual = wordcounter.obtener_numero_palabras()
    assert actual == esperado, f"Conteo de palabras incorrecto. Esperado: {esperado}; obtenido: {actual}"


@then(parsers.parse("el contador de caracteres debe mostrar {esperado:d}"))
def validar_caracteres(wordcounter, esperado):
    actual = wordcounter.obtener_numero_caracteres()
    assert actual == esperado, f"Conteo de caracteres incorrecto. Esperado: {esperado}; obtenido: {actual}"


@then(parsers.re(r"las tres palabras más frecuentes deben ser\n(?P<tabla>.+)", flags=re.DOTALL))
def validar_keyword_density(wordcounter, tabla):
    filas = []
    for linea in tabla.splitlines():
        if not linea.strip():
            continue
        filas.append([celda.strip() for celda in linea.strip().strip("|").split("|")])
    esperado = [(fila[0], int(fila[1])) for fila in filas[1:]]
    actual = wordcounter.obtener_keyword_density(limite=3)
    assert actual == esperado, f"Keyword Density incorrecto. Esperado: {esperado}; obtenido: {actual}"


@then("el conteo de palabras y caracteres de la página debe coincidir con el conteo local")
def validar_conteo_local(wordcounter, texto_aleatorio):
    palabras_locales = contar_palabras(texto_aleatorio)
    caracteres_locales = contar_caracteres(texto_aleatorio)
    palabras_pagina = wordcounter.obtener_numero_palabras()
    caracteres_pagina = wordcounter.obtener_numero_caracteres()
    assert (palabras_pagina, caracteres_pagina) == (palabras_locales, caracteres_locales), (
        "El conteo de la página no coincide con el conteo local. "
        f"Texto: {texto_aleatorio!r}. "
        f"Palabras local={palabras_locales}, página={palabras_pagina}. "
        f"Caracteres local={caracteres_locales}, página={caracteres_pagina}."
    )


@then("la página debe advertir que el texto podría contener errores de escritura")
def validar_aviso_errores_escritura(wordcounter):
    wordcounter.esperar_aviso_errores_escritura()
