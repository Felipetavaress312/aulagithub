def encontrando_os_numeros_impares(lista):
    numeros_impares = []
    
    for numero in lista:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    
    return numeros_impares

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = encontrando_os_numeros_impares(numeros)
print(f"Os números ímpares da lista são: {resultado}")