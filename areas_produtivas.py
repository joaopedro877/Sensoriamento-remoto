# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:51:50 2022

@author: jdebr
"""

''' Visualizando quantos meses cada pixel possui um valor de clorofila acima de 1 mg/m³'''
''' Indicando o mes da maior e menor concentracao de clorofila, similar ao que vi em alguns
artigos->citar depois'''
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from cartopy.feature import ShapelyFeature

'''acessando os dados de clorofila'''
fn = 'C:/Users/jdebr/Documents/clorofila_bahia/chl_ba_monthly.nc'
ds = nc.Dataset(fn)

'''definindo as variaveis'''
chl=ds['chlor_a'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]


'''em quantos % do tempo (228 meses) a clorofila esteve acima de 0.5 mg/m³ em cada pixel'''

prod=np.zeros_like(chl[0])

for i in range(0,164):
    for j in range(0,102):
        prod[i,j]=(((chl[:,i,j]>0.5).tolist()).count(True))*100/228
prod[prod==0]=np.nan
'''visualisando a imagem'''
levels=np.linspace(0,100,11)
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,prod,60,levels=levels,transform=ccrs.PlateCarree(),cmap='jet')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False
ax.coastlines(resolution = '10m')
fname = r'C:/Users/jdebr/Documents/clorofila_bahia/ne_10m_bathymetry_K_200.shp'
shape_feature = ShapelyFeature(Reader(fname).geometries(),ccrs.PlateCarree(), edgecolor='red',linestyle='-')
ax.add_feature(shape_feature, facecolor='none')
cb=plt.colorbar( ticks=[0,10,20,30,40,50,60,70,80,90,100])
plt.suptitle('Chlorophyll-a > 0.5 mg/m³')
cb.ax.set_xlabel('% of time')
plt.subplots_adjust(top=0.945,bottom=0.041,left=0.01,right=0.735,hspace=0.195,wspace=0.2)  

'''em quantos % do tempo (228 meses) a clorofila esteve acima de 1 mg/m³ em cada pixel'''
prod1=np.zeros_like(chl[0])

for i in range(0,164):
    for j in range(0,102):
        prod1[i,j]=(((chl[:,i,j]>1).tolist()).count(True))*100/228
prod1[prod1==0]=np.nan
'''visualisando a imagem'''
levels=np.linspace(0,100,11)
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,prod1,60,levels=levels,transform=ccrs.PlateCarree(),cmap='jet')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False
ax.coastlines(resolution = '10m')
ax.add_feature(shape_feature, facecolor='none')
cb=plt.colorbar( ticks=[0,10,20,30,40,50,60,70,80,90,100])
plt.suptitle('Chlorophyll-a > 1.0 mg/m³')
cb.ax.set_xlabel('% of time')
plt.subplots_adjust(top=0.94,bottom=0.041,left=0.0,right=0.8,hspace=0.195,wspace=0.2)
