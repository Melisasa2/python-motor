import random
import faker

# Generar datos de muestra utilizando Faker
fake = faker.Faker()

palabras_clave = ["violencia", "estafa", "alimentos", "salud", "pensión", "medicinas"]


# Función para generar una tutela simulada
def generar_tutela_es_ajustado(id):
    # Seleccionar una palabra clave aleatoriamente para incluir en el resumen
    palabra_clave = random.choice(palabras_clave)
    parte1 = fake.sentence(nb_words=6, ext_word_list=None)
    parte2 = fake.text(max_nb_chars=180)
    # Combinar las partes incluyendo la palabra clave una sola vez
    resumen = f"{parte1} {palabra_clave} {parte2}"
    return {
        "id": f"tutela{id}",
        "titulo": fake.sentence(nb_words=6),
        "resumen": resumen,
        "decreto": str(random.randint(1000, 9999))  # Generar un número de decreto aleatorio
    }

# Generar 100 muestras de tutelas con los ajustes especificados
listado_tutelas_es_ajustado = [generar_tutela_es_ajustado(i) for i in range(1, 101)]

# Mostrar las primeras 5 tutelas para verificar
listado_tutelas_es_ajustado[:5]

print(listado_tutelas_es_ajustado)

