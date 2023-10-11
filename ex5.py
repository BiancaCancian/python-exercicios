#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação 
# como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario: "))
anos_pagar = int(input("Quantos anos pra pagar: "))
meses = anos_pagar * 12
prestacao = valor / meses

if prestacao > salario * 0.3:
    print("Infelizmente você não pode obter o emprestimo!")
else:
    print (f"Valor da prestação: R$ {prestacao:7.2f} Emprestimo OK!")
    
