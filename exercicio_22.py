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

# EXIBIR
print(menor, maior)
# FIM
