from .json import JSON

class Artista:
    def __init__(self) -> None:
        self.id = None
        self.nome = None
        self.albuns = []

        # Carrega dados ao ser construido o objeto
        self.dados = JSON.carregar()

    def adicionar(self):
        """
        Metodo para adicionar um determinado artista
        """
        # atribui o tamanho do dicionario 
        # ao atributo self.id + 1 como ID novo
        self.id = str(len(self.dados['artista']) + 1)

        # Gera um dicionário novo
        novo = {
            "_id": self.id,
            "nome": self.nome,
            "albuns": [],
        }

        # acrescenta o dic 'novo' em self.dados['artista']
        self.dados['artista'].append(novo)

        #Salva o dic em JSON
        JSON.salvar(self.dados)

    def listar(self):
        """
        Metodo para listar artistas

        :return: lista de artistas
        """
        lista = []
        for artista_dados in self.dados['artista']:
            artista = Artista()
            artista.id = artista_dados['_id']
            artista.nome = artista_dados['nome']

            lista.append(artista)

        return lista
            
    def buscar_por_id(self, artista_id):
        """
        Metodo para listar um determinado artista
            :param artista_id: ID do artista
            :return: artista (objeto)
        """
        for artista_dados in self.dados['artista']:
            if artista_dados['_id'] == artista_id:
                artista = Artista()
                artista.nome = artista_dados['nome']

                return artista

        return None

    @classmethod 
    def tamanho(cls):
        dados = JSON.carregar()
        return len(dados['artista'])
    
    