from BLL import AlbumBLL
from classes import Utils

class AlbumView():
    def __init__(self, artista_id = None, titulo = None, ano = None, gravadora = None, duracao = None):
        self.artista_id = artista_id
        self.titulo = titulo
        self.ano = ano
        self.gravadora = gravadora
        self.duracao = duracao

    def inserir(self):
        album = AlbumBLL(self.titulo, self.ano, self.gravadora, self.duracao)
        album.adicionar(self.artista_id)

    def mostrar(self, artista_id):
        album = AlbumBLL()
        print("-------------------------------------------")
        if album.listar(artista_id) == 0:
            return False
        print("-------------------------------------------")
        return True

    def mostrar_por_id(self, artista_id, album_id):
        album = AlbumBLL()
        Utils.limpa_tela()

        album_dados = album.listar_por_id(artista_id, album_id)
        if album_dados is None:
            return False
        
        print(f"Músicas de {album_dados.titulo} ({album_dados.ano})")
        return True