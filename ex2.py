#Escreva um programa que leia três números e que imprima o maior e o menor

primeiro_valor = int(input("Digite o primeiro valor:"))
segundo_valor = int(input("Digite o segundo valor:"))
terceiro_valor = int(input("Digite o terceiro valor:"))

maior = primeiro_valor
if segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor

if terceiro_valor > primeiro_valor and terceiro_valor > primeiro_valor:
    maior = terceiro_valor

menor = primeiro_valor
if segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor = segundo_valor

if terceiro_valor < primeiro_valor and terceiro_valor < segundo_valor:
    menor = terceiro_valor
    
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")

