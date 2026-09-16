# DECLARAR
a: int; b: int; maior: int; menor: int
# INÍCIO
# LER
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

if maior % menor == 0:
    print("O maior é múltiplo do menor")
else:
    print("O maior não é múltiplo do menor")
# FIM
