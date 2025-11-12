//Algoritm description
//Basic calc v1
//Get two numbers 
//Add, sub, mul, div
//Print results

Algoritmo basic_calc
	//1. Define vars and/or const
	Definir num1, num2 Como Real
	Definir add, subs, mult, div Como Real
	//2. Initialize vars and/or const
	// inputs
	Escribir "Enter number 1:" // show message  from pc to user
	Leer num1 // user enter a number and programs reads it
	Escribir "Enter number 2:" // show message  from pc to user
	Leer num2 // user enter a number and programs reads it
	// 3.processes
	add = num1 + num2;
	subs = num1 - num2;
	mult = num1 * num2;
	div = num1 / num2;
	//4. Outputs
	Mostrar "addition: ", add;;
	Mostrar "subtraction:", subs;
	Mostrar "Multipication:", mult;	
	Mostrar "Division:", div; 
	
FinAlgoritmo
