# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros = []
numeros.extend(range(1,11))

for numero in numeros:
    print(numero ** 2)

# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]

lista.remove('C++')
lista.append('Ruby')
print(lista)

# 3) Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    'Titulo': 'Alice no País das Maravilhas',
    'Autor': 'Lewis Carroll',
    'Ano': '1865'
}
lista_elementos = livro.items()

for elemento in lista_elementos:
    print(elemento)

# 3.1) Adicionando um novo livro...
livro_01 = {
    'Titulo': 'Alice no País das Maravilhas',
    'Autor': 'Lewis Carroll',
    'Ano': '1865'
}

livro_02 = {
    'Titulo': 'Harry Potter',
    'Autor': 'J. K. Rowling',
    'Ano': '1997'
}

lista_livros = []

lista_livros.append(livro_01)
lista_livros.append(livro_02)

print(lista_livros)
print("\n")
print(lista_livros[1])
print("\n")
print(lista_livros[1]["Titulo"])

# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def conta_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
        
    return contagem

print(conta_caracteres("Bootcamp Python para Engenharia de Dados"))

# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
dicionario_precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco_total = sum(dicionario_precos[item] for item in lista_compras)
print(f"O preco total é: R$ {preco_total}")

