def encontrando_o_maior_numero(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    
    return maior

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = encontrando_o_maior_numero(numeros)
print(f"O maior número da lista é: {resultado}")