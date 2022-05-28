# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:48:29 2022

@author: jdebr
"""

''' Indicando o mes da maior e menor concentracao de clorofila, similar ao que vi em alguns
artigos->citar depois'''
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs
import seaborn as sns
import matplotlib as mpl
import xarray as xr

'''acessando os dados de clorofila'''
fn = 'C:/Users/jdebr/Documents/clorofila_bahia/chl_ba_monthly.nc'
ds = nc.Dataset(fn)
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
'''separando os meses'''


chl_jan= chl[0:228:12]
chl_fev=chl[1:228:12]
chl_mar=chl[2:228:12]
chl_abr=chl[3:228:12]
chl_mai=chl[4:228:12]
chl_jun=chl[5:228:12]
chl_jul=chl[6:228:12]
chl_ago=chl[7:228:12]
chl_set=chl[8:228:12]
chl_out=chl[9:228:12]
chl_nov=chl[10:228:12]
chl_dez=chl[11:228:12]

chl_jan_med = np.mean(chl_jan,axis=0)
chl_fev_med = np.mean(chl_fev,axis=0)
chl_mar_med = np.mean(chl_mar,axis=0)
chl_abr_med = np.mean(chl_abr,axis=0)
chl_mai_med = np.mean(chl_mai,axis=0)
chl_jun_med = np.mean(chl_jun,axis=0)
chl_jul_med = np.mean(chl_jul,axis=0)
chl_ago_med = np.mean(chl_ago,axis=0) 
chl_set_med = np.mean(chl_set,axis=0)
chl_out_med = np.mean(chl_out,axis=0)
chl_nov_med = np.mean(chl_nov,axis=0)
chl_dez_med = np.mean(chl_dez,axis=0)

'''criando um array para representar o ano climatologico'''
chl_ano_clim = np.empty((12,164,102))
chl_ano_clim[0]=chl_jan_med
chl_ano_clim[1]=chl_fev_med
chl_ano_clim[2]=chl_mar_med
chl_ano_clim[3]=chl_abr_med
chl_ano_clim[4]=chl_mai_med
chl_ano_clim[5]=chl_jun_med
chl_ano_clim[6]=chl_jul_med
chl_ano_clim[7]=chl_ago_med
chl_ano_clim[8]=chl_set_med
chl_ano_clim[9]=chl_out_med
chl_ano_clim[10]=chl_nov_med
chl_ano_clim[11]=chl_dez_med


'''descobrindo em qual mes ocorrem os valores maximos e minimos de clorofila em cada pixel'''

mes_max=np.zeros_like(chl_abr_med)
def max_chl(x,y):
    return np.max(chl_ano_clim[:,x,y])

for i in range(0,164):
    for j in range(0,102):
        if max_chl(i,j)!= 0 : 
            mes_max[i,j]=(int((np.where(chl_ano_clim[:,i,j]==max_chl(i,j)))[0])+1)



'''visualisando a imagem'''
levels=np.linspace(1,13,13)
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,mes_max,60,levels=levels,transform=ccrs.PlateCarree(),cmap='jet')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines(resolution = '10m')
cb=plt.colorbar( ticks=[1,2,3,4,5,6,7,8,9,10,11,12], orientation='horizontal',fraction=0.09, pad=0.08)
cb.ax.set_xticklabels(['january','february','march','april','may','june','july','august','october','september','november','december'])
plt.suptitle('month of highest values of chlorophyll-a, based on climatological year')
ax.set_xlabel('month')

'''consertar o colorbar -> posicao e tamanho'''



'''fazendo o mesmo para os minimos'''
mes_min=np.zeros_like(chl_abr_med)
def min_chl(x,y):
    return np.min(chl_ano_clim[:,x,y])

for i in range(0,164):
    for j in range(0,102):
        if min_chl(i,j)!= 0 : 
            mes_min[i,j]=(int((np.where(chl_ano_clim[:,i,j]==min_chl(i,j)))[0])+1)
            
levels=np.linspace(1,13,13)
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,mes_min,60,levels=levels,transform=ccrs.PlateCarree(),cmap='jet')
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines(resolution = '10m')
cb=plt.colorbar( ticks=[1,2,3,4,5,6,7,8,9,10,11,12], orientation='horizontal',fraction=0.09, pad=0.08)
cb.ax.set_xticklabels(['january','february','march','april','may','june','july','august','october','september','november','december'])
plt.suptitle('month of lowest values of chlorophyll-a, based on climatological year')
ax.set_xlabel('month')

#######################################################################
'''algo nao esta funcionando corretamente - partes em branco no mapa'''

'''Salvando em formato netcdf'''
#salvando para ver no SNAP
df = xr.DataArray(mes_max, coords=[('lat', lat), ('lon', lon)])
df.to_netcdf('chl_mes_max.nc')