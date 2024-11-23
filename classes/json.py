import os
import json
from settings import arquivo_json
from settings import dic_vazio

class JSON:
    @staticmethod
    def carregar():
        try:
            if os.path.exists(arquivo_json):
                with open(arquivo_json, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return dic_vazio  # Se o arquivo não existir, retorna uma estrutura vazia
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo JSON.")
            return dic_vazio
        
    @staticmethod
    def salvar(dados):
        try:
            with open(arquivo_json, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)
        except IOError:
            print("Erro ao salvar o arquivo JSON.")