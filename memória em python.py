
V = [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

while True:
    I = input('Digite W para escrever, R para Ler, L para listar toda memoria e qualquer tecla para parar:')
    if I == 'W':
        b = input('Digite um endereco de 4 bits:')
        d = int(b,2)
        V.pop(d)
        a = int(input('Digite o dado de 8 bits:'))
        l = list(str(a))
        while len(l)<8:
            l.insert(0,0)
        V.insert(d,l)
    elif I == 'R':
        b = input('Digite um endereco de 4 bits:')
        d = int(b,2)
        print(*V[d], sep='')
    elif I == 'L':
        for i in range(len(V)):
            print(*V[i], sep='')
    else:
        break
