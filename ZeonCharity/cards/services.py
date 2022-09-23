import pandas as pd
import json


def stats():
    data= pd.read_excel('https://data.gov.kg/dataset/5f490a2f-1248-4b56-b613-b1d697f3d141/resource/04009bb4-8262-4de3-8b62-e2f43c979af4/download/-.xlsx')
    data = data.rename(columns = {'Регион':'region'})
    holder = []
    for index in data.index:
        raw = data.iloc[index][1:]
        holder += [sum(list(raw))]
    data['all_years'] = pd.Series(holder)
    return json.loads(data.to_json())


def stats_proba():


    data= pd.read_excel('https://data.gov.kg/dataset/5f490a2f-1248-4b56-b613-b1d697f3d141/resource/04009bb4-8262-4de3-8b62-e2f43c979af4/download/-.xlsx')

    holder = []
    for index in data.index:
        raw = data.iloc[index][1:]
        holder += [sum(list(raw))]
        
    final_df = pd.DataFrame()
    final_df['all_years'] = holder

    population = pd.Series([6_636_800, 548_200, 1_260_600, 501_900, 291_100, 1_391_700, 271_000, 975_000, 1_074_100, 322_200])
    final_df['population'] = population
    final_df['proba'] = final_df['all_years'] / final_df['population']
    
    return json.loads(final_df.to_json())
