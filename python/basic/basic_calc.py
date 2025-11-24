#Algoritm description:
""" 
Basic calc v1
Get two numbers
Add, sub, mul, div
Print results 
"""
import os

os.system('clear')
#1. Initialze vars and/or constants (inputs)
num1 =10
num2 = 5
#2.processes
add = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2

	#4. Outputs
# Outputs without f-strings
print("addition: ",add,type(add))
print("subtraction:",subs,type(subs))
print("Multipication:",mult,type(mult))
print("Division:",div,type(div))

# Outputs with f-strings
print( f"addition: {add}")    
print( f"subtraction: {subs}")
print( f"Multipication: {mult}")
print( f"Division: {div}")

