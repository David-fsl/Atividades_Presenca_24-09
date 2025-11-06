import random
import timeit

def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range (1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

lista_original = list(range(1000))
random.shuffle(lista_original)

lista_para_selecao = lista_original[:]

inicio = timeit.default_timer()
resultado_selecao = ordenacaoporSelecao(lista_para_selecao)
fim = timeit.default_timer()
print(f"Ordenação por Seleção levou: {fim - inicio:.6f} segundos")


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
inicio = timeit.default_timer()
resultado_selecao = ordenacaoporSelecao(lista_para_selecao)
fim = timeit.default_timer()
print(f"Ordenação por Seleção levou: {fim - inicio:.6f} segundos")