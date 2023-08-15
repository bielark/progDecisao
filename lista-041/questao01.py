'''1) Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.'''


a = float(input("me de um numero:"))

if(a > 20 ):
    b = a / 2
    print(f"a metade do seu numero {b}")
else:
    print(f"esse e seu numero sem alteraçao {a}")

print("fim do programa!")