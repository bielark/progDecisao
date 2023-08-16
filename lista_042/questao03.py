'''3. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000.'''


a = int(input("informe um numero "))
if(a<1000):
    print("seu numero esta abaixo de 1000")
elif(a>1000 and a<5000):
    print("seu numero esta entre 1000 e 5000")
elif(a>5001 and a<8000):
    print("seu numero esta entre 5001 e 8000")
else:
    print("seu numero esta acima de 8000")
