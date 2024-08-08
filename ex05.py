
cores = ['azul', 'vermelho', 'roxo', 'amarelo', 'verde', 'rosa', 'lilas', 'cinza', 'marrom']

while True:
    cor = str(input('Escolha uma cor:' ))
    if cor in cores:
        print("esta cor esta disponivel")
        break
    else: 
        print("esta cor não esta disponivel")
    
