n = int(input())

chamadas_fib = [[] for _ in range(n + 1)]

def fibonacci(n):
    chamadas_fib[n].append(0)
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibonacci(n - 2)) + (fibonacci(n - 1))

#Chamada da função para atualizar a lista e facilitar impressão
n_termo = fibonacci(n)

print(f"Termo: {n_termo}", "Quantidades:", sep="\n")

for i in range(n + 1):
    print(f"fibonacci({i}) - {len(chamadas_fib[i])}")

