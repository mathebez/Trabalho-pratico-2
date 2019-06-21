def conversorMB(tamanhoEmBytes):
    tamanhoEmBytes = float(tamanhoEmBytes)
    return (float(tamanhoEmBytes / (1024 * 1024)))


def percentual(lista, total):
    percentual = (lista[3] / total) * 100
    lista.insert((len(cadaUsuario)), percentual)


def espacoOcupado(lista, total):
    media = 0
    elementos = len(lista)
    media = (total) / (elementos + 1)
    return media


usuarios = []
posicao = 1
total = media = 0
with open('usuarios.txt', 'r') as arquivo:
    valor = 0
    for linha in arquivo:
        usuarios.append(linha.split())

    for cadaUsuario in usuarios:
        cadaUsuario.insert(0, posicao)
        valor = conversorMB(float(cadaUsuario[2]))
        total += valor
        cadaUsuario.insert((len(cadaUsuario)), valor)
        posicao += 1

    for cadaUsuario in usuarios:
        percentual(cadaUsuario, total)

media = espacoOcupado(cadaUsuario, total)

with open('relatorio.txt', 'w') as arquivo:
    arquivo.write('ACME Inc.        Uso do espaço em disco pelos usuários.\n')
    arquivo.write('--------------------------------------------------------------\n')
    arquivo.write('Nr.\tUsuário        \tEspaço utilizado\t% do uso\n\n')

    for cadaUsuario in usuarios:
        percentagem = '{0:.2f}'.format(round(cadaUsuario[3], 2))
        arquivo.write(str(cadaUsuario[0]) + " {:<15}\t ".format(cadaUsuario[1])+"{}".format(percentagem) + ' MB\t\t\t' + "{0:.2f}".format(cadaUsuario[4]) + '%' + '\n')

    arquivo.write('\n\nEspaço Total Ocupado: ' + '{0:.2f}'.format(total) + ' MB')
    arquivo.write('\n\nEspaço médio Ocupado: ' + '{0:.2f}'.format(media) + ' MB')
    arquivo.close()

with open('relatorio.txt', 'r') as arquivo:
    print(arquivo.read())