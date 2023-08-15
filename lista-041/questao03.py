'''
3) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

a = int(input("irfome um numero"))
resto = a % 2

if(resto == 0 ):
    print("seu numero e par")
else:
    print("seu numero e impar")

