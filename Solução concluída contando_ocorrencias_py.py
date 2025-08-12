def contando_ocorrencias(lista, valor):
    contador = 0
    
    for elemento in lista:
        if elemento == valor:
            contador += 1
    
    return contador

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado1 = contando_ocorrencias(numeros, 2)
print(f"O número 2 aparece {resultado1} vezes na lista")

resultado2 = contando_ocorrencias(numeros, 13)
print(f"O número 13 aparece {resultado2} vezes na lista")

resultado3 = contando_ocorrencias(numeros, 9)
print(f"O número 9 aparece {resultado3} vezes na lista")