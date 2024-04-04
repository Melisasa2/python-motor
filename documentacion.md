
## Búsqueda de Información - API Documentación

¡Bienvenido a la documentación de la API de búsqueda de información! Esta API te permite buscar información específica relacionada con tutelas, decretos y contenido dentro de nuestra base de datos.

### ¿Cómo funciona?

La API proporciona un endpoint (`/api/v1/search`) al que puedes enviar solicitudes para buscar información. Puedes buscar información por tipo de tutela, por número de decreto o por contenido específico.

### Ejemplos de Uso

#### Búsqueda por Tipo de Tutela

Puedes buscar información relacionada con un tipo específico de tutela. Por ejemplo, si estás interesado en obtener información sobre la tutela de salud, puedes enviar una solicitud como esta:

```
GET /api/v1/search?tipo_tutela=salud
```

La API devolverá información relevante sobre la tutela de salud si está disponible.

#### Búsqueda por Número de Decreto

También puedes buscar información relacionada con un decreto específico proporcionando su número. Por ejemplo, si deseas información sobre el Decreto 1, puedes enviar una solicitud como esta:

```
GET /api/v1/search?decreto=8064
```

La API te proporcionará detalles relacionados con el Decreto 1 si existe en nuestra base de datos.

#### Búsqueda por Contenido

Si estás buscando información específica dentro del contenido de nuestras tutelas, también puedes realizar una búsqueda por contenido. Por ejemplo, si deseas encontrar todas las tutelas que contienen la palabra "salud", puedes enviar una solicitud como esta:

```
GET /api/v1/search?contenido=salud
```

La API devolverá todas las tutelas que contienen la palabra "salud" en su contenido.

### Respuestas de la API

La API devolverá diferentes respuestas dependiendo de la solicitud que realices:

- Si la solicitud se realiza correctamente y se encuentra la información solicitada, la API devolverá los detalles correspondientes.
- Si no se encuentra la información solicitada, la API devolverá un mensaje indicando que no se encontró la información solicitada.

### Consideraciones adicionales

- Esta API utiliza una base de datos predefinida que contiene información sobre tutelas y decretos. Por lo tanto, las búsquedas solo devolverán resultados disponibles en esta base de datos.
- Asegúrate de enviar solicitudes válidas siguiendo el formato correcto para cada tipo de búsqueda.

¡Gracias por utilizar nuestra API de búsqueda de información!
