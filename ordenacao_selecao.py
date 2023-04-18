def buscaMenor(arr): # Função que busca o menor valor do array
    menor = arr[0] # Inicializa a variável menor com o primeiro valor do array
    menor_indice = 0 # Inicializa a variável menor_indice com o índice 0
    for i in range(1, len(arr)): # Percorre o array a partir do segundo elemento
        if arr[i] < menor: # Verifica se o elemento atual é menor que o menor
            menor = arr[i] # Se for, atualiza a variável menor
            menor_indice = i # Atualiza a variável menor_indice
    return menor_indice # Retorna o índice do menor valor

def ordenacaoporSelecao(arr): # Função que ordena o array
    novoArr = [] # Cria um novo array vazio
    for i in range(len(arr)): # Percorre o array
        menor = buscaMenor(arr) # Busca o menor valor do array
        novoArr.append(arr.pop(menor)) # Adiciona o menor valor do array ao novo array
    return novoArr # Retorna o novo array ordenado

def printarr(arr): # Função que imprime o array
    for i in range(0, len(arr)): # Percorre o array
        print(arr[i])   # Imprime o elemento atual

lista = [5, 3, 6, 2, 10] # Cria um array com os valores a serem ordenados
lista_ordenada = ordenacaoporSelecao(lista) # Chama a função que ordena o array
printarr(lista_ordenada) # Imprime o array ordenado


# Saída esperada: 2, 3, 5, 6, 10