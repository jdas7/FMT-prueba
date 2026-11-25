# Reporte de experiencia de usuario (UX) – Farmatodo

**Sitio evaluado:** https://www.farmatodo.com/  
**Sitio Colombia consultado:** https://www.farmatodo.com.co/  
**Tipo de evaluación:** Heurística y exploratoria

## Resumen de hallazgos

| ID | Hallazgo                                                       | Módulo | Vista propuesta para validación | Prioridad |
|---|----------------------------------------------------------------|---|---------------------------------|---|
| [FMT-bug1](video%2FFMT-bug1.mp4) | La lista desplegable para cambiar de país actualiza la pagina  | Navegación y búsqueda | Web (desktop)                   | Media |
| [FMT-bug2](video%2FFMT-bug2.mp4) | Demora en la visualización y actualización del carrito         | Carrito de compras | Web (desktop)                   | Media |
| [FMT-bug3](video%2FFMT-bug3.mp4) | PopUp descarga la APP, aparece cada vez que se carga la pagina | Carrito de compras | Web (Mobile)                    | Media |

---

## FMT-bug1 – La lista desplegable para cambiar de país actualiza la pagina

**Módulo:** Navegación y búsqueda  
**Vista:** Web (desktop) 
**Tipo:** Oportunidad de mejora de usabilidad  
**Prioridad:** Media

### Descripción

La lista desplegable de paises actualiza la página lo cual no deberia hacer, solo debería actualizarce si se selecciona el país deseado.

### Pasos para reproducir

1. Ingresar a https://www.farmatodo.com.co/.
2. Ubicar la opción **paises**.
3. Desplegar el menú de paises.
4. Se actualiza la pagina al desplegar la lista de paises.

### Resultado esperado

Se deberia desplegar la lista de los paises sin que la página se actualice.

### Recomendación

- Mantener una navegación consistente entre todas las listas del menú principal y los submenús.

### Impacto en el usuario

Error en el proposito de la lista, es ver los paises no la actualización de la pagina.

---

## FMT-bug2 – Demora en la visualización y actualización del carrito

**Módulo:** Carrito de compras  
**Vista:** Web (desktop)
**Tipo:** Oportunidad de mejora de experiencia  
**Prioridad:** Media

### Descripción

El carrito es una etapa crítica del proceso de compra. El usuario espera que los productos agregados, las cantidades y los valores se actualicen de forma clara y oportuna.

Se identificó demoras en la visualización y actualización del carrito de compras.

### Pasos para reproducir

1. Ingresar a https://www.farmatodo.com.co/.
2. Buscar un producto disponible.
3. Agregar el producto al carrito.
4. Ingresar al carrito de compras.
5. Observar el tiempo que tarda en mostrarse el contenido.
6. Modificar la cantidad de un producto.
7. Verificar si los valores y el resumen de compra se actualizan de forma clara y oportuna.

### Resultado esperado

El carrito debe mostrar oportunamente los productos agregados y permitir que el usuario identifique fácilmente.

Cuando se modifica una cantidad o se elimina un producto, el resumen debe actualizarse y proporcionar rapidamente, si hay procesos se deben ejecutar de manera asincrona.

### Recomendación

- Optimizar la presentación y actualización del carrito, disminuir los tiempos de carga.
- Proporcionar retroalimentación visual al agregar, eliminar o modificar productos.

### Impacto en el usuario

La demora o falta de retroalimentación puede generar incertidumbre sobre si el producto fue agregado correctamente, provocar operaciones repetidas y afectar la confianza durante el proceso de compra.

---

## FMT-bug3 – PopUp descarga la APP, aparece cada vez que se carga la pagina

**Módulo:** PopUp descarga la APP
**Vista:** Web (mobile)
**Tipo:** Oportunidad de mejora de experiencia  
**Prioridad:** Media

### Descripción

Cuando se ingresa a la web desde el celular, se muestra en el home un popUp que indica que puedes descargar la APP, si se actualiza la página por parte del usuario se vuelve a retroalimentar al usuario con el PopUp indicando que puede descargar la APP.
### Pasos para reproducir

1. Ingresar a https://www.farmatodo.com.co/ desde web mobile en un celular sin la app de farmatodo.
2. Visualiza el popUp y cierralo.
3. actualiza la pagina haciendo sroll.
4. Se visualiza nuevamente el popUp.

### Resultado esperado

Si el usuario ya vio la información para descargar la APP y no la uso y cierra el popUp pero vuelve a aparecer genera una mala experiencia.
### Recomendación

- Usar una cache en el navegador, si el usuario ya vio el popUp y no lo uso aun que cargue de nuevo el home, no deberia mostrarle em popUp durante esa Sesión.

### Impacto en el usuario

Se debe tener en cuenta que el usuario opto por no descargar la APP se debe administrar bien la retroalimentación del usuario

