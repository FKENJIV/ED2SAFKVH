#Retos :Ejercicios propuestos Sobre estandares y buenas practicas PEP8
#Fernando Kenji Villarroel Henzan - 220030464

def calcular_promedio():
    """Pide al usuario una serie de números y calcula su promedio."""
    numeros = []
    print("Introduce una serie de números (ingresa 'fin' para terminar):")
    while True:
        entrada = input("> ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número o 'fin'.")
    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"promedio: {promedio}")
    else:
        print("No se ingresaron números.")

if __name__ == "__main__":
    calcular_promedio()