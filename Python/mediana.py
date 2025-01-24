def mediana_e_mais_proximo_media_e_pos(lista):
    if len(lista) == 0:
        return [None, None, None]
    
    lista_ordenada = []
    
    for n in lista:
        lista_ordenada.append(n)
    
    lista_ordenada.sort()
    tam = len(lista)
    
    if tam % 2 == 0:
        mediana = (lista_ordenada[tam // 2 - 1] + lista_ordenada[tam // 2])/2
    else:
        mediana = (lista_ordenada[tam // 2])
        
    media = sum(lista) / tam
    
    menor_distancia = max(lista)
    prox_media = lista[0]
    index = 0
    
    for i in range(tam):
        distancia = abs(media - lista[i])
        if distancia < menor_distancia:    
            menor_distancia = distancia
            prox_media = lista[i]
            index = i
            
    return [mediana, prox_media, index]
    