"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json

with open('./resolucao3/dados.json', 'r') as arquivo:
  faturamento = json.load(arquivo)

#Aqui estou filtrando o faturamento para que seja ignorado os dias com faturamento de 0
filtro = [dia['valor'] 
          for dia in faturamento 
            if dia['valor'] >0]

#Aqui estou trazendo o maior, menor e média do faturamento
menorValor = min(filtro)
print(f"O menor valor do faturamento foi no mês foi {menorValor}")
maiorValor = max(filtro)
print(f"O maior valor do faturamento foi no mês foi {maiorValor}")
mediaValor = sum(filtro)/ len(filtro)
print(f"A média do faturamento mensal é de {mediaValor}")
diasAcimaDaMedia = sum(1 for dia in filtro if dia > mediaValor)
print(f"Quantidade de dias que o faturamento foi acima da média {diasAcimaDaMedia}")