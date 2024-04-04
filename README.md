# Notas


- Ejecucion en local
Primero tube que aprender como ejecutar lo que habia y no me deja asi que inestigando tengo que tener un archivo `requirements.txt` que tiene lo que voy a usar, pero par poderlos usar toca crear un espacio donde colocarlos que es con `python -m venv venv` he estado investigando el porque pero aun no entiendo la razon, y mas ensima despues de eso hi si se agregan a ese espacio asi `pip install -r requirements.txt`.








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
