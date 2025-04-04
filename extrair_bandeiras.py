
import pandas as pd 

def baixar_bandeiras(dados):
 # Lista de nomes de países da America Latina
    nomes_paises = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
              "Costa Rica", "Cuba", "Dominican Republic", "Ecuador",
               "El Salvador", "Guatemala", "Haiti", "Honduras",
                 "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Uruguay", "Venezuela"]
  

    # Filtrando e armazenando as informações dos países da América do Sul
    bandeiras = []
    
    for paises in dados:
        if paises['name']['common'] in nomes_paises:
            bandeiras.append({
                'nome': paises['name']['common'],
                'png': paises['flags']['png']
            })

    # Mostrando as informações dos países da América do Sul
    print("Informações das bandeiras :")
    for paises in  bandeiras:
        print(f"Nome: {paises['nome']}")
        print(f"PNG: {paises['png']}")
       
    df_dados = pd.DataFrame(bandeiras)
    print(df_dados)
    df_dados.to_csv("paises_bandeiras.csv", encoding='utf8', index=False)