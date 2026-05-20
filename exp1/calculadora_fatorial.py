#calculadora_fatorial

import math


# Captura o valor digitado pelo usuário e converte de string para inteiro usando int()
numero_usuario = int(input("Digite o número para fatoriar: "))

if numero_usuario < 0:
    print("Fatorial não existe para números negativos!")
else:
    resultado_fatorial = math.factorial(numero_usuario)
    print(f"Resultado da fatoriação de {numero_usuario}! é: {resultado_fatorial}")