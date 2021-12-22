# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:43:27 2021

@author: jdebr
"""
#15/11/2021
'''juntando os dados de sst em um unico arquivo em netcdf, adicionando uma dimensao de tempo'''
import xarray
import numpy as np
import  pandas as pd
import netCDF4 


''' os arquivos a serem concatenados devem estar na mesma pasta. Deve estar no formato abaixo para funcionar'''

ds = xarray.open_mfdataset(C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Semestre_2021.2/Introducao_a_geotecnologias/dados_level3/sea_level_anomaly_chl/*.nc',combine = 'nested', concat_dim="time")

'''dando um nome e salvadano'''
ds.to_netcdf('sstjan.nc')


