# Estou criando uma função onde estou criando a sequência de Fibonacci e colocando um limite conforme o número que o usuário digitar.

def sequenciaFib(total):
  sequencia = [0, 1]
  while len(sequencia) < int(total): 
    prox = sequencia[-1] + sequencia[-2]
    if prox > int(total):
      break
    sequencia.append(prox)
  return sequencia