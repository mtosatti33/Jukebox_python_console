from classes import Utils

class MenuView():
    def __init__(self):
        pass

    @classmethod
    def mostrar(cls, mensagem = "Opção: "):
        Utils.limpa_tela()

        # Menu Principal
        print("Jukebox")
        print("-------------------------------------------")
        print("1. Listar")
        print("2. Adicionar")
        print("0. Sair")
        print("-------------------------------------------")

        try:
            return int(input(mensagem))
        except ValueError:
            input("Valor Inválido")
            return None

    @classmethod
    def cadastro(cls, mensagem = "Opção: "):
        Utils.limpa_tela()

        # Menu Secundário
        print("1. Artista")
        print("2. Albuns")
        print("3. Músicas")
        print("0. Voltar")
        
        try:
            return int(input(mensagem))
        except ValueError:
            input("Valor Inválido")
            return None

        