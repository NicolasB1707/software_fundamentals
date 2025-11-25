import random

# Función para lanzar los dados
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)

# Función principal del juego
def juego():
    contador = 0
    pares_totales = 0

    print(" JUEGO DE LOS DOS DADOS ")
    print("Tu objetivo es sacar un par de 6.")

    while True:
        contador += 1
        dado1, dado2 = lanzar_dados()

        print(f"Lanzamiento {contador}: Salió {dado1} y {dado2}")

        # Contar pares (cualquier número)
        if dado1 == dado2:
            pares_totales += 1

        # Condición de salidas
        if dado1 == 6 and dado2 == 6:
            print(" ¡Sacaste un par de 6! ¡Ganaste! ")
            break
    
    # Mostrar estadísticas
    print("--- ESTADÍSTICAS ---")
    print(f"Total de lanzamientos: {contador}")
    print(f"Total de pares obtenidos: {pares_totales}")
    print("--------------------")

# Menú para repetir el juego
def main():
    while True:
        juego()
        opcion = input("¿Quieres jugar nuevamente? (s/n): ").lower()
        if opcion == 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

# Iniciar menú
main()