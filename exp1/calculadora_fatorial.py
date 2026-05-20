#calculadora_fatorial

import math

numero_usuario = int(input("Digite o número para fatoriar: "))

if numero_usuario < 0:
    print("Fatorial não existe para números negativos!")
else:
    resultado = math.factorial(numero_usuario)
    print(f"Resultado da fatoriação de {numero_usuario}! é: {resultado}")
