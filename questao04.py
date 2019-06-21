class Carro(object):
    def __init__(self, kmL):
        self.kmL = kmL
        self.combustivel = 0

    def adicionarGasolina(self, acrecimoDecombustivel):
        self.combustivel = self.combustivel + acrecimoDecombustivel

    def andar(self, km):

        if (km / self.kmL) <= self.combustivel:
            self.combustivel = self.combustivel - (km / self.kmL)
            print('Otimo, chegamos ao nosso destino!')
        else:
            kmFinal = self.kmL * self.combustivel
            self.combustivel = 0

            print('Vish! Acabou a gasolina, você andou {}km e lhe resta {:.3f}km'.format(kmFinal, km - kmFinal))

    def obterGasolina(self):
        print('Seu tanque ainda tem {:.3f}L de Gasolina'.format(self.combustivel))
