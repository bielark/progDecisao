'''
Crie um programa que pergunte a idade do usuário e em seguida informe se
este usuário é menor de idade ou maior de idade.
'''

idade = int(input("Informe a sua idade:"))

resposta = "você e maior de idade" if idade >= 18 else "você e menor de idade"
print(resposta)