#Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.

num1 = float (input("Primeiro numero: "))
num2 = float (input("Segundo numero:"))

operacao = input ("Digite a operação a realizar (+, -, * ou /)")

if operacao == "+":
    resultado = num1 + num2
    
elif operacao == "-":
    resultado = num1 - num2
    
elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    resultado = num1 / num2
    
else:
    print("Operação invalida!")
    resultado = 0 

print("Resultado: ", resultado)