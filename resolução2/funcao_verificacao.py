#Aqui estou criando outra função para verificar se o número informado pertence ou não a sequênca.
from funcao_sequencia import sequenciaFib

def pertenceFib(verNum):
    sequencia = sequenciaFib(verNum)
    if verNum in sequencia:
      print("Esse número pertence a lista de Fibonacci!\n")
    else:
      print("Esse número não pertece a lista de Fibonacci!\n")