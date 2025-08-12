def buscando_um_numero(numero, lista):
    for elemento in lista:
        if elemento == numero:
            return True
    
    return False

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

resultado1 = buscando_um_numero(42, numeros)
print(f"O número 42 está na lista: {resultado1}")

resultado2 = buscando_um_numero(100, numeros)
print(f"O número 100 está na lista: {resultado2}")