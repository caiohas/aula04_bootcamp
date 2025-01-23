## Algoritmo de Ordenação Bubble Sort

# lista_numeros = [40,50,60,70,0,-408593,1,50]
# lista_numeros_02 = [40,60,27,0,-4,15,50]
# lista_numeros_03 = [29,25,8,702,10,-403,19,550]

def ordena_lista_numeros(numeros) -> list:
    nova_lista_numeros = numeros.copy()

    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]: # se numero na posicao i > numero na posicao j
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i] # realiza a troca
    
    return nova_lista_numeros

# nova_lista = ordena_lista_numeros(lista_numeros)
# nova_lista_02 = ordena_lista_numeros(lista_numeros_02)
# nova_lista_03 = ordena_lista_numeros(lista_numeros_03)

# print(lista_numeros)
# print(lista_numeros_02)
# print(lista_numeros_03)