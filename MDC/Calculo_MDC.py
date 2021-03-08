import numpy
lista = []
listaResultado = []
divisor = 2
while True:
    quant = int(input("Digite a quantidade de numeros que deseja saber o MDC:\n"))
    if quant > 1:
        break
    elif quant == 0:
        print("Obrigado por utilizar nosso programa!!")
        break
    elif quant == 1 or quant < 1:
        print("\033[31mQuantidade inválida!! Digite um número maior que 1 ou 0 para sair:\033[m\n")
for i in range(quant):
    while True:
        try:
            num = int(input(f'Digite o {i + 1}º numero:\n'))
            if num <= 0:
                while True:
                    print('\033[31mERRO! Digite um numero inteiro maior que 0!!\033[m')
                    print(' ')
                    num = int(input(f'Digite o {i + 1}º numero:\n'))
                    if num > 0:
                        lista.append(num)
                        break
            lista.append(num)
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro válido!!\033[m')
            continue
lista.sort()
while True:
    if sum(lista) == len(lista):
        break
    else:
        soma = 0
        VerificaMDC = 0
        for i in range(len(lista)):
            if lista[i] % divisor == 0 and lista[i] > 1:
                lista[i] = lista[i] // divisor
                VerificaMDC += 1
        lista.sort()
        for x in range(len(lista)):
            if lista[x] != 1 and lista[x] % divisor == 0:
                soma += 1
        if VerificaMDC == quant:
            listaResultado.append(divisor)
        if soma == 0:
            divisor += 1
if quant > 1:
    print(f'O MDC dos numeros informados é: {numpy.prod(listaResultado)}')
