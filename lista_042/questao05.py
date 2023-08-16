'''5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste. '''

a = int(input("informe um estado brasileiro em sigla"))

if(a =="RJ"):
    print(f"{a} esta no sudeste")
elif(a == "SP"):
    print(F"{a} esta no sudeste")
elif(a == "ES"):
    print(f"{a} esta no sudeste")
elif(a=="MG"):
    print(f"{a} esta no sudeste")
else:
    print(F"{a}esse estado noa esta no sudeste")