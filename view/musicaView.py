from BLL import MusicaBLL
from classes import Utils

class MusicaView():
    def __init__(self, artista_id = None, album_id = None, titulo = None, duracao = None):
        self.artista_id = artista_id
        self.album_id = album_id
        self.titulo = titulo
        self.duracao = duracao

    def inserir(self):
        musica = MusicaBLL(self.titulo, self.duracao)
        musica.adicionar(self.artista_id, self.album_id)

    def mostrar(self, artista_id, album_id):
        musica = MusicaBLL()
        print("-------------------------------------------")
        if musica.listar(artista_id, album_id) == 0:
            return False
        print("-------------------------------------------")
        input()
        return True

    def mostrar_por_id(self, artista_id, album_id, musica_id):
        musica = MusicaBLL()
        Utils.limpa_tela()

        musica_dados = musica.listar_por_id(artista_id, album_id, musica_id)
        if musica_dados is None:
            return False
        
        # No futuro
        print(f"Tocando {musica_dados.titulo}")
        print(f"Duração {musica_dados.duracao}")
        input()
        Utils.mensagem("No Futuro")
        return True