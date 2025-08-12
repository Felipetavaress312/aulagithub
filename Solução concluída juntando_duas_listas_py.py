def juntando_duas_listas(lista1, lista2):
    lista_concatenada = []
    
    for elemento in lista1:
        lista_concatenada.append(elemento)
    
    for elemento in lista2:
        lista_concatenada.append(elemento)
    
    return lista_concatenada

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

resultado = juntando_duas_listas(natureza, tecnologia)
print(f"Lista natureza: {natureza}")
print(f"Lista tecnologia: {tecnologia}")
print(f"Lista concatenada: {resultado}")
print(f"Tamanho da lista concatenada: {len(resultado)}")