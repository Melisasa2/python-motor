from typing import Union
from mook import tutelas
from fastapi import FastAPI
from indexing import crear_caja_AZ_tipo, crear_caja_AZ_decreto, crear_caja_clave

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id, q):
    return {"item_id": item_id, "q": q}


caja_AZ_tipo_tutela = crear_caja_AZ_tipo(tutelas)
caja_AZ_decreto = crear_caja_AZ_decreto(tutelas)
caja_AZ_contenido = crear_caja_clave(tutelas)


@app.get("/api/v1/search")
def search(tipo_tutela = None, decreto = None, contenido = None):

    if tipo_tutela and tipo_tutela in caja_AZ_tipo_tutela:
        return caja_AZ_tipo_tutela[tipo_tutela]
    
    if decreto and decreto in caja_AZ_decreto:
        return caja_AZ_decreto[decreto]

    if contenido:
        return [elemento for elemento in caja_AZ_contenido if any(contenido in palabra for palabra in elemento["palabras_claves"])]

    return {"message": "No se encontró la información solicitada."}