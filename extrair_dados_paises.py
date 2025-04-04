import pandas as pd 

def acessa_paises(dados):
 # Lista de IDs dos países da América do Sul
    america_do_sul_ids = [32, 68, 76, 152, 170, 188, 192, 214, 218, 222, 320, 332, 340, 484, 558, 591, 600, 604, 858, 862]
    # IDs dos países da América do Sul

    # Filtrando e armazenando as informações dos países da América do Sul
    america_do_sul_paises = []
    
    for paises in dados:
        if paises['id']['M49'] in america_do_sul_ids:
            america_do_sul_paises.append({
                'nome': paises['nome']['abreviado'],
                'codigo': paises['id']['ISO-3166-1-ALPHA-2'],
                'area': paises['area']['total'],
                'capital': paises['governo']['capital']['nome'],
                'moeda': paises['unidades-monetarias'][0]['nome'],
                'lingua': paises['linguas'][0]['nome'],
                'historico':paises['historico'],
            })

    # Mostrando as informações dos países da América do Sul
    print("Informações dos Países da América do Sul:")
    for paises in  america_do_sul_paises:
        print(f"Nome: {paises['nome']}")
        print(f"Código: {paises['codigo']}")
        print(f"Área: {paises['area']} km²")
        print(f"Capital: {paises['capital']}")
        print(f"Moeda: {paises['moeda']}")
        print(f"Língua: {paises['lingua']}")
        print(f"Histórico: {paises['historico']}")

    df_dados = pd.DataFrame(america_do_sul_paises)
    df_dados = df_dados.drop_duplicates(subset='nome', keep='last')
    print(df_dados)
    df_dados.to_csv("paises_informacoes.csv", encoding='utf8', index=False)