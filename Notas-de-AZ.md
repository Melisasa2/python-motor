Imagina que tengo una mesa llena de papeles con diferentes números escritos en ellos, todos mezclados. Entonces, este código funciona como mi asistente personal. Va tomando cada papel, mira el número escrito en él y decide en qué carpeta colocarlo. Si ve que ya hay una carpeta con ese número, simplemente agrega el papel allí; si no, crea una nueva carpeta. Al final, me entrega un índice ordenado donde puedo ver rápidamente qué papeles están en cada carpeta. Es como si mi asistente estuviera organizando todos mis documentos en diferentes carpetas para que pueda encontrar lo que necesito mucho más rápido cuando lo necesite. ¡Es muy útil, especialmente cuando tengo un montón de papeles y necesito mantenerlos todos organizados!

Imagina que tenemos una lista de casos legales (`tutelas`) que se ven así:

```python
tutelas = [
    {'decreto': 'A', 'contenido': '...'},
    {'decreto': 'B', 'contenido': '...'},
    {'decreto': 'A', 'contenido': '...'},
    {'decreto': 'C', 'contenido': '...'},
    {'decreto': 'B', 'contenido': '...'}
]
```

Ahora, vamos a ejecutar el código paso a paso:

1. Creamos una caja vacía llamada `AZ`.
2. Empezamos a recorrer la lista `tutelas`.
3. Tomamos el primer caso legal: `{'decreto': 'A', 'contenido': '...'}`. El decreto es 'A'.
   - Verificamos si 'A' está en la caja `AZ`. No está.
   - Creamos una nueva carpeta para 'A' dentro de la caja `AZ`.
   - Ponemos este caso legal dentro de la carpeta 'A'.
4. Tomamos el segundo caso legal: `{'decreto': 'B', 'contenido': '...'}`. El decreto es 'B'.
   - Verificamos si 'B' está en la caja `AZ`. No está.
   - Creamos una nueva carpeta para 'B' dentro de la caja `AZ`.
   - Ponemos este caso legal dentro de la carpeta 'B'.
5. Tomamos el tercer caso legal: `{'decreto': 'A', 'contenido': '...'}`. El decreto es 'A'.
   - Verificamos si 'A' está en la caja `AZ`. Sí está.
   - Ponemos este caso legal dentro de la carpeta 'A'.
6. Tomamos el cuarto caso legal: `{'decreto': 'C', 'contenido': '...'}`. El decreto es 'C'.
   - Verificamos si 'C' está en la caja `AZ`. No está.
   - Creamos una nueva carpeta para 'C' dentro de la caja `AZ`.
   - Ponemos este caso legal dentro de la carpeta 'C'.
7. Tomamos el quinto caso legal: `{'decreto': 'B', 'contenido': '...'}`. El decreto es 'B'.
   - Verificamos si 'B' está en la caja `AZ`. Sí está.
   - Ponemos este caso legal dentro de la carpeta 'B'.
8. Hemos terminado de recorrer todos los casos legales en `tutelas`.
9. Devolvemos la caja `AZ`, que contiene todas las carpetas organizadas por número de decreto y cada carpeta contiene los casos legales correspondientes.

Al final, obtendríamos algo como:

```python
{
    'A': [
        {'decreto': 'A', 'contenido': '...'},
        {'decreto': 'A', 'contenido': '...'}
    ],
    'B': [
        {'decreto': 'B', 'contenido': '...'},
        {'decreto': 'B', 'contenido': '...'}
    ],
    'C': [
        {'decreto': 'C', 'contenido': '...'}
    ]
}
```

