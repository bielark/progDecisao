'''6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.'''

a = int(input("diga seu ano de nacimento"))
b = int(input("diga o ano atuais"))

if(a<b):
    print(f"sua idade {b-a}")
else:
    print("dados inseridos estao incorretos")
