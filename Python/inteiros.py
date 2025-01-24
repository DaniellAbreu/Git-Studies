inteiros = list(map(int, input().split()))

if len(inteiros) < 2:
    print(f"{inteiros.pop():.2f}")

else:
    res = []

    inteiros[0] = 2 * inteiros[0]
    inteiros[1] = 0.5 * inteiros[1]

    res.append(inteiros[0] + inteiros[1])

    for i in range(len(inteiros) - 2):
        soma = res[i] * 2 + inteiros[i + 2] * 0.5
        res.append(soma)
    
    print(f"{res[-1]:.2f}")