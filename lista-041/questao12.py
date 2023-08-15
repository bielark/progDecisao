'''12) Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.'''

n1 = int(input("informe um numero: "))
n2 = int(input("informe um numero: "))
n3 = int(input("informe um numero: "))
n4 = int(input("informe um numero: "))
n5 = int(input("informe um numero: "))

maior = n1

if(maior < n2):
    maior = n2
if(maior < n3):
    maior = n3
if(maior < n4):
    maior = n4
if(maior < n5):
    maior = n5

menor = n1

if(menor > n2):
    menor=n2
if (menor > n3):
    menor = n3
if (menor > n4):
     menor = n4
if (menor > n5):
    menor = n5

print(f"o maior valor foi {maior} e o menor e {menor}")