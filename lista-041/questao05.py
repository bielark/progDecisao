'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno
'''

a = float(input("diga sua nota do primeiro bimestri"))
b = float(input("diga sua nota do segundo bimestri"))
c = float(input("diga sua nota do terceiro bimestri"))
d = float(input("diga sua nota do quarto bimestri"))

e = (a + b + c + d ) / 4

if(e >= 5.0):
    print(F"parabem vc esta aprovado com {e}")
else:
    print(f"você nao foi aprovado:{e}")