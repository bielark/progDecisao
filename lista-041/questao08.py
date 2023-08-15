'''8) Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10'''

num = int(input("informe um numero"))


resposta = (f"{num} nao esta na faixa de 1 a 10",f" {num} esta na faixa de 1 a 10")[num >=1 and num <= 10]

print(resposta)






