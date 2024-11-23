import os

class Utils:
    @staticmethod
    def limpa_tela():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def mensagem(msg):
        Utils.limpa_tela()
        input(msg)