#Donada -> Còdigo de Huffman
import numpy
import math
lista = []
linha = []
matriz = []
lista_h = []
soma_valida = 0

# insere o número de mensagens e valida apenas se for inteiro
m = float(input('Informe o número de mensagens (valor inteiro): '))
if m // 1 == m:
    m = int(m)
while type(m) != int:
    m = float(input('O número de mensagens precisa ser inteiro: '))
    if m // 1 == m:
        m = int(m)
        break

#coloca os valores das mensagens em uma lista
while True:
    for c in range(0,m):
        valor_mensagem = float(input(f'Informe as probabilidades das {m} mensagens (uma de cada vez): '))
        soma_valida += valor_mensagem
        lista.append(valor_mensagem)
        lista.sort()
    # verifica se a soma das probabilidades das mensagens não é maior que 1
    if soma_valida > 1:
        lista.clear()
        soma_valida = 0
        print('Os valores inseridos ultrapassaram o limite de 1 (100%), redigite-os: ')
    else:
        break

#adiciona os valores e as mensagens na matriz
for p in range(0,m):
    linha.append(lista[p])
    linha.append(f'm{m - 1 - p}')
    matriz.append(linha[:])
    linha.clear()

# codigo O
cod_o = 0
for o in range(0, m):
    cod_o += (matriz[o][0]) * math.log2(1/matriz[o][0])
bits_o = len(bin(m -1).lstrip('0b'))

#mostra tabela
print('[PROBABILIDADE],[MENSAGEM]'.center(100, '-'))
print(f'{numpy.matrix(matriz)}')
print("-" * 100)
print(f'{matriz}'.center(100))

# Soma os menores valores da lista
for z in range(0, m - 1):
    x = matriz[0][0] + matriz[1][0]
    msg = '(' + matriz[0][1] + '|' + matriz[1][1] + ')'
    linha.append(x)
    linha.append(msg)
    matriz.append(linha[:])
    matriz.sort(key=lambda x: x[0])
    linha.clear()
    lista_h.append(msg)

    # print na forma de arvore
    print(f'___|___'.center(100))
    print(f'{matriz[0][1]}   {matriz[1][1]}\n'.center(100))
    matriz.pop(0)
    matriz.pop(0)
    print(f'{matriz}'.center(100))


# codigo H
print('Número de bits do Código Hoffman:')
cod_h = 0
for h in range(0, m):
    niveis = 0
    var = 'm' + str(h)
    for a in lista_h:
        if var in a:
            niveis += 1
    print(f'{var} | {niveis}')
    lista.sort(reverse=True)
    cod_h += lista[h] * niveis

print(f'\nPara o código H temos: {cod_h} bits/msg')
print(f'Para o código O temos: {cod_o} bits/msg')

#cálculo do melhor método para ser utilizado
n_o = cod_o / bits_o
n_h = cod_o / cod_h
print(f'O valor de no = {n_o}\nO valor de nh = {n_h}')
if cod_h > cod_o:
    print(f'O código Huffman é mais recomendado: {cod_h} bits/msg')
elif cod_o > cod_h:
    print(f'O código O é o mais recomendado: {cod_o} bits/msg')
else:
    print('Ambos os métodos são iguais')
