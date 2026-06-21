# Guía: Ruleta No Repetitiva

Esta guía explica cómo implementar una "ruleta" que selecciona opciones al azar sin repetirlas y cambia a un nuevo conjunto de opciones una vez que se agotan las actuales.

## Lógica del Sistema

Para evitar que una opción se repita, no debemos usar un generador de números aleatorios simple cada vez. En su lugar, debemos usar un sistema de **muestreo sin reemplazo**:

1.  **Cargar el conjunto**: Tomas tus 3 opciones iniciales.
2.  **Mezclar (Shuffle)**: Desordenas la lista al azar.
3.  **Consumir**: Vas extrayendo elementos de esa lista mezclada uno a uno.
4.  **Transición**: Cuando la lista esté vacía, cargas el siguiente conjunto (las 5 opciones) y repites el proceso.

## Ejemplo en Python

He incluido un script en `scripts/ruleta.py` que demuestra exactamente esta lógica. Puedes ejecutarlo para ver cómo funciona:

```bash
python3 scripts/ruleta.py
```

### Código de ejemplo:

```python
import random

ruletas = [
    ["Opcion 1", "Opcion 2", "Opcion 3"],
    ["A", "B", "C", "D", "E"]
]

for opciones in ruletas:
    random.shuffle(opciones)
    for seleccion in opciones:
        print(f"Resultado: {seleccion}")
```

## Aplicación en Juegos o Chatbots

Si estás usando esto en un entorno de Rol o Chat (como SillyTavern o Mazmo):

1.  **Prompt Engineering**: Puedes instruir a la IA diciéndole: "Tienes una lista de opciones [A, B, C]. Elige una que no hayas usado antes. Cuando las uses todas, pasa a la lista [1, 2, 3, 4, 5]".
2.  **Variables de Estado**: Necesitarás guardar en una variable qué opciones han salido ya para que la lógica persista entre turnos.
