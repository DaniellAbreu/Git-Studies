N = int(input())
count = ''

for i in range(N):
    string_codificada = input()
    
    for char in string_codificada:
        if char.isalpha() and count != '':
            resultado = letter * int(count)
            print(resultado, end='')
            letter = char
            count = ''
        
        elif char.isalpha():
            letter = char
            count = ''
        
        elif char.isdigit():
            count = count + char
            
    print(letter * int(count))
    count = ''
        