'''. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.'''

a = int(input("informe um numero"))

if (a < 1000):
    print("seu numero esta abaixo")
elif(a>1000 and a<5000):
    print("seu numero esta entre 1000 e 5000")
else:
    print("seu numero esta acima de 5000")