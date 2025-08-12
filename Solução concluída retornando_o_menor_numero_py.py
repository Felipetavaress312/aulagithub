def retornando_o_menor_numero(lista):
    if not lista:
        return None
    
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    
    return menor

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = retornando_o_menor_numero(numeros)
print(f"O menor número da lista é: {resultado}")