import csv

caminho_arquivo = "exemplo.csv"

arquivo_csv = []

with open(file=caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)