# DECLARAR
valor1: int; valor2: int; diferenca: int
# INÍCIO
# LER
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))

if valor1 > valor2:
    diferenca = valor1 - valor2
else:
    diferenca = valor2 - valor1

# EXIBIR
print(diferenca)
# FIM
