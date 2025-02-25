import pandas as pd 
def indicadores_paises(dados):
    todos_indicadores = []  
    
    for indi in dados:
        indicador = indi['indicador'] 
        
        for series in indi['series']:  
            pais_nome = series['pais']['nome']  
            
            if 'serie' in series:
                for serie in series['serie']: 
                    for ano, valor in serie.items():  
    
                        if valor is not None:  
                            todos_indicadores.append({
                                'indicador': indicador,
                                'pais': pais_nome,
                                'ano': ano,  
                                'valor': valor  
                            })
    
    # Print the results for each extracted indicator
    for ind in todos_indicadores:
        print(f"Nome: {ind['indicador']}")
        print(f"País: {ind['pais']}")
        print(f"Ano: {ind['ano']}")
        print(f"Valor: {ind['valor']}")
        print("-------------")  # Separator for clarity
    
    df_dados = pd.DataFrame(todos_indicadores)
    print(df_dados)
    df_dados.to_csv("paises_indicadores.csv", encoding='utf8', index=False)