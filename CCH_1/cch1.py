class Carro:
    def __init__(self):
        self.motor = None
        self.rodas = None
        self.cor = None

    def __str__(self):
        return f"Carro(motor={self.motor}, rodas={self.rodas}, cor={self.cor})"

class ConstrutorCarro:
    def __init__(self):
        self.resetar()

    def resetar(self):
        self.carro = Carro()

    def definir_motor(self, motor):
        self.carro.motor = motor
        return self

    def definir_rodas(self, rodas):
        self.carro.rodas = rodas
        return self

    def definir_cor(self, cor):
        self.carro.cor = cor
        return self

    def construir(self):
        carro_finalizado = self.carro
        self.resetar()
        return carro_finalizado


class DiretorCarro:
    def __init__(self, construtor):
        self.construtor = construtor

    def construir_carro_esportivo(self):
        return self.construtor.definir_motor("V8").definir_rodas(4).definir_cor("Vermelho").construir()

    def construir_carro_economico(self):
        return self.construtor.definir_motor("V2").definir_rodas(4).definir_cor("Azul").construir()


construtor = ConstrutorCarro()
diretor = DiretorCarro(construtor)

carro_esportivo = diretor.construir_carro_esportivo()
carro_economico = diretor.construir_carro_economico()

print(carro_esportivo)
print(carro_economico)
