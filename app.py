from view import *
from classes import Utils

# Loop Principal
def main():
    while True:
        opcao = MenuView.mostrar()
        if opcao is None:
            continue

        match opcao:
            # Listar ----------------------------------------------------------------------------
            case 1: 
                while True:
                    artista = ArtistaView()
                    artista.mostrar()
                    # variavel armazena o ID do artista
                    artista_id = input("Escolha o artista [pressione 0 para voltar]: ").strip()
                    if artista_id == '':
                        Utils.mensagem("Opção inválida")
                        continue # continua no laço

                    # Volta ao menu principal se o valor for zero '0'
                    if artista_id == '0':
                        break
                    
                    if not artista.mostrar_por_id(artista_id):
                        Utils.mensagem("Artista não encontrado")
                        continue

                    albuns = AlbumView()
                    if not albuns.mostrar(artista_id):
                        Utils.mensagem("Não há album(s) cadastrado(s)")
                        continue

                    # variavel armazena o ID do album
                    album_id = input("Escolha o album [pressione 0 para voltar]: ").strip()
                    if album_id == '':
                        Utils.mensagem("Opção inválida")
                        continue # continua no laço

                    # Volta ao menu principal se o valor for zero '0'
                    if album_id == '0':
                        break
                    
                    if not albuns.mostrar_por_id(artista_id, album_id):
                        Utils.mensagem("Álbum não encontrado")
                        continue

                    musicas = MusicaView()
                    if not musicas.mostrar(artista_id, album_id):
                        Utils.mensagem("Não há músicas(s) cadastrada(s)")
                        continue
            # Adicionar ----------------------------------------------------------------------------
            case 2: 
                while True:
                    opcao_cad = MenuView.cadastro()
                    if opcao_cad is None:
                        continue
                    
                    match opcao_cad:
                        # 1. Artista ----------------------------------------------------------------------------
                        case 1:
                            # Insere os Dados nos atributos
                            while True:
                                nome = input("Nome do Artista [pressione 0 para voltar]: ").strip()
                                if nome == '0':
                                    break
                                if nome == '':
                                    continue

                                # Adiciona
                                artista = ArtistaView(nome)
                                artista.inserir()
                        # 2. Album ----------------------------------------------------------------------------
                        case 2:
                            # Traz uma lista
                            artista = ArtistaView()
                            artista.mostrar()
                            # variavel armazena o ID do artista
                            artista_id = input("Escolha o artista [pressione 0 para voltar]: ").strip()

                            if artista_id == '':
                                Utils.mensagem("Opção inválida")
                                continue # continua no laço

                            # Volta ao menu principal se o valor for zero '0'
                            if artista_id == '0':
                                break
                                
                            if not artista.mostrar_por_id(artista_id):
                                Utils.mensagem("Artista não encontrado")
                                continue

                            # Insere os Dados nos atributos
                            while True:
                                titulo = input("Título [pressione 0 para voltar]: ").strip()
                                if titulo == 0:
                                    break
                                if titulo == '':
                                    continue

                                ano = input("Ano [pressione 0 para voltar]: ").strip()
                                if ano == 0:
                                    break
                                if ano == '':
                                    continue

                                gravadora = input("Gravadora [pressione 0 para voltar]: ").strip()
                                if gravadora == 0:
                                    break
                                if gravadora == '':
                                    continue

                                duracao = input("Duração [pressione 0 para voltar]: ").strip()
                                if duracao == 0:
                                    break
                                if duracao == '':
                                    continue
                            
                                # Adiciona
                                album = AlbumView(artista_id, titulo, ano, gravadora, duracao)
                                album.inserir()
                        # 3. Musica ----------------------------------------------------------------------------
                        case 3:
                            # Traz uma lista de artistas
                            artista = ArtistaView()
                            artista.mostrar()
                            # variavel armazena o ID do artista
                            artista_id = input("Escolha o artista [pressione 0 para voltar]: ").strip()
                            if artista_id == '':
                                Utils.mensagem("Opção inválida")
                                continue # continua no laço

                            # Volta ao menu principal se o valor for zero '0'
                            if artista_id == '0':
                                break
                                
                            if not artista.mostrar_por_id(artista_id):
                                Utils.mensagem("Artista não encontrado")
                                continue # continua no laço

                            # Traz uma lista de albuns
                            albuns = AlbumView()
                            albuns.mostrar(artista_id)
                            # variavel armazena o ID do album
                            album_id = input("Escolha o album [pressione 0 para voltar]: ").strip()  
                            if album_id == '':
                                Utils.mensagem("Opção inválida")
                                continue # continua no laço

                            # Volta ao menu principal se o valor for zero '0'
                            if album_id == '0':
                                break
                            
                            if not albuns.mostrar_por_id(artista_id, album_id):
                                Utils.mensagem("Álbum não encontrado")
                                continue # continua no laço

                            # Sai do laço quando o valor dos atributos for zero '0'
                            while True:
                                # Insere os Dados nos atributos
                                titulo = input("Título [pressione 0 para retornar]: ").strip()
                                if titulo == '':
                                    continue
                                if titulo == '0':
                                    break

                                duracao = input("Duração [pressione 0 para retornar]: ").strip()
                                if duracao == '':
                                    continue
                                if duracao == '0':
                                    break

                                # Adiciona
                                musica = MusicaView(artista_id, album_id, titulo, duracao)
                                musica.inserir()
                        # 0. Volta ao Menu Principal ----------------------------------------------------------------------------
                        case 0:
                            break
                        # Qualquer outra coisa ----------------------------------------------------------------------------
                        case _:
                            Utils.mensagem("Opção não encontrada")
            # Sai do Programa ----------------------------------------------------------------------------
            case 0: 
                break
            # Qualquer outra coisa ----------------------------------------------------------------------------
            case _: 
                input("opção não encontrada")

    print('\nSaindo...')


if __name__ == "__main__":
    main()
