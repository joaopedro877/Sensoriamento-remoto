# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 11:38:08 2022

@author: jdebr
"""

'''correlação entre chl e sst'''
''' a variavel e a sst e a y e a chl'''
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs
import seaborn as sns
import matplotlib as mpl
import scipy.stats
from scipy.stats import pearsonr

'''abrindo dados de sst e chl, mensais, entre 2003 e 2021'''

fn = 'C:/Users/jdebr/Documents/clorofila_bahia/sst_ba.nc'
ds = nc.Dataset(fn)
'''definindo as variaveis'''
sst=ds['sst'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]

fn2='C:/Users/jdebr/Documents/clorofila_bahia/chl_ba_monthly.nc'
ds2=nc.Dataset(fn2)
chl=ds2['chlor_a'][:]

'''Correlacao de Pearson entre sst(x) e chl(y)'''
#criando uma matriz vazia com o mesmo shape que as de sst e chl
corr_matrx= np.empty_like(sst[0],dtype=float)

#colocando os valores de correlacao de sst e chl na matriz

#acredito que tenho que apagar os NaN


   
corr_matrx[corr_matrx==0]=np.nan


for i in range(0,164):
    for j in range(0,102):
        corr_matrx[i,j]=(pearsonr((sst[:,i,j]),(chl[:,i,j])))[0]

'''visaulisando a imagem '''
levels=np.linspace(-1,1,100)
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,corr_matrx,60,levels=levels,transform=ccrs.PlateCarree(),cmap='jet',vmin=-1,vmax=1)
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines(resolution = '10m')
cb=plt.colorbar()
fname = r'C:/Users/jdebr/Documents/clorofila_bahia/ne_10m_bathymetry_K_200.shp'
shape_feature = ShapelyFeature(Reader(fname).geometries(),ccrs.PlateCarree(), edgecolor='black',linestyle='--')
ax.add_feature(shape_feature, facecolor='none')

''' Os pontos perto de 13° demonstram uma correlacao negativa forte, possivelmente devido a ressurgencia'''
ax.plot((lon[23]),(lat[40]),color='black', marker='.',transform=ccrs.PlateCarree())
ax.title.set_text('Coeficiente de correlação entre temperatura da superfície do mar e clorofila-a na costa da Bahia')

