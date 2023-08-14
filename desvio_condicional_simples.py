'''
Crie um programa que pergunte dois números ao usuário.
Em seguida o programa deverá somar os dois números e apresentar o
resultado se o valor for maior que 10.
'''

num1 = int(input("informe um numero"))
num2 = int(input("informe outro numero"))

soma = num1 + num2

if(soma > 10):
    print(f"a soma dos valores inserido e {soma}")

print(f"fim do programa")

