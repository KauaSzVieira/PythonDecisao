# DECLARAR
hora_inicio: int; minuto_inicio: int; hora_final: int; minuto_final: int
inicio: int; final: int; duracao: int; horas: int; minutos: int
# INÍCIO
# LER
hora_inicio = int(input("Insira a hora de início: "))
minuto_inicio = int(input("Insira os minutos de início: "))
hora_final = int(input("Insira a hora final: "))
minuto_final = int(input("Insira os minutos finais: "))

inicio = hora_inicio * 60 + minuto_inicio
final = hora_final * 60 + minuto_final

if final <= inicio:
    final = final + 24 * 60

duracao = final - inicio
horas = duracao // 60
minutos = duracao % 60

# EXIBIR
print(horas, "hora(s) e", minutos, "minuto(s)")
# FIM
