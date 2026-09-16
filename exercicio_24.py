# DECLARAR
numero: int
# INÍCIO
# LER
numero = int(input("Insira um valor inteiro: "))

if numero % 2 == 0 and numero % 3 == 0:
    print("É divisível por 2 e 3")
else:
    print("Não é divisível por 2 e 3")
# FIM
