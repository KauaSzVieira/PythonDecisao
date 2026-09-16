# DECLARAR
a: float; b: float; c: float; delta: float; x1: float; x2: float
# INÍCIO
# LER
a = float(input("Insira A: "))
b = float(input("Insira B: "))
c = float(input("Insira C: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:
    x1 = -b / (2 * a)
    print("Existe uma raiz real:", x1)
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print("Existem duas raízes reais:", x1, x2)
# FIM
