Algoritmo reto_condicional_3
	Definir num_usuario como Entero
	Mostrar "Ingrese un numero entero (positivo o negativo): "
	Leer num_usuario
	
	si num_usuario > 0 Entonces
		si num_usuario mod 2 = 0 Entonces
			Mostrar "El numero entero es par positivo"
		SiNo
			Mostrar "El numero es impar negativo"
		FinSi
	SiNo
		si num_usuario mod 2 = 0 Entonces
			Mostrar "El numero entero es par negativo"
		SiNo
			Mostrar "El numero entero es impar negativo"
		FinSi
	FinSi
FinAlgoritmo
