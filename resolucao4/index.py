""" 
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.   """

import json
from funcao_calcular import calcularPercentual

with open('./resolucao4/dados.json', 'r') as arquivo:
  faturamento = json.load(arquivo)

faturamentoTotal = sum(dado['valor'] for dado in faturamento)

print("Esse é o valor total do faturamento: ", faturamentoTotal)

for dado in faturamento:
  estado = dado['estado']
  valor = dado['valor']
  percentual = calcularPercentual(valor, faturamentoTotal)
  print(f"\nO percentual do {estado}: {percentual: .2f}%")

