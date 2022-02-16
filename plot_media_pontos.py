# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:27:49 2022

@author: jdebr
"""

'''Download de dados mensais de chl,resolucao espacial de 4km, entre
01/01/2003 e 31/01/2022,do sensor  MODIS abordo do satelites AQUA,no site https://oceancolor.gsfc.nasa.gov/l3/
limmites:
-11.47, -35.5, -18.3, -39.75
Objetivo = plotar a media mensal de diferentes pontos do mapa
-definir pontos
-calcular medias
-plotar

'''


######
'''concatei os arquivos de chl, com uma dimensao de tempo. '''

'''modulos necessarios para abrir,visualizar e editar os arquivos'''
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs
import seaborn as sns
import pandas as pd
from datetime import datetime

'''acessando os dados de clorofila'''
fn = 'C:/Users/jdebr/Documents/clorofila_bahia/chl_ba_monthly.nc'
ds = nc.Dataset(fn)
print(ds)

'''vendo as dimensoes do array'''
for dim in ds.dimensions.values():
    print(dim)

'''vendo as variaveis'''
for var in ds.variables.values():
    print(var)
    
print(ds['chlor_a'])

'''definindo as variaveis'''
chl=ds['chlor_a'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]


'''criando uma lista com as datas da serie temporal'''
teste=pd.date_range(start="2003-01-01",end="2021-12-31",freq='M')

'''Mudando a quantidade de ticks no eixo x do grafico'''


'''plotando serie temporal dos pixels'''

####vou listar os pontos e plotar
fig = plt.figure()
plt.suptitle('Clorofila mensal(mg/m³)',fontsize=16)
ax = fig.add_subplot()

#bts - perto da boia 
bts_sim=chl[:,37,28]

ax.plot(teste,bts_sim,'--r',color='red',label='BTS')

#rio jequitinhonha
rio_j=chl[:,104,22]
ax.plot(teste,rio_j,color='green',label='Rio Jequitinhonha')


#abrolhos
abro1=chl[:,155,20]
ax.plot(teste,abro1,'--r',color='black',label='Abrolhos')

#Adicionando label,titulo e legenda
plt.xlabel('Ano')
plt.ylabel('clorofila-a(mg.m³')
plt.suptitle('Clorofila-a na costa da Bahia')
ax.legend()
###adicionando mais tickers
extraticks=np.arange(2003,2022,2).tolist()
plt.xticks()
###########################################################################

'''Marcando pontos no mapa'''
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,((chl_jan[18])),transform=ccrs.PlateCarree(),cmap='Spectral_r')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False
ax.coastlines()
plt.colorbar()
plt.suptitle('Clorofila na superfície em janeiro de 2021(mg/m³) ')

###plotando os pontos em um mapa
ax.plot((-38.56),(-13.0),color='red', marker='o',transform=ccrs.PlateCarree())
ax.text((-38.56),(-13.0), 'bts',fontsize =15,horizontalalignment='left',transform=ccrs.PlateCarree())
ax.plot(-38.81,-15.83,color='yellow', marker='o',transform=ccrs.PlateCarree())
ax.text(-38.81,-15.83, 'Rio Jequitinhonha',fontsize =15,horizontalalignment='right',transform=ccrs.PlateCarree())
ax.plot(-38.89,-17.95,color='black', marker='o',transform=ccrs.PlateCarree())
ax.text(-38.89,-17.95, 'Abrolhos',fontsize =15,horizontalalignment='right',transform=ccrs.PlateCarree())
