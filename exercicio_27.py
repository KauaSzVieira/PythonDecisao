# DECLARAR
voltas: int; extensao: float; tempo: float; distancia: float; velocidade: float
# INÍCIO
# LER
voltas = int(input("Insira o número de voltas: "))
extensao = float(input("Insira a extensão do circuito em metros: "))
tempo = float(input("Insira o tempo em minutos: "))

distancia = voltas * extensao / 1000
velocidade = distancia / (tempo / 60)

# EXIBIR
print(velocidade)
# FIM
