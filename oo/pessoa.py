class Pessoa:
    olhos = '2'
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):   # método de instância cria atributo
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():   # método estático não cria atributo, funciona como função atrelada a classe,
        # independe do objeto.
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):   # classe palavra reservada
        return f'{cls} - olhos {cls.olhos}'




if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    # print(renzo.sobrenome)   # AttributeError: 'Pessoa' object has no attribute 'sobrenome'
    print(luciano.__dict__)
    print(renzo.__dict__)
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 2
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico(), renzo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe(), renzo.nome_e_atributos_de_classe())
