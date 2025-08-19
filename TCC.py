# Importação da biblioteca para manipulação e análise de dados em formato de tabelas
import pandas as pd
# Funções para trabalhar com datas e horários (definir intervalos de tempo, comparar datas, etc.)
from datetime import time, datetime
# Leitura da planilha Excel com os dados dos sensores
df = pd.read_excel('teste0805 e 1706 - coleta de dados.xlsx')
df.columns
df.head()
# Conversão da coluna de data para o tipo datetime.date (para facilitar comparações)
df['DATE'] = pd.to_datetime(df['DATE']).dt.date
# Conversão da coluna de hora para o tipo datetime.time, com formato definido
df['TIME'] = pd.to_datetime(df['TIME'].astype(str), format= '%H:%M:%S').dt.time
# Seleção apenas das colunas de interesse: data, hora, nível e chuva
sensor = df[['DATE','TIME','Nível','Chuva']]
# Definição da data e do intervalo de horário que se deseja analisar
data_desejada = datetime (2025,5,8).date()
horario_inicio= time(15,54,0)
horario_fim= time(15,56,0)
# Verificação se a data existe nos registros da planilha
if data_desejada in sensor['DATE'].values:
    # Filtra os registros que estão dentro da data e do intervalo de horário desejado
    intervalo = sensor[
        (sensor['DATE'] == data_desejada) &
        (sensor['TIME'] >= horario_inicio) &
        (sensor['TIME'] <= horario_fim)
        ]
    # Verifica se o intervalo tem registros
    if not intervalo.empty:
        # Calcula o total de chuva com base nos valores únicos registrados no intervalo
        valores_unicos = intervalo['Chuva'].unique()
        chuva_total = valores_unicos.sum()
        # Calcula o número total de batidas do pluviômetro (considerando 0,2 mm por batida)
        batidas_total = round(chuva_total / 0.2)
        # Exibe os resultados finais
        print(f"Total de batidas: {batidas_total}")
        print(f"Valores únicos de chuva no intervalo: {valores_unicos}")
        print(f"Chuva total no intervalo (somando valores únicos): {chuva_total:.1f} mm")
    else:
        # Caso a data exista mas não haja registros no horário definido
        print(f"A data {data_desejada} existe, mas não há registros no intervalo de horário definido.")
else:
    # Caso a data informada não exista na planilha
    print(f"A data {data_desejada} não foi encontrada na planilha!")