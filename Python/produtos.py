N, M, K = map(int, input().split())

quantidade_produtos = list(map(int, input().split()))

valor_produtos = [list(map(int, input().split())) for _ in range(N)]

def comprar_produtos(M, K, valor_produtos):
    for _ in range(K):
        for mercearia in valor_produtos:
            if not mercearia:
                return "Nao"
            
            menor_preco = min(mercearia)
            M -= menor_preco    
            
            if M < 0:
                return "Nao"
        
            mercearia.remove(menor_preco)
            
    return "Sim"    

print(comprar_produtos(M, K, valor_produtos))
