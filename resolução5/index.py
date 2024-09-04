""" 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
 """

from funcao_inverter import invertendo

inverter = input("Digite a palavra que deseja inverter: ")
string_invertida = invertendo(inverter)

print("\n A palavra invertida ficou assim: ", string_invertida)
