# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:03:36 2021

@author: jdebr
"""

'''Parte dedicada  a sst'''

'''Download de dados mensais de sst,com criteirios iguais a clorofila'''



import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs

"abrindo o arquivo de sst "
fn = 'C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Semestre_2021.2/Introducao_a_geotecnologias/ATV/sst20032021.nc'
ds = nc.Dataset(fn)
print(ds)


'''vendo as dimensoes do array'''
for dim in ds.dimensions.values():
    print(dim)

'''vendo as variaveis'''
for var in ds.variables.values():
    print(var)
    

'''                      plotando a sst                            '''
####3
'''definindo as variaveis'''
sst=ds['sst4'][:]
lat=ds['lat'][:]
lon=ds['lon'][:]

'''separando os meses, ja pela media'''
sst_jan= np.mean(sst[0:218:12],axis=0)
sst_fev=np.mean(sst[1:218:12],axis=0)
sst_mar=np.mean(sst[2:218:12],axis=0)
sst_abr=np.mean(sst[3:218:12],axis=0)
sst_mai=np.mean(sst[4:218:12],axis=0)
sst_jun=np.mean(sst[5:218:12],axis=0)
sst_jul=np.mean(sst[6:218:12],axis=0)
sst_ago=np.mean(sst[7:218:12],axis=0)
sst_set=np.mean(sst[8:218:12],axis=0)
sst_out=np.mean(sst[9:218:12],axis=0)
sst_nov=np.mean(sst[10:218:12],axis=0)
sst_dez=np.mean(sst[11:218:12],axis=0)

'''plotando janeiro media x 2021 '''
fig = plt.figure()
plt.suptitle('Variação de temperatura')
#figura 1
ax1 = fig.add_subplot(1,2,1, projection=ccrs.PlateCarree())
plt.contourf(lon, lat, sst_jan, 60,transform=ccrs.PlateCarree(),cmap='RdBu_r',vmin=18,vmax=28)
ax1.title.set_text('Média total de janeiro(2003-2021) em °C')
g1 = ax1.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g1.ylabels_right = False
g1.xlabels_top = False
ax1.title.set_text('Média total de janeiro(2003-2021) em °C')
ax1.coastlines()

#figura 2
ax2 = fig.add_subplot(1,2,2,projection=ccrs.PlateCarree())
plt.contourf(lon, lat, sst[216,:,:], 60,transform=ccrs.PlateCarree(),cmap='RdBu_r',vmin=18,vmax=28)
ax2.title.set_text('Média de janeiro de 2021')
ax2.coastlines()
g2 = ax2.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g2.ylabels_right = False
g2.ylabels_left = False
g2.xlabels_top = False
#marcando ponto - cabo frio
cab_lat=-22.71555556
cab_lon=-42.01861111
ax1.plot(cab_lon, cab_lat,color='black', marker='o',transform=ccrs.Geodetic())
ax1.text(cab_lon, cab_lat, 'Cabo Frio',horizontalalignment='right',transform=ccrs.Geodetic())
ax2.plot(cab_lon, cab_lat,color='black', marker='o',transform=ccrs.Geodetic())
ax2.text(cab_lon, cab_lat, 'Cabo Frio',horizontalalignment='right',transform=ccrs.Geodetic())

#adicionando colorbar
fig.subplots_adjust(right=0.8)
im = ax.imshow(np.random.random((12,12)),cmap= 'RdBu_r',vmin=18, vmax=28)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)
