def removendo_duplicatas(lista):
    lista_unica = []
    
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    
    return lista_unica

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado = removendo_duplicatas(numeros)
print(f"Lista original: {numeros}")
print(f"Lista sem duplicatas: {resultado}")
print(f"Tamanho original: {len(numeros)}, Tamanho sem duplicatas: {len(resultado)}")