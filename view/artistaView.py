from BLL import ArtistaBLL
from classes import Utils

class ArtistaView():
    def __init__(self, nome = None):
        self.nome = nome

    def inserir(self):
        artista = ArtistaBLL(self.nome)
        artista.adicionar()

    def mostrar(self):
        artista = ArtistaBLL()
        Utils.limpa_tela()

        print("Artistas")
        print("-------------------------------------------")
        artista.listar()
        print("-------------------------------------------")

    def mostrar_por_id(self, artista_id):
        artista = ArtistaBLL()
        Utils.limpa_tela()
        
        artista_dados = artista.listar_por_id(artista_id)
        if artista_dados is None:
            return False
        
        print(f"Albuns de {artista_dados.nome}")
        return True