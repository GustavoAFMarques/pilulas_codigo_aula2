import random

#entrada
cotacao_atual = float(input("Insira a cotação atual: "))

#processamento
variacao_aleatoria = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao_atual * (1 + variacao_aleatoria)

#saida
print(f'variação (%): {variacao_aleatoria: .3%}')
print(f'Nova cotação: {nova_cotacao: .4f}')
