from classes import Musica

class MusicaBLL():
    def __init__(self, titulo = None, duracao = None):
        self.titulo = titulo
        self.duracao = duracao

    def adicionar(self, artista_id, album_id):
        musica = Musica()
        musica.titulo = self.titulo
        musica.duracao = self.duracao

        musica.adicionar(artista_id, album_id)

    def listar(self, artista_id, album_id):
        musica = Musica()

        # Tenta exibir a lista
        try:
            musicas = musica.listar(artista_id, album_id)
            if musicas is None:
                return 0
            
            # Iterador de Lista carregada
            for musica_dados in musicas:
                print(f'{musica_dados.id}. {musica_dados.titulo} ({musica_dados.duracao})')
            
            return Musica.tamanho(artista_id, album_id)
        except KeyError:
            return 0
        
    def listar_por_id(self, artista_id, album_id, musica_id):
        musica = Musica()
        return musica.listar_por_id(artista_id, album_id, musica_id)
        # No futuro