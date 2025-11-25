import random

vidas = 2  # Número de vidas
contador = 0

print("=== SIMULADOR DE DADOS CON DOS VIDAS ===")
print(f"Tienes {vidas} vidas para sacar doble 6.\n")

while vidas > 0:
    contador += 1
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(f"Lanzamiento {contador}: salió {dado1} y {dado2}")
    
    if dado1 == 6 and dado2 == 6:
        print("¡Felicidades! Sacaste un par de 6 ")
        break
    else:
        vidas -= 1
        if vidas > 0:
            print(f"No fue doble 6. Te quedan {vidas} vidas.\n")
        else:
            print("Se te acabaron las vidas :C. Intenta de nuevo.")

print(f"\nNúmero total de lanzamientos: {contador}")