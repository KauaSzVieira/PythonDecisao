# DECLARAR
valor1: float; valor2: float; maior: float
# INÍCIO
# LER
valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

# EXIBIR
print(maior)
# FIM
