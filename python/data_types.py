
numberx = 10
print(type(numberx))

numberx = 10.5
print(type(numberx))

numberx = 8J
print(type(numberx))

n1 = "1"
n2 = "3"

add = n1 + n2
print(add)

suma_datos = True & True
print("suma datos:", suma_datos)
print(type(suma_datos))

##################################
x = True - False
print(x) 
print(type(x))

# El resto del código visible
print("############################")
print("p and q")
print("############################")
print(f"V ^ V: {True and True}")
print(f"V ^ F: {True and False}")
print(f"F ^ V: {False and True}")
print(f"F ^ F: {False and False}")

print("############################")
print("p or q")
print("############################")
print(f"V V V: {True or True}")
print(f"V V F: {True or False}")
print(f"F V V: {False or True}")
print(f"F V F: {False or False}")