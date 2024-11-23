from classes import Album

class AlbumBLL:
    def __init__(self, titulo = None, ano = None, gravadora = None, duracao = None):
        self.titulo = titulo
        self.ano = ano
        self.gravadora = gravadora
        self.duracao = duracao

    def adicionar(self, artista_id):
        album = Album()
        album.titulo = self.titulo
        album.ano = self.ano
        album.gravadora = self.gravadora
        album.duracao = self.duracao

        album.adicionar(artista_id)

    def listar(self, artista_id):
        album = Album()

        # Tenta exibir a lista
        try:
            albuns = album.listar(artista_id)
            if albuns is None:
                return 0
            
            # Iterador de Lista carregada
            for album_dados in albuns:
                print(f'{album_dados.id}. {album_dados.titulo} ({album_dados.ano})')
            
            return Album.tamanho(artista_id)
        except KeyError:
            return 0
        
    def listar_por_id(self, artista_id, album_id):
        album = Album()
        return album.buscar_por_id(artista_id, album_id)