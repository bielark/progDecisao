'''
Crie um programa que pergunte um número ao usuário. Em seguida o programa deve
informar se o número inserido está abaixo de 100, entre 100 e 200 ou acima de 200.
'''


num1 = int(input("informe um numero:"))

if (num1 < 100):
    print(f"{num1} esta abaixo de 100")
elif (num1 <= 200):
    print(f"{num1} esta entre 100 e 200")
else:
    print(f"{num1} esta acima de 200")