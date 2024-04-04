# Notas


- Ejecucion en local

Primero tuve que aprender como ejecutar lo que habia, investigando tengo que tener un archivo `requirements.txt` que tiene lo que voy a usar, para poderlo usar toca crear un espacio donde colocarlos que es con `python -m venv venv` he estado investigando el porque pero aun no entiendo la razon, ahi si se agregan a ese espacio asi `pip install -r requirements.txt`.


- [Tutorial de FastAPI https://fastapi.tiangolo.com/#create-it](https://fastapi.tiangolo.com/#create-it)

Haciendo el tutorial de la pagina de fastAPI encontre que toca agregar mas cosas a usar, las colocare en el archivo `requirements.txt` al igual de las demas, ya agrege `uvicorn[standard]` en el. al colocar e la terminal el comando del tutorial me da 
```bash
(venv) @Melisasa2 ➜ /workspaces/python-motor (main) $ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/workspaces/python-motor']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14962] using WatchFiles
INFO:     Started server process [14964]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     10.240.2.99:0 - "GET / HTTP/1.1" 200 OK
INFO:     10.240.2.99:0 - "GET /favicon.ico HTTP/1.1" 404 Not Found
```
"Uvicorn" es como el encargado de hacer funcionar mi aplicación web. Cuando ejecuto uvicorn main:app --reload, básicamente le estoy diciendo a Uvicorn: "toma el código que escribí en el archivo main.py, donde está la parte principal de mi aplicación (que se llama app), y ejecútalo como un sitio web en mi computadora".

Y lo del --reload es como un truco útil que le digo a Uvicorn: "Si veo un error o quiero hacer algún cambio en mi código, no quiero tener que apagar y volver a encender el servidor cada vez. Así que, por favor, actualízate automáticamente cuando haga cambios".

Es como si estuviera diciendo a Uvicorn: "Haz que mi aplicación web funcione y actualízate automáticamente si cambio algo".

Cuando veo esas líneas que comienzan con INFO, es como si estuviera recibiendo actualizaciones sobre lo que está pasando en mi programa mientras está en funcionamiento. Es como si alguien me estuviera contando lo que está sucediendo adentro.

Por ejemplo, cuando veo 10.240.2.99:0 - `GET / HTTP/1.1` 200 OK, es como si alguien estuviera pidiendo ver la página principal de mi programa. Me alegra ver que todo está bien (200 OK) y que puedo mostrarles la página sin problemas.

No estoy muy segura de lo que significa `GET /favicon.ico HTTP/1.1 404 Not Found`. Parece que alguien está buscando algo, pero no estoy seguro de qué es (404 Not Found). Parece ser algo que se llama favicon.ico, pero no tengo idea de qué es eso, segun entiendo eso se define en el codigo pero ahi no hay nada de favicon.ico

el resultado de mi programa fue 
```json
{
  "Hello": "World"
}
```

siguiendo las pruebas que me están indicando. Cuando escribo /items/5?q=somequery, algo aparece en la pantalla. ¡Es como si mi programa estuviera respondiendo tal como me dijeron en el tutorial!

Lo que veo en la pantalla es algo como `{"item_id":5,"q":"somequery"}`. Hmm, parece que esto es la información sobre el artículo número 5, y también algo que estoy `"somequery"` que es el texto que se mando a `?q=somequery`

- Implementación de Endpoint con FastAPI
Con eso creo que ya puedo hacer el `http://[mi_ip]/api/v1/search?tipo_tutela=salud` que e piden ya que veo que es muy parecido
con la funcion 
```python

@app.get("/api/v1/search")
def search(tipo_tutela: Union[str, None] = None):
    return {"tipo_tutela": tipo_tutela}
```
al probar `/api/v1/search?tipo_tutela=salud` me dio como resultado 
```json
{"tipo_tutela":"salud"}
```


# Ejercicio: Motor de Búsqueda para Tutelas del MinJusticia

## Descripción

En este ejercicio, desarrollarán un motor de búsqueda que permitirá a los usuarios buscar y listar las tutelas cuyo contenido tenga las palabras (violencia o estafa o alimentos o salud o pensión o medicinas) en el resumen de la tutela coincida con el parámetro de búsqueda proporcionado (tipo_tutela). Este sistema será especialmente útil para el MinJusticia, permitiendo un acceso eficiente y rápido a la información relevante de las tutelas.

Se espera que utilicen las técnicas y estructuras que mas se ajusten para optimizar las búsquedas, estructurando los datos de manera que puedan inferir rápidamente qué tutelas coinciden con los términos de búsqueda. Además, implementarán un endpoint utilizando FastAPI para interactuar con su motor de búsqueda.

## Requisitos

1. **Preprocesamiento de Datos**: Deberán comenzar por procesar el conjunto de datos de tutelas para normalizar el texto. Esto incluye convertir el texto a minúsculas, eliminar puntuación y stopwords, y opcionalmente aplicar stemming o lematización.

2. **Indexacion**: Construya un algoritmo que mapee cada decreto único a la lista de tutelas que lo mencionan.

3. **Desarrollo del Motor de Búsqueda**: Utilizando las técnicas y estructuras que mas se ajusten para optimizar las búsquedas, implementen la lógica de búsqueda que permita encontrar rápidamente las tutelas relevantes basadas en el decreto buscado.

4. **Implementación de Endpoint con FastAPI**: Desarrollen un endpoint `/api/v1/search` que reciba como parámetro de búsqueda el tipo_tutela y devuelva una lista de las tutelas que coinciden con dicho tipo_tutela.

## Resultado Esperado

Se espera que entreguen un proyecto que incluya:

1. **Código Fuente**: El código fuente de su motor de búsqueda, incluyendo el preprocesamiento de datos, y la lógica de búsqueda.

2. **API**: Una API construida con FastAPI que exponga el endpoint `/api/v1/search`.

3. **Documentación**: Una breve documentación que explique cómo utilizar su API, incluyendo ejemplos de peticiones y respuestas.

## Ejemplo de Salida

Si un usuario realiza una petición GET a `http://[mi_ip]/api/v1/search?tipo_tutela=salud`, la respuesta podría tener el siguiente formato:

```json
{
  "decreto": "1234",
  "tutelas": [
    {
      "id": "tutela1",
      "titulo": "Título de la Tutela 1",
      "resumen": "Resumen de la Tutela 1",
      "fecha": "2023-01-01"
    },
    {
      "id": "tutela2",
      "titulo": "Título de la Tutela 2",
      "resumen": "Resumen de la Tutela 2",
      "fecha": "2023-02-01"
    }
  ]
}
```

> Este ejercicio proporciona una guía clara para los estudiantes sobre cómo aplicar sus conocimientos teóricos en un proyecto práctico, fomentando el aprendizaje a través de la implementación de casos reales.

> Ademas, no solo pondrá a prueba su comprensión sobre los temas tratados en Estructuras de Datos y Algoritmos, sino que también les permitirá adquirir experiencia práctica en el desarrollo de APIs con FastAPI, conceptos de servicios, servidores etc.

> Nota: utilizar el scipt (faker.py) para generar los datos de prueba o use (mook.py) que ya contiene la data para construida.
