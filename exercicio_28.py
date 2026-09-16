# DECLARAR
vendas: int; preco_atual: float; preco_novo: float
# INÍCIO
# LER
vendas = int(input("Insira a venda mensal: "))
preco_atual = float(input("Insira o preço atual: "))

preco_novo = preco_atual

if vendas < 500 and preco_atual < 30:
    preco_novo = preco_atual * 1.10
elif vendas >= 500 and vendas < 1000 and preco_atual >= 30 and preco_atual < 80:
    preco_novo = preco_atual * 1.15
elif vendas >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual * 0.95

# EXIBIR
print(preco_novo)
# FIM
