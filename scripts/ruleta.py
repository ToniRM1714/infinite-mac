import random
import sys

def ruleta_no_repetitiva(sets_de_opciones):
    """
    Simula una ruleta que consume opciones sin repetir.

    :param sets_de_opciones: Lista de listas, cada una con opciones.
    """
    for i, opciones in enumerate(sets_de_opciones):
        print(f"\n--- Iniciando Ruleta {i+1} ({len(opciones)} opciones) ---")

        # Mezclamos las opciones para que el orden sea aleatorio
        mazo = opciones[:]
        random.shuffle(mazo)

        turno = 1
        while mazo:
            seleccion = mazo.pop()
            print(f"Turno {turno}: Ha salido -> {seleccion}")
            turno += 1

    print("\n¡Se han agotado todas las ruletas!")

if __name__ == "__main__":
    # Ejemplo basado en la petición del usuario
    mis_ruletas = [
        ["Opción A", "Opción B", "Opción C"],
        ["1", "2", "3", "4", "5"]
    ]

    ruleta_no_repetitiva(mis_ruletas)
