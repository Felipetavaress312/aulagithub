def calculando_a_media(lista):
    if not lista:
        return None
    
    soma = 0
    for numero in lista:
        soma += numero
    
    media = soma / len(lista)
    return media

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = calculando_a_media(numeros)
print(f"A média dos valores da lista é: {resultado}")
print(f"Quantidade de elementos: {len(numeros)}")
print(f"Soma total: {sum(numeros)}")