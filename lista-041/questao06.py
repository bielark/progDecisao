'''6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.'''

a = int(input("diga um valor"))
b = int(input("diga outro"))

if(a > b):
    print(f"a diferença deles e {a - b }")
else:
    print(f"a diferença deles e {b - a}")