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

# 6) Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}

lista_chaves = list(dicionario.keys())
lista_valores = list(dicionario.values())

print("Chaves:", lista_chaves)
print("Valores", lista_valores)

# 7) Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [8, 13, 22, 15, 30, 17, 18, 48, 72]
idades_filtradas = [idade for idade in idades if idade >= 18]

print(idades_filtradas)

# 8) Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
media = sum(numeros) / len(numeros)
print(media)

# 9) Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)

# 10) Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico e calcular a media antes e depois.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

lista_valores_antigos = [produto["preço"] for produto in produtos]

# Atualizar o preço do produto com id 3 para 320
for produto in produtos:
    if produto["id"] == 3:
        produto["preço"] = 320

lista_valores_novos = [produto["preço"] for produto in produtos]

media_antiga = sum(lista_valores_antigos) / len(lista_valores_antigos)
media_nova = sum(lista_valores_novos) / len(lista_valores_novos)

print(produtos)
print(f"A media antiga é: {media_antiga}")
print(f"A media nova é: {media_nova}")

