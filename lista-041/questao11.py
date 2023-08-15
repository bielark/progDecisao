'''11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.'''

a = int(input("informe um numuero com 3 algarismo"))
b = a / 100

if (a >= 100):
    print(f"o algarismo dde sse numerp e {b}")
