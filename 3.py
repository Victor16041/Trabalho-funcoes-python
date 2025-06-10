def media_notas(notas):
    soma = 0
    for num in notas:
        soma += num
    media = soma / len(notas)
    return media

notasfin = [60, 82, 78, 90, 30]

print("Média das notas: ", media_notas(notasfin))