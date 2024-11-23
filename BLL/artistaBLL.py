from classes import Artista

class ArtistaBLL():
    def __init__(self, nome= None):
        self.nome = nome

    def adicionar(self):
        artista = Artista()
        artista.nome = self.nome

        artista.adicionar()

    def listar(self):
        artista = Artista()
        
        # Tenta exibir a lista
        try:
            artistas = artista.listar()
            if artistas is None:
                return 0
            
            # Iterador de Lista carregada
            for artista in artistas:
                print(f'{artista.id}. {artista.nome}')

            return Artista.tamanho()
        except KeyError:
            return 0
        
    def listar_por_id(self, artista_id):
        artista = Artista()
        return artista.buscar_por_id(artista_id)