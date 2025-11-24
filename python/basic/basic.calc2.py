#Algoritm description: Basic calc v2
#Get two numbers 
#Add, sub, mul, div
#Print results

import os

os.system('clear')
#1. Initialize vars and/or constants (Inputs)

#Escribir "Enter number 1: " //Show message from pc to user
#Leer num1 //User enter a number and program reads it
#print("Please, enter number 1: ")
num1 = float(input("Please, enter number 1: "))
#print(type(num1))

#Escribir "Enter number 2: " //Show message from pc to user
#Leer num2 //User enter a number and program reads it
#print("Please, enter number 2: ")
num2 = float(input("Please, enter number 2: "))
#print(type(num2))

	#2. Initialize vars and/or const
	# inputs
num1 =10
num2 = 3
	#3.processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2
	#4. Outputs without f-strings
print("addition: ",add, type(add))
print("subtraction:",subs,type(subs))
print("Multipication:",mult,type(mult))
print("Division:",div,type(div))
	
    #4. Outputs with f-strings
print( f"addition: {add}")    
print( f"subtraction: {subs}")
print( f"Multipication: {mult}")
print( f"Division: {div}")
