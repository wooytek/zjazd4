import pandas as pd

df = pd.read_json('data\\data.json')

print(df.head())

age_under_30 = df[df['wiek'] < 30]
print(age_under_30)

df['wiek_za_5_lat'] = df['wiek'] +5
print(f'\n dana z kolumną wiek za 5 lat')
print(df)

sredni_wiek = df['wiek'].mean()
print(f'średni wiek: {sredni_wiek}')

df_sorted = df.sort_values('wiek', ascending=False)
print(f'\ndane posortowane malejąco:')
print(df_sorted)

df.to_json('final_data\\f_data.json')
df.to_json('final_data\\f_data1.json', indent = 4)
df.to_json('final_data\\f_data2.json', indent = 4, orient='split')
df.to_json('final_data\\f_data3.json', indent = 4, orient='records')
df.to_json('final_data\\f_data4.json', indent = 4, orient='index')
df.to_json('final_data\\f_data5.json', indent = 4, orient='columns')