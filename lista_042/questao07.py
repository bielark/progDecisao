'''7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.'''

a = int(input("infome um numero"))
b = int(input("outro numero"))

if(a > b ):
    print(f"{a} e maior que {b}")
elif(b>a):
    print(f"{b} e maior que {a}")
else:
    print("os dois são iguais")
