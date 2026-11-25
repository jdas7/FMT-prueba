# Reporte de hallazgos – WordCounter

**Aplicación:** [https://wordcounter.net/](https://wordcounter.net/)  
**Módulo:** Keyword Density  
**Tipo de hallazgo:** Oportunidad de mejora – Usabilidad  
**Severidad:** Baja  
**Prioridad:** Baja  
**Ambiente:** Web – Desktop  

## UX-WC-001 – Falta de claridad en los controles de Keyword Density

### Descripción

En la sección **Keyword Density** se presentan tres controles identificados como `x1`, `x2` y `x3`. Sin embargo, no se observa una descripción textual que permita comprender claramente la función de cada uno.

Esta situación puede generar confusión en los usuarios, especialmente en aquellos que utilizan la herramienta por primera vez, cuando se da clic sobre x2 y x3 no muestra nada.

### Pasos para reproducir

1. Ingresar a https://wordcounter.net/.
2. Desplazarse hasta la sección **Keyword Density**.
3. Identificar los controles `x1`, `x2` y `x3`.

### Resultado actual

Los controles se muestran identificados únicamente como `x1`, `x2` y `x3`, sin una explicación textual visible de su propósito.

### Resultado esperado

Cada control debería contar con una etiqueta descriptiva, un tooltip o una ayuda contextual que permita al usuario comprender su funcionalidad y el efecto de seleccionarlo.

### Impacto

La falta de información puede afectar la experiencia de usuario y dificultar la interpretación de los resultados de densidad de palabras clave.

### Recomendación

Agregar etiquetas descriptivas o información contextual para explicar la función de cada control y facilitar su uso.
