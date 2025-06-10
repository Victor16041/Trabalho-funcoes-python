def soma_pares(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma

numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = soma_pares(numeros)
print("O resultado é: ", resultado)
