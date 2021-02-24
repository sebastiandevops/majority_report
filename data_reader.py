#!/usr/bin/python3
"""Function to read csv file
"""
import pandas as pd
import numpy as np

def data_reader(filename):
    """Function to read data in CSV file

    Args:
        filename (str): database from Alcaldía de Medellín

    Returns:
        data: dataframe
    """
    data = pd.read_csv(filename, sep=';', parse_dates=True,
                       index_col='seguridad.fecha_hecho')
    data.sort_values(by=['seguridad.fecha_hecho'], inplace=True)
    data.drop(['seguridad.grupo_actor',
               'seguridad.actividad_delictiva',
               'seguridad.parentesco',
               'seguridad.ocupacion',
               'seguridad.discapacidad',
               'seguridad.grupo_especial',
               'seguridad.nivel_academico',
               'seguridad.testigo',
               'seguridad.conducta',
               'seguridad.caracterizacion',
               'seguridad.articulo_penal',
               'seguridad.categoria_penal',
               'seguridad.codigo_barrio',
               'seguridad.modelo',
               'seguridad.color',
               'seguridad.permiso',
               'seguridad.unidad_medida'], axis=1, inplace=True)
    data = data.replace('Sin dato', np.nan)
    for col in data.columns:
        if data[col].dtype == "object":
            data = data.fillna(data[col].value_counts().index[0])
    data['hora'] = data.index.hour
    data['día'] = data.index.weekday
    data['semana'] = data.index.week
    data['mes'] = data.index.month
    data['año'] = data.index.year
    data = data.replace('Sin dato', np.nan)
    data.to_csv('/home/sebastian/Holberton/final_project/data.csv')
    return data
