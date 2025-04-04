import requests
from extrair_dados_paises import *
from extrair_dados_indicadores import *
from extrair_bandeiras import * 

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

def acessando_api_indicadores():
    # URL da API do IBGE
    url = "https://servicodados.ibge.gov.br/api/v1/paises/AR%7CBO%7CBR%7CCL%7CCO%7CCR%7CCU%7CDO%7CEC%7CSV%7CGT%7CHN%7CMX%7CNI%7CPA%7CPY%7CPE%7CPR%7CUY%7CVE/indicadores/77818%7C77819%7C77820%7C77821%7C77825%7C77826%7C77827%7C77831%7C77845%7C77846"

    # Fazendo a requisição na API
    response = requests.get(url)

    # Verificando se a conexão foi realizada
    if response.status_code == 200:
        api_acesso = response.json()
        return api_acesso 
    else:
      print("Erro ao acessar a API:", response.status_code)

def acessando_api_bandeiras():
    # URL da API do IBGE
    url = "https://restcountries.com/v3.1/all?fields=name,flags"

    # Fazendo a requisição na API
    response = requests.get(url)

    # Verificando se a conexão foi realizada
    if response.status_code == 200:
        api_acesso = response.json()
        return api_acesso 
    else:
      print("Erro ao acessar a API:", response.status_code)


if __name__ == '__main__':
    # response_paises = acessando_api()
    # acessa_paises(response_paises)
    response_indicarores = acessando_api_indicadores()
    indicadores_paises(response_indicarores)
    # response_bandeiras = acessando_api_bandeiras()
    # baixar_bandeiras(response_bandeiras)
    

