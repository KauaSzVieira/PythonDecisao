# DECLARAR
a: int; b: int; c: int; d: int
# INÍCIO
# LER
a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))
d = int(input("Insira o quarto valor: "))

valores = [a, b, c, d]
valores.sort()

# EXIBIR
print(valores)
# FIM
