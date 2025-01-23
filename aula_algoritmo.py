## Algoritmo de Ordenação Bubble Sort

lista_numeros = [40,50,60,70,0,-408593,1,50]


def ordena_numeros(numeros):
    nova_lista_numeros = lista_numeros.copy()

    for i in range(len(lista_numeros)):
        for j in range(i+1, len(lista_numeros)):
            if lista_numeros[i] > lista_numeros[j]: # se numero na posicao i > numero na posicao j
                lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i] # realiza a troca
    
    return nova_lista_numeros

nova_lista = ordena_numeros(lista_numeros)
print(lista_numeros)