'''4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.'''

a = int(input("informe um valor inteiro: "))

b = a % 4
c = a % 5

if( b == 0 and c == 0):
    print("seu numero e divisivel")
else:
    print("seu numero nao e divisivel pelo 4 e 5")