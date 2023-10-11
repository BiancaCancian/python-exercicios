#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float (input("Digite o seu salário: "))

aumento = 0.15

if salario > 1250:
    aumento = 0.10

aumento = salario * aumento

print(f"Seu aumento será de: R$ {aumento: 7.2f}")