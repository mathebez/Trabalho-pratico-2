def comparar(numero):
    if (numero%10) <= 5:
        numero = numero+4
        return numero
    else:
        numero = numero-6
        return numero

num = int(input('Digite um número inteiro de 4 digitos para ciptografar: '))


u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

u = (u+6)%10
d = (d+6)%10
c = (c+6)%10
m = (m+6)%10

print('O numero criptografado é: {}{}{}{}'.format(d, u, m, c))

num2 = int(input('Digite um numero inteiro de 4 digitos para descriptografar: '))

u2 = num2 // 1 % 10
d2 = num2 // 10 % 10
c2 = num2 // 100 % 10
m2 = num2 // 1000 % 10

u2 = comparar(u2)
d2 = comparar(d2)
c2 = comparar(c2)
m2 = comparar(m2)

print('O numero descriptografado é: {}{}{}{}'.format(d2, u2, m2, c2))