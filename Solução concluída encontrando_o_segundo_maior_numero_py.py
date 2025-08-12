def encontrando_o_segundo_maior_numero(lista):
    if len(lista) < 2:
        return None
    
    numeros_unicos = list(set(lista))
    
    if len(numeros_unicos) < 2:
        return None
    
    numeros_unicos.sort(reverse=True)
    return numeros_unicos[1]

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = encontrando_o_segundo_maior_numero(numeros)
print(f"O segundo maior número da lista é: {resultado}")