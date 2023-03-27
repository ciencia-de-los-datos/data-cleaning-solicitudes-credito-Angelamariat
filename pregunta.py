"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    #df.isnull().sum()
    df.dropna(subset=['tipo_de_emprendimiento','barrio','comuna_ciudadano'], inplace=True)
    #Sexo
    df.sexo=df.sexo.str.lower() 
    #Tipo de emprendimiento
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    #Idea de negocio
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace('-', ' ', regex=True).replace('_', ' ', regex=True).str.strip()
    #barrio
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('-', ' ', regex=True).replace('_', ' ', regex=True)
    #fecha de beneficio
    df.fecha_de_beneficio=pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    #Monto del credito 
    df.monto_del_credito=df.monto_del_credito.str.replace(',','',regex=True)
    df.monto_del_credito=df.monto_del_credito.str.replace('$','',regex=True).str.strip()
    df.monto_del_credito=pd.to_numeric(df.monto_del_credito)
    #Linea credito
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace('-', ' ', regex=True).replace('_', ' ', regex=True).str.strip()
    df.línea_credito = df.línea_credito.str.replace('.', '', regex=True)
    
    df.drop_duplicates(inplace=True)
    
    return df
