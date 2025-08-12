def verificando_se_a_lista_esta_vazia(lista):
    return len(lista) == 0

lista_vazia = []
lista_com_elementos = [1, 2, 3, 4, 5]

resultado1 = verificando_se_a_lista_esta_vazia(lista_vazia)
print(f"A lista vazia está vazia: {resultado1}")

resultado2 = verificando_se_a_lista_esta_vazia(lista_com_elementos)
print(f"A lista com elementos está vazia: {resultado2}")

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]
resultado3 = verificando_se_a_lista_esta_vazia(numeros)
print(f"A lista de números está vazia: {resultado3}")