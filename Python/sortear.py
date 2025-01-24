n, t = int(input()), int(input())

lista_inteiros = [list(map(int, input().split())) for _ in range(n)]

# Define Critérios de Organização
def ordenar_inteiros(lista):
    return (lista[t], sum(lista)) #Segundo elemento da tupla para casos de empate
    
lista_inteiros.sort(key=ordenar_inteiros)

for linhas in lista_inteiros:
    print(*linhas)