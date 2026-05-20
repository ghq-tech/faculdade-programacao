#conversor_de_temperatura

temperatura_celsius = float(input("Digite a temperatura: ")) 
print(f"Sua temperatura em celsius é: {temperatura_celsius:.2f} °C")

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
print(f"Sua temperatura em fahrenheit é: {temperatura_fahrenheit:.2f} °F")