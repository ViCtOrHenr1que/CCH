class Soldado:
    def __init__(self, cor_uniforme, arma):  # Estado intrínseco
        self.cor_uniforme = cor_uniforme
        self.arma = arma

    def renderizar(self, posicao):  # Estado extrínseco
        print(f"Soldado com uniforme {self.cor_uniforme}, armado com {self.arma}, na posição {posicao}.")


class FabricaDeSoldados:
    soldados = {}

    @classmethod
    def obter_soldado(cls, cor_uniforme, arma):
        chave = (cor_uniforme, arma)
        if chave not in cls.soldados:
            cls.soldados[chave] = Soldado(cor_uniforme, arma)
        return cls.soldados[chave]

fabrica = FabricaDeSoldados()

soldado1 = fabrica.obter_soldado("Verde", "Rifle")
soldado2 = fabrica.obter_soldado("Verde", "Rifle")
soldado3 = fabrica.obter_soldado("Azul", "Sniper")

soldado1.renderizar((5, 10))
soldado2.renderizar((156, 235))
soldado3.renderizar((0, 40))