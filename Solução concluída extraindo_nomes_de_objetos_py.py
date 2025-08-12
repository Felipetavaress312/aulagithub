def extraindo_nomes_de_objetos(lista_objetos):
    nomes = []
    
    for objeto in lista_objetos:
        if hasattr(objeto, 'nome'):
            nomes.append(objeto.nome)
    
    return nomes

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoas = [
    Pessoa("João"),
    Pessoa("Maria"),
    Pessoa("Pedro"),
    Pessoa("Ana"),
    Pessoa("Carlos")
]

resultado = extraindo_nomes_de_objetos(pessoas)
print(f"Os nomes extraídos são: {resultado}")