from .json import JSON

class Album:
    def __init__(self) -> None:
        self.id = None
        self.titulo = None
        self.ano = None
        self.gravadora = None
        self.duracao = None
        self.musicas = []
        
        # Carrega dados ao ser construido o objeto
        self.dados = JSON.carregar()
        
    def adicionar(self, artista_id):
        """
        Metodo para adicionar albuns de um determinado artista
            :param artista_id: ID do artista
        """
        for artista_dados in self.dados['artista']:
            # artista_id == artista_dados['_id] 
            # retorna os dados do dic 'artista_dados'
            if artista_id == artista_dados['_id']:
                # atribui o tamanho do dicionario 
                # ao atributo self.id + 1 como ID novo
                self.id = str(len(artista_dados['albuns']) + 1)

                # Gera um dicionário novo
                novo = {
                    "_id": self.id,
                    "titulo": self.titulo,
                    "ano": self.ano,
                    "gravadora": self.gravadora,
                    "duracao": self.duracao,
                    "musicas": []
                }

                # acrescenta o dic 'novo' em artista_dados['albuns']
                artista_dados['albuns'].append(novo)
                
        #Salva o dic em JSON
        JSON.salvar(self.dados)


    def listar(self, artista_id):
        """
        Metodo para listar albuns de um determinado artista
            :param artista_id: ID do artista
            :return: lista de albuns
        """
        lista = []
        for artista_dados in self.dados['artista']:
            if artista_dados['_id'] == artista_id:
                for album_dados in artista_dados['albuns']:
                    album = Album()
                    album.id = album_dados['_id']
                    album.titulo = album_dados['titulo']
                    album.ano = album_dados['ano']
                    album.gravadora = album_dados['gravadora']
                    album.duracao = album_dados['duracao']

                    lista.append(album)

                return lista
        
        return None

    def buscar_por_id(self, artista_id, album_id):
        """
        Metodo para listar um album especifico de um determinado artista
            :param artista_id: ID do artista
            :param album_id: ID do album
            :return: album (objeto)
        """
        for artista_dados in self.dados['artista']:
            if artista_dados['_id'] == artista_id:
                for albuns in artista_dados['albuns']:
                    if albuns['_id'] == album_id:
                        album = Album()
                        album.titulo = albuns['titulo']
                        album.ano =  albuns['ano']
                        album.gravadora =  albuns['gravadora']
                        album.duracao =  albuns['duracao']

                        return album
                
        return None
                
    @classmethod
    def tamanho(cls, artista_id):
        dados = JSON.carregar()
        for artista_dados in dados['artista']:
            if artista_dados['_id'] == artista_id:
                return len(artista_dados['albuns'])
