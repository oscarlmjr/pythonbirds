class Pessoa:
    olhos = '2'
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):   # método de instância cria atributo
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():   # método estático não cria atributo, funciona como função atrelada a classe,
        # independe do objeto.
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):   # classe palavra reservada
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        # cumprimentar_da_classe = Pessoa.cumprimentar(self)
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')
    for filho in luciano.filhos:
        print(filho.nome)
    print(renzo.__dict__)
    # Pessoa.olhos = 2
    print(Pessoa.olhos)
    # print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico(), renzo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe(), renzo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
