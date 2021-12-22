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


''' os arquivos a serem concatenados devem ter o nome parecido e estar na mesma pasta. O script deve estar 
tambem na mesma pasta para que os arquivos sejam lidos. Caso nao estejam vai dar erro'''

ds = xarray.open_mfdataset('AQUA_MODIS.*.nc',combine = 'nested', concat_dim="time")

'''dando um nome e salvadano'''
ds.to_netcdf('sstjan.nc')


