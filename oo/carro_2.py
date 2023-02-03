
class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self, velocidade):
        return self.velocidade

    def calcular_direcao(self, valor):
        return self.valor

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1
        return Carro.calcular_velocidade(self, self.velocidade)

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            return 0
        return Carro.calcular_velocidade(self, self.velocidade)

class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
            return Carro.calcular_direcao(self, self.valor)
            # return Carro.calcular_direcao()
        elif self.valor == 'Leste':
            self.valor = 'Sul'
            return Carro.calcular_direcao(self, self.valor)
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
            return Carro.calcular_direcao(self, self.valor)
        elif self.valor == 'Oeste':
            self.valor = 'Norte'
            return Carro.calcular_direcao(self, self.valor)

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
            return Carro.calcular_direcao(self, self.valor)
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
            return Carro.calcular_direcao(self, self.valor)
        elif self.valor == 'Sul':
            self.valor = 'Leste'
            return Carro.calcular_direcao(self, self.valor)
        elif self.valor == 'Leste':
            self.valor = 'Norte'
            return Carro.calcular_direcao(self, self.valor)


motor = Motor()
print(motor.velocidade)
direcao = Direcao()
print(direcao.valor)
print()
carro = Carro(motor, direcao)
print(carro.motor.acelerar())
print(carro.motor.acelerar())
print(carro.motor.acelerar())
print(carro.motor.frear())
print(carro.motor.frear())
print()
print(carro.direcao.girar_a_direita())
print(carro.direcao.girar_a_direita())
print(carro.direcao.girar_a_direita())
print(carro.direcao.girar_a_direita())
print()
print(carro.direcao.girar_a_esquerda())
print(carro.direcao.girar_a_esquerda())
print(carro.direcao.girar_a_esquerda())
print(carro.direcao.girar_a_esquerda())
