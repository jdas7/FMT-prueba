# Prueba técnica QA – Farmatodo

Suite E2E para [WordCounter](https://wordcounter.net/) con **Python, pytest, pytest-bdd, Playwright** y patrón **Page Object Model (POM)**. con escenarios escritos en Gherkin.

## Requisitos
- Python 3.10 o superior
- pip

## Instalación

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

## Ejecución
```bash
pytest
```

`pytest` reparte los escenarios entre workers de pytest-xdist (`-n auto`): un proceso por CPU, cada uno con su propio Chromium. Para un solo proceso:

```bash
pytest -n0
```

Para fijar el número de workers:

```bash
pytest -n 2
```

Solo pruebas E2E:
```bash
pytest -m e2e
```

Modo visible (Windows PowerShell):
```powershell
$env:HEADLESS="false"
pytest -s
```

Modo visible (macOS/Linux):
```bash
HEADLESS=false pytest -s
```

El reporte HTML se genera en `reports/reporte.html`. Incluye el resumen de pruebas ejecutadas y, para los fallos, el detalle de la excepción y traceback. Al fallar un escenario se intenta guardar una captura en `reports/screenshots/`.

## Estructura
```text
farmatodo-qa-automation/
├── pages/
│   └── wordcounter_page.py
├── tests/
│   ├── features/
│   │   └── wordcounter.feature
│   ├── steps/
│   │   └── test_wordcounter_steps.py
│   └── conftest.py
├── reports/
├── requirements.txt
├── pytest.ini
└── README.md
```

## Escenarios
1. Contar palabras.
2. Contar caracteres incluyendo espacios.
3. Obtener las tres palabras más repetidas y sus frecuencias.
4. Actualizar el conteo al reemplazar el texto.
5. Procesar texto con varias líneas.
6. Procesar texto vacío.
