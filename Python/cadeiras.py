m, n = map(int, input().split())
fileiras = [list(map(int, input().split())) for _ in range(m)]

maior_distancia = -1

ocupadas = [[] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if fileiras[i][j] == 1:
            ocupadas[i].append(j)

for posicao, fileira in enumerate(fileiras):
    for i in range(len(fileira)):
        if fileira[i] == 0:
            menor_distancia = float('inf')
            for cadeira in ocupadas[posicao]:
                distancia = abs(i - cadeira)
                if distancia < menor_distancia:
                    menor_distancia = distancia
            if menor_distancia > maior_distancia:
                maior_distancia = menor_distancia

print(maior_distancia)