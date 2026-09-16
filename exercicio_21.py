# DECLARAR
n1: float; n2: float; n3: float; n4: float; media: float
# INÍCIO
# LER
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
n3 = float(input("Insira a terceira nota: "))
n4 = float(input("Insira a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print("APROVADO")
elif media >= 3:
    print("EXAME")
else:
    print("RETIDO")
# FIM
