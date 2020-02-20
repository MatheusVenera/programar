import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Truco"


class Sorteador():

    def __init__(self):
        self.naipes = ["ouros","espadas","copas","paus"]
        self.numeros = ["quatro","cinco","seis","sete","dez","onze","doze","um","dois","tres"]
        self.mao_minha = ["a"]
        self.mao_computador = ["a"]
        self.carta = None
        self.manilha = None
        self.valor_dos_naipes = [('ouros', 1), ('espadas', 2), ('copas', 3), ('paus', 4)]
        self.valor_dos_naipes = dict(self.valor_dos_naipes)
        self.valor_das_cartas = [('quatro', 1), ('cinco', 2), ('seis', 3), ('sete', 4), ('dez', 5), ('onze', 6), ('doze', 7), ('um', 8), ('dois', 9), ('tres', 10)]
        self.valor_das_cartas = dict(self.valor_das_cartas)
        self.valor_das_cartas_reverso = [(1, 'quatro'), (2, 'cinco'), (3, 'seis'), (4, 'sete'), (5, 'dez'), (6, 'onze'), (7, 'doze'), (8, 'um'), (9, 'dois'), (10, 'tres')]
        self.valor_das_cartas_reverso = dict(self.valor_das_cartas_reverso)

    def sortear(self):
        self.mao_minha = []
        self.mao_computador = []
        self.carta = None
        self.manilha = None
        if sum((len(self.mao_minha),len(self.mao_computador))) == 0:
            while len(self.mao_minha) != 3:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_minha) and not(self.carta in self.mao_computador):
                    self.mao_minha.append(self.carta)
            while len(self.mao_computador) != 3:
                self.carta = random.choice(self.numeros) + " de " + random.choice(self.naipes)
                self.carta = str(self.carta)
                if not(self.carta in self.mao_computador) and not(self.carta in self.mao_minha):
                    self.mao_computador.append(self.carta)
        while True:
            self.manilha = random.choice(self.numeros) + " de " + random.choice(self.naipes)
            self.manilha = str(self.manilha)
            if not(self.manilha in self.mao_computador) and not(self.manilha in self.mao_minha):
                self.manilha = self.manilha.split(" ")
                self.manilha = self.manilha[0]
                self.manilha = self.valor_das_cartas[self.manilha]
                if self.manilha == 10:
                    self.manilha = 1
                    break
                elif self.manilha < 10:
                    self.manilha += 1
                    break
        self.manilha = self.valor_das_cartas_reverso[self.manilha]
        self.sorteou = False


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.sorteou = False
        self.sortear = Sorteador()
        self.valor_dos_naipes = [('ouros', 1), ('espadas', 2), ('copas', 3), ('paus', 4)]
        self.valor_dos_naipes = dict(self.valor_dos_naipes)
        self.valor_das_cartas = [('quatro', 1), ('cinco', 2), ('seis', 3), ('sete', 4), ('dez', 5), ('onze', 6), ('doze', 7), ('um', 8), ('dois', 9), ('tres', 10)]
        self.valor_das_cartas = dict(self.valor_das_cartas)
        self.minha_carta = None
        self.carta_computador = None
        self.ganhador = None
        self.ganhador_primeira_rodada = None
        self.ganhador_segunda_rodada = None
        self.ganhador_terceira_rodada = None
        self.pontos_jogador = 0
        self.pontos_computador = 0
        
    def on_draw(self):
        arcade.start_render()
        posicao_x = 100
        for i in range(3):
            arcade.draw_text(self.sortear.mao_minha[i], posicao_x, 100, arcade.color.WHITE)
            arcade.draw_text(self.sortear.mao_computador[i], posicao_x, 500, arcade.color.RED)
            arcade.draw_text(self.sortear.manilha, 50, 250, arcade.color.WHITE)
            posicao_x += 250

    def on_update(self, delta_time):
        if self.sorteou == False:
            self.sortear.sortear()
            self.sorteou = True
        print("O ganhador da primeira rodada é o : ", self.ganhador_primeira_rodada)
        print("O ganhador da segunda rodada é o : ", self.ganhador_segunda_rodada)
        print("O ganhador da terceira rodada é o : ", self.ganhador_terceira_rodada)
        print("A pontuação do jogador é: ", self.pontos_jogador)
        print("A pontuação do computador é: ", self.pontos_computador)
        print(self.ganhador)

    def verificar_ganhador(self):
        self.ganhador_primeira_rodada = None
        self.ganhador_segunda_rodada = None
        self.ganhador_terceira_rodada = None
        self.ganhador = None
        self.pontos_jogador = 0
        self.pontos_computador = 0
        for i in range(len(self.sortear.mao_minha)):
            if self.pontos_computador == 2:
                self.ganhador = "computador"
            elif self.pontos_jogador == 2:
                self.ganhador = "jogador"

            if self.ganhador == None:
                self.minha_carta = self.sortear.mao_minha[i]
                self.carta_computador = self.sortear.mao_computador[i]

                self.minha_carta = self.minha_carta.split(" ")
                self.minha_carta = self.minha_carta[0]

                self.carta_computador = self.carta_computador.split(" ")
                self.carta_computador = self.carta_computador[0]

                if self.sortear.manilha == self.minha_carta:
                    self.minha_escolha = 11
                if self.sortear.manilha == self.carta_computador:
                    self.escolha_computador = 11
                if self.sortear.manilha != self.minha_carta and self.sortear.manilha != self.carta_computador:
                    self.minha_escolha = self.valor_das_cartas[self.minha_carta]
                    self.escolha_computador = self.valor_das_cartas[self.carta_computador]

                if self.minha_escolha > self.escolha_computador:
                    self.minha_carta = self.sortear.mao_minha[i]
                    self.carta_computador = self.sortear.mao_computador[i]
                    print("Sua carta é maior: ", self.minha_carta)
                    if self.ganhador_primeira_rodada == "empachado":
                        if i == 1:
                            self.ganhador_segunda_rodada = "jogador"
                            self.pontos_jogador += 1
                        elif i == 2:
                            self.ganhador_terceira_rodada = "jogador"
                            self.pontos_jogador += 1
                        self.ganhador = "jogador"
                    elif self.ganhador_primeira_rodada != "empachado":
                        if i == 0:
                            self.ganhador_primeira_rodada = "jogador"
                        elif i == 1:
                            self.ganhador_segunda_rodada = "jogador"
                        elif i == 2:
                            self.ganhador_terceira_rodada = "jogador"
                        self.pontos_jogador += 1
                elif self.escolha_computador > self.minha_escolha:
                    print("A carta do computador é maior: ", self.carta_computador)
                    if self.ganhador_primeira_rodada == "empachado":
                        if i == 1:
                            self.ganhador_segunda_rodada = "computador"
                            self.pontos_computador += 1
                        elif i == 2:
                            self.ganhador_terceira_rodada = "computador"
                            self.pontos_computador += 1
                        self.ganhador = "computador"
                    elif self.ganhador_primeira_rodada != "empachado":
                        if i == 0:
                            self.ganhador_primeira_rodada = "computador"
                        elif i == 1:
                            self.ganhador_segunda_rodada = "computador"
                        elif i == 2:
                            self.ganhador_terceira_rodada = "computador"
                        self.pontos_computador += 1
                elif self.minha_escolha == self.escolha_computador:
                    if (self.minha_escolha == 11 and self.escolha_computador == 11) or (self.ganhador_primeira_rodada == "empachado" and self.ganhador_segunda_rodada == "empachado"):
                        self.minha_carta = self.sortear.mao_minha[i]
                        self.carta_computador = self.sortear.mao_computador[i]

                        self.minha_carta = self.minha_carta.split(" ")
                        self.minha_carta = self.minha_carta[2]

                        self.carta_computador = self.carta_computador.split(" ")
                        self.carta_computador = self.carta_computador[2]

                        self.minha_escolha = self.valor_dos_naipes[self.minha_carta]
                        self.escolha_computador = self.valor_dos_naipes[self.carta_computador]

                        if self.minha_escolha > self.escolha_computador:
                            self.minha_carta = self.sortear.mao_minha[i]
                            self.carta_computador = self.sortear.mao_computador[i]
                            print("Sua carta é maior: ", self.minha_carta)
                            if self.ganhador_primeira_rodada == "empachado":
                                self.ganhador = "jogador"
                            elif self.ganhador_primeira_rodada != "empachado":
                                if i == 0:
                                    self.ganhador_primeira_rodada = "jogador"
                                elif i == 1:
                                    self.ganhador_segunda_rodada = "jogador"
                                elif i == 2:
                                    self.ganhador_terceira_rodada = "jogador"
                                self.pontos_jogador += 1
                        elif self.escolha_computador > self.minha_escolha:
                            print("A carta do computador é maior: ", self.carta_computador)
                            if self.ganhador_primeira_rodada == "empachado":
                                self.ganhador = "computador"
                            elif self.ganhador_primeira_rodada != "empachado":
                                self.pontos_computador += 1
                                if i == 0:
                                    self.ganhador_primeira_rodada = "computador"
                                elif i == 1:
                                    self.ganhador_segunda_rodada = "computador"
                                elif i == 2:
                                    self.ganhador_terceira_rodada = "computador"
                    elif self.minha_escolha != 11 and self.escolha_computador != 11:
                        if i == 0:
                            print("Empachou!")
                            self.ganhador_primeira_rodada = "empachado"
                        elif i == 1:
                            print("Empachou!")
                            self.ganhador_segunda_rodada = "empachado"
                        elif i == 2:
                            print("Empachou!")
                            self.ganhador_terceira_rodada = "empachado"
                            if self.ganhador_primeira_rodada == "jogador":
                                self.ganhador = "jogador"
                            elif self.ganhador_primeira_rodada == "computador":
                                self.ganhador = "computador"

            if self.pontos_computador == 2:
                self.ganhador = "computador"
            elif self.pontos_jogador == 2:
                self.ganhador = "jogador"
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.sortear.sortear()
        if key == arcade.key.BACKSPACE:
            MyGame.verificar_ganhador(self)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
