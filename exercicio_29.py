# DECLARAR
tipo: int; investimento: float; valor_corrigido: float
# INÍCIO
# LER
tipo = int(input("Insira o tipo de investimento (1 ou 2): "))
investimento = float(input("Insira o valor do investimento: "))

valor_corrigido = 0

if tipo == 1:
    valor_corrigido = investimento * 1.03
elif tipo == 2:
    valor_corrigido = investimento * 1.05

# EXIBIR
if tipo == 1 or tipo == 2:
    print(valor_corrigido)
# FIM
