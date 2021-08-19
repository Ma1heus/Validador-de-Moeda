from Desafio112.utilidadescev import moeda
from Desafio112.utilidadescev import dado


print('-=' * 10)
print('\033[0;33mFORMATAÇÃO DE MOEDA\033[m')
print('-=' * 10)

p = dado.leiaDinheiro('Digite o preço: R$')
aum = dado.leiaDinheiro('Deseja ver um aumento de quanto? (%) ')
dim = dado.leiaDinheiro('Deseja ver um decrescimo de quanto? (%) ')
moeda.resumo(p, aum, dim)
