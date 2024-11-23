from .json import JSON

class Musica:
    def __init__(self) -> None:
        self.id = None
        self.titulo = None
        self.duracao = None
        
        # Carrega dados ao ser construido o objeto
        self.dados = JSON.carregar()
    
    def adicionar(self, artista_id, album_id):
        """
        Metodo para adicionar albuns de um determinado artista
            :param artista_id: ID do artista
            :param album_id: ID do álbum
        """
        for artista_dados in self.dados['artista']:
            # artista_id == artista_dados['_id] 
            # retorna os dados do dic 'artista_dados'
            if artista_id == artista_dados['_id']:
                for album in artista_dados['albuns']:

                    # album_id == album['_id] 
                    # retorna os dados do dic 'album'
                    if album_id == album['_id']:
                        # atribui o tamanho do dicionario 
                        # ao atributo self.id + 1 como ID novo
                        self.id = str(len(album['musicas']) + 1)
                        
                        # Gera um dicionário novo
                        novo = {
                            "_id": self.id,
                            "titulo": self.titulo,
                            "duracao": self.duracao
                        }

                        # acrescenta o dic 'novo' em album['musicas']
                        album['musicas'].append(novo)
                        
        #Salva o dic em JSON
        JSON.salvar(self.dados)


    def listar(self, artista_id, album_id):
        """
        Metodo para listar músicas de um determinado album
            :param artista_id: ID do artista
            :param album_id: ID do album
            :return: lista de músicas
        """
        lista = []
        for artista_dados in self.dados['artista']:
            if artista_dados['_id'] == artista_id:
                for album in artista_dados['albuns']:
                    if album['_id'] == album_id:
                        for musica_dados in album['musicas']:
                            musica = Musica()
                            musica.id = musica_dados['_id']
                            musica.titulo = musica_dados['titulo']
                            musica.duracao = musica_dados['duracao']

                            lista.append(musica)

                        return lista
        return None
    def listar_por_id(self, artista_id, album_id, musica_id):
        pass
        # no Futuro
        
    @classmethod
    def tamanho(cls, artista_id, album_id):
        dados = JSON.carregar()
        for artista_dados in dados['artista']:
            if artista_dados['_id'] == artista_id:
                for album in artista_dados['albuns']:
                    if album['_id'] == album_id:
                        return len(album['musicas'])