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
    
    # Mostrar o resultado dos indicadores
    for ind in todos_indicadores:
        print(f"Nome: {ind['indicador']}")
        print(f"País: {ind['pais']}")
        print(f"Ano: {ind['ano']}")
        print(f"Valor: {ind['valor']}")
        print("-------------")  # Para mostrar separado
    
    # Para salvar em um csv 
    df_dados = pd.DataFrame(todos_indicadores)
    print(df_dados)

    df_dados_turistas = df_dados.loc[df_dados['indicador'] == 'Economia - Chegada de turistas'] 
    df_dados_turistas.to_csv("ind_turistas.csv", encoding='utf8', index=False)

    df_dados_gastos_edu = df_dados.loc[df_dados['indicador'] == 'Economia - Gastos públicos com educação']
    df_dados_gastos_edu.to_csv("ind_eco_gas_educa.csv", encoding='utf8', index=False)

    df_dados_gastos_saude = df_dados.loc[df_dados['indicador'] == 'Economia - Gastos públicos com saúde']
    df_dados_gastos_saude.to_csv("ind_eco_gas_saude.csv", encoding='utf8', index=False)
    
    df_dados_inves_pesq_desen = df_dados.loc[df_dados['indicador'] == 'Economia - Investimentos em pesquisa e desenvolvimento']
    df_dados_inves_pesq_desen.to_csv("ind_eco_gas_pesqu.csv", encoding='utf8', index=False)

    df_dados_total_expor = df_dados.loc[df_dados['indicador'] == 'Economia - Total de exportações']
    df_dados_total_expor.to_csv("ind_eco_total_expo.csv", encoding='utf8', index=False)

    df_dados_total_imp = df_dados.loc[df_dados['indicador'] == 'Economia - Total de importações']
    df_dados_total_imp.to_csv("ind_eco_total_impo.csv", encoding='utf8', index=False)

    df_dados_total_pib = df_dados.loc[df_dados['indicador'] == 'Economia - Total do PIB']
    df_dados_total_pib.to_csv("ind_eco_total_pib.csv", encoding='utf8', index=False)

    df_dados_ind_desen_humano = df_dados.loc[df_dados['indicador'] == 'Indicadores sociais - Índice de desenvolvimento humano']
    df_dados_ind_desen_humano.to_csv("ind_soc_des_huma.csv", encoding='utf8', index=False)

    df_dados_popu_homens = df_dados.loc[df_dados['indicador'] == 'População - Homens']
    df_dados_popu_homens.to_csv("ind_total_popu_homens.csv", encoding='utf8', index=False)

    df_dados_popu_mulheres = df_dados.loc[df_dados['indicador'] == 'População - Mulheres']
    df_dados_popu_mulheres.to_csv("ind_total_popu_mulheres.csv", encoding='utf8', index=False)



   


  