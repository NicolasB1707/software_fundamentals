Proceso DadosConDosVidas
    Definir dado1, dado2, contador, vidas Como Entero
    vidas = 2
    contador = 0

    Escribir "=== SIMULADOR DE DADOS CON DOS VIDAS ==="
    Escribir "Tienes ", vidas, " vidas para sacar doble 6."
    Escribir ""

    Mientras vidas > 0 Hacer
        contador = contador + 1
        dado1 = Azar(6) + 1  // Genera número entre 1 y 6
        dado2 = Azar(6) + 1
        Escribir "Lanzamiento ", cont
