'''4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.'''

dia = int(input("informe um dia da semana em numero"))

if(dia == 1 ):
    print("esse numero e considerado domindo")

elif(dia == 2):
    print("esse numero e considerado segunda_feira")

elif(dia == 3):
    print("esse numero e considerado terca_feira")

elif(dia == 4):
    print("esse numero e considerado quarta_feira")

elif (dia == 5):
    print("esse numero e considerado quinda_feira")

elif (dia == 6):
    print("esse numero e considerado sexta_feira")

elif (dia == 7):
    print("esse numero e considerado sabado")
else:
    print("o seu numero nao representa nenhum dia da semana")


