from preprocessing import procesar_texto

palabras_clave = ["violencia", "estafa", "alimentos", "salud", "pensión", "medicinas"]

def crear_caja_AZ_tipo(tutelas):
    caja_AZ = {}
    for tutela in tutelas:
        resumen = tutela['resumen']
        for palabra in palabras_clave:
            if palabra in resumen:
                if palabra not in caja_AZ:
                    caja_AZ[palabra] = [] # crear carpeta vacia
                caja_AZ[palabra].append(tutela) # metemos la tutela en mi carpeta
    return caja_AZ


def crear_caja_AZ_decreto(tutelas):
    caja_AZ = {}
    for tutela in tutelas:
        decreto = tutela['decreto']
        if decreto not in caja_AZ:
            caja_AZ[decreto] = [] # crear carpeta vacia
        caja_AZ[decreto].append(tutela) # metemos la tutela en mi carpeta
    return caja_AZ




def crear_caja_clave(tutelas):
    for tutela in tutelas:
        tutela["palabras_claves"] = procesar_texto(f"{tutela['resumen']} {tutela['titulo']}")
    return tutelas


