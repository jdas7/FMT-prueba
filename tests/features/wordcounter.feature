# language: es
Característica: Análisis de texto en WordCounter
  Como usuario de WordCounter
  Quiero analizar un bloque de texto
  Para conocer la cantidad de palabras, caracteres y las palabras más frecuentes

  Antecedentes:
    Dado que el usuario abre la página de WordCounter

  @e2e @smoke
  Escenario: Contar correctamente las palabras de un texto
    Cuando el usuario ingresa el texto "Hola mundo desde QA"
    Entonces el contador de palabras debe mostrar 4

  @e2e @smoke
  Escenario: Contar caracteres incluyendo espacios
    Cuando el usuario ingresa el texto "Hola mundo"
    Entonces el contador de caracteres debe mostrar 10

  @e2e
  Escenario: Mostrar las tres palabras más repetidas
    Cuando el usuario ingresa el texto "manzana manzana manzana pera pera naranja"
    Entonces las tres palabras más frecuentes deben ser
      | palabra | frecuencia |
      | manzana | 3          |
      | pera    | 2          |
      | naranja | 1          |

  @e2e
  Escenario: Actualizar el conteo al reemplazar el texto
    Cuando el usuario ingresa el texto "uno dos"
    Y reemplaza el texto por "uno dos tres cuatro"
    Entonces el contador de palabras debe mostrar 4

  @e2e
  Escenario: Procesar un texto con varias líneas
    Cuando el usuario ingresa el texto
      """
      calidad automatizacion
      pruebas calidad
      """
    Entonces el contador de palabras debe mostrar 4

  @e2e
  Escenario: Procesar un texto vacío
    Cuando el usuario ingresa un texto vacío
    Entonces el contador de palabras debe mostrar 0

  @e2e
  Escenario: Contrastar un texto aleatorio con el conteo de la página
    Cuando el usuario ingresa un texto aleatorio
    Entonces el conteo de palabras y caracteres de la página debe coincidir con el conteo local

  @e2e
  Escenario: Advertir cuando el texto no tiene sentido
    Cuando el usuario ingresa un texto sin sentido
    Entonces la página debe advertir que el texto podría contener errores de escritura
