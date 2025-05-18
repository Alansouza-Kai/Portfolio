'''Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

Apenas os 3 primeiros mais assistidos
Os últimos 2 mais assistidos
A lista em ordem alfabética
Em que posição está “O rei leão”
'''

"""
1 -Avatar: (2009)
2 - Vingadores: Ultimato: (2019)
3 - Avatar: O Caminho da Água: (2022)
4 - Titanic: (1997)
5 - Star Wars: Episódio VII - O Despertar da Força: (2015)
6 - Vingadores: Guerra Infinita: (2018)
7 - Homem-Aranha: Sem Volta Para Casa: (2021)
8 - Jurassic World: O Mundo dos Dinossauros: (2015)
9 - O Rei Leão: (2019)
10 - Os Vingadores: (2012) 
"""

Filmes = ("Avatar", "Vingadores: Ultimato", "Avatar: O Caminho da água", "Titanic", "Star Wars: Episódio VII - O Despertar da Força", "Vingadores: Guerra Infinita","Homem-Aranha: Sem Volta Para Casa","Jurassic World: O Mundo dos Dinossauros","O Rei Leão","Os Vingadores")

for i in range (3):
    print(Filmes[i])

print("--*---")

for j in range (len(Filmes),len(Filmes)-2,-1):
    print(Filmes[j-1])
print("--*---")

print(sorted(Filmes))

print("--*---")

print(Filmes.index("O Rei Leão"))