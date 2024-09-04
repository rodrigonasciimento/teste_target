""" 
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 

escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

#Aqui estou interagindo com o usuário solicitando o número que ele deseja saber e também imprimindo o relatório das informações.

from funcao_sequencia import sequenciaFib
from funcao_verificacao import pertenceFib

print("Vamos verificar se o número que você informar abaixo pertence ou não na sequência de Fibonacci\n")
num = int(input("Digite um número desejado: "))

resultado = pertenceFib(num)
lista = sequenciaFib(num)
print("Sequência de Fibonacci:\n",lista)
print("Número digitado:\n",num)
   