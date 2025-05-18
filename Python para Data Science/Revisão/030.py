#Escreva um programa que crie um dicionário com as informações de 5 livros, como título, autor, ano de lançamento e número de páginas.
# Em seguida, exiba apenas os autores dos livros.

Livros = {}
Titulo = ['a','b','c','d','e']
Autor = ['e','d','c','b','a']
Ano_de_lançamento = [2012,2013,2025,1998,2305]
Número_de_páginas = [35,564,123,2856,12]


for i in range(5):
    Livros[f"Livro {i+1}"] = {
        "Título": Titulo[i],
        "Autor": Autor[i],
        "Ano de Lançamento": Ano_de_lançamento[i],
        "Número de Páginas": Número_de_páginas[i]
    }

# Exibindo apenas os autores
print("Autores dos livros:")
for info in Livros.values():
    print(info["Autor"])

print(Livros)