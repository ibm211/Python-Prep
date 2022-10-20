def operacion(x,y,z):
    if z == "sumar":
        return x+y
    if z == "multiplcar":
        return x*y
    if z == "restar":
        return x-y
    else:
        return print("operacion erronea")

print("Bienvenido a la calculadora 3000: ")
z = input("Que operacion va a realizar?")
x = input("Primer numero: ")
y = input("Segundo numero: ")
print("el resultado es ",operacion(x,y,z))
