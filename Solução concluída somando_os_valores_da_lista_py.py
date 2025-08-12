def somando_os_valores_da_lista(lista):
    soma = 0
    
    for numero in lista:
        soma += numero
    
    return soma

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = somando_os_valores_da_lista(numeros)
print(f"A soma dos valores da lista é: {resultado}")