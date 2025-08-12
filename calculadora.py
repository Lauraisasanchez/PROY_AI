def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Programa principal
print("=== Calculadora Básica ===")
x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))

print(f"Suma: {sumar(x, y)}")
print(f"Resta: {restar(x, y)}")
print(f"Multiplicación: {multiplicar(x, y)}")
print(f"División: {dividir(x, y)}")
