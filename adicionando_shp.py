# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:03:56 2022

@author: jdebr
"""

'''Adicionando arquivos em shp aos mapas criados.'''
'''download do shapefile de batimetria em https://www.naturalearthdata.com/downloads/10m-physical-vectors/'''
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from cartopy import config
import cartopy.crs as ccrs
import seaborn as sns

'''acessando os dados de clorofila'''
fn1 = 'C:/Users/jdebr/Documents/clorofila_bahia/chl_ba_monthly.nc'
ds = nc.Dataset(fn1)
print(ds)

'''definindo as variaveis'''
chl=ds['chlor_a'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]

'''removendo a bts e outros'''
chl[:,29:36,22:31]=np.nan
chl[:,147,13]=np.nan
chl[:,126:128,14]=np.nan 
chl[:,114:116,17]=np.nan
chl[:,28,24:26]=np.nan   
chl[:,149,14]=np.nan  
chl[:,154,8]=np.nan

'''vendo os dados de um mes aleatorio'''
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,np.log10(chl[3]),60,transform=ccrs.PlateCarree(),cmap='jet')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines(resolution = '10m')
cb=plt.colorbar()

'''adicionando linha de 200m'''
fname = r'C:/Users/jdebr/Documents/clorofila_bahia/ne_10m_bathymetry_K_200.shp'
shape_feature = ShapelyFeature(Reader(fname).geometries(),ccrs.PlateCarree(), edgecolor='red',linestyle='--')
ax.add_feature(shape_feature, facecolor='none')
'''adicionando rios da regiao'''
fname2=r'C:/Users/jdebr/Documents/clorofila_bahia/ne_10m_rivers_lake_centerlines_scale_rank/ne_10m_rivers_lake_centerlines_scale_rank.shp'
shape_feature = ShapelyFeature(Reader(fname2).geometries(),ccrs.PlateCarree(), edgecolor='blue')
ax.add_feature(shape_feature, facecolor='none')
'''esse shp nao e o melhor, preciso baixar um mais detalhado'''


