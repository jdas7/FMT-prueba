from __future__ import annotations
import os
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
from pytest_bdd import types
from pytest_bdd.parser import STEP_PREFIXES
from pages.wordcounter_page import WordCounterPage

_PREFIJOS_ES = [
    ("Característica: ", types.FEATURE),
    ("Funcionalidad: ", types.FEATURE),
    ("Esquema del escenario: ", types.SCENARIO_OUTLINE),
    ("Ejemplos:", types.EXAMPLES),
    ("Escenario: ", types.SCENARIO),
    ("Ejemplo: ", types.SCENARIO),
    ("Antecedentes:", types.BACKGROUND),
    ("Entonces ", types.THEN),
    ("Cuando ", types.WHEN),
    ("Dadas ", types.GIVEN),
    ("Dados ", types.GIVEN),
    ("Dada ", types.GIVEN),
    ("Dado ", types.GIVEN),
    ("Pero ", None),
    ("Y ", None),
]
for _prefijo in reversed(_PREFIJOS_ES):
    if _prefijo not in STEP_PREFIXES:
        STEP_PREFIXES.insert(0, _prefijo)

REPORTS = Path("reports")
SCREENSHOTS = REPORTS / "screenshots"


@pytest.fixture(scope="session", autouse=True)
def preparar_reportes():
    REPORTS.mkdir(exist_ok=True)
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)


def _headless() -> bool:
    return os.getenv("HEADLESS", "true").lower() not in {"false", "0", "no"}


@pytest.fixture(scope="session")
def navegador():
    """Un Chromium por worker de pytest-xdist."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=_headless())
        yield browser
        browser.close()


@pytest.fixture
def navegador_page(navegador):
    context = navegador.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def wordcounter(navegador_page):
    return WordCounterPage(navegador_page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("navegador_page")
        if page:
            nombre = "".join(c if c.isalnum() or c in "-_" else "_" for c in item.name)
            try:
                page.screenshot(path=str(SCREENSHOTS / f"{nombre}.png"), full_page=True)
            except Exception:
                pass
