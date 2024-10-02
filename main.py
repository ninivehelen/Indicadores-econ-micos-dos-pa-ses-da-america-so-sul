import requests
from extrair_dados_paises import *

def acessando_api():
    # URL da API do IBGE
    url = "https://servicodados.ibge.gov.br/api/v1/paises/paises"

    # Fazendo a requisição na API
    response = requests.get(url)

    # Verificando se a conexão foi realizada
    if response.status_code == 200:
        api_acesso = response.json()
        return api_acesso 
    else:
      print("Erro ao acessar a API:", response.status_code)
    
if __name__ == '__main__':
    response = acessando_api()
    acessa_paises(response)
