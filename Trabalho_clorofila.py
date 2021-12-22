# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:53:39 2021

@author: jdebr
"""

''' Trabalho da disciplina Introducao as geotecnologias'''

'''Download de dados mensais de chl,resolucao espacial de 4km, entre
01/01/2003 e 28/02/2021,do sensor  MODIS abordo do satelites AQUA,no site https://oceancolor.gsfc.nasa.gov/l3/
Coordenadas : -50,-30,-10,-30'''



######
'''concatei os arquivos de chl, com uma dimensao de tempo. '''

'''modulos necessarios para abrir,visualizar e editar os arquivos'''
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs

'''acessando os dados de clorofila'''
fn = 'C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Semestre_2021.2/Introducao_a_geotecnologias/ATV/clorofila.nc'
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

'''separando os meses'''
chl=ds['chlor_a'][:]

chl_jan= chl[0:218:12]
chl_fev=chl[1:218:12]
chl_mar=chl[2:218:12]
chl_abr=chl[3:218:12]
chl_mai=chl[4:218:12]
chl_jun=chl[5:218:12]
chl_jul=chl[6:218:12]
chl_ago=chl[7:218:12]
chl_set=chl[8:218:12]
chl_out=chl[9:218:12]
chl_nov=chl[10:218:12]
chl_dez=chl[11:218:12]

'''vendo janeiro de 2021'''



ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat, np.log10(chl_jan[18]), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines()
plt.colorbar()
plt.suptitle('Clorofila na superfície em janeiro de 2021 (log10 mg/m³) ')

'''em 2016(jan[13]) tambem ocorreu evento floracao similar, mas com maiores proporcoes'''

'''media total dos meses'''
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

np.min((np.log10(chl_jan)))

'''plotando as medias juntas'''
fig = plt.figure()
plt.suptitle('Clorofila mensal (log10 mg/m³)',fontsize=16)
ax1 = fig.add_subplot(2,6,1, projection=ccrs.PlateCarree())
ax1.contourf(lon, lat,np.log10(chl_jan_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax1.title.set_text('Janeiro')
ax1.coastlines()

ax2 = fig.add_subplot(2,6,2, projection=ccrs.PlateCarree())
ax2.contourf(lon, lat,np.log10(chl_fev_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax2.title.set_text('Fevereiro')
ax2.coastlines()

ax3 = fig.add_subplot(2,6,3, projection=ccrs.PlateCarree())
ax3.contourf(lon, lat,np.log10(chl_mar_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax3.title.set_text('Março')
ax3.coastlines()

ax4 = fig.add_subplot(2,6,4, projection=ccrs.PlateCarree())
ax4.contourf(lon, lat,np.log10(chl_abr_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax4.title.set_text('Abril')
ax4.coastlines()

ax5 = fig.add_subplot(2,6,5, projection=ccrs.PlateCarree())
ax5.contourf(lon, lat,np.log10(chl_mai_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax5.title.set_text('Maio')
ax5.coastlines()

ax6 = fig.add_subplot(2,6,6, projection=ccrs.PlateCarree())
ax6.contourf(lon, lat,np.log10(chl_jun_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax6.title.set_text('Junho')
ax6.coastlines()


ax7 = fig.add_subplot(2,6,7, projection=ccrs.PlateCarree())
ax7.contourf(lon, lat,np.log10(chl_jul_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax7.title.set_text('Julho')
ax7.coastlines()

ax8 = fig.add_subplot(2,6,8, projection=ccrs.PlateCarree())
ax8.contourf(lon, lat,np.log10(chl_ago_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax8.title.set_text('Agosto')
ax8.coastlines()

ax9 = fig.add_subplot(2,6,9, projection=ccrs.PlateCarree())
ax9.contourf(lon, lat,np.log10(chl_set_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax9.title.set_text('Setembro')
ax9.coastlines()

ax10 = fig.add_subplot(2,6,10, projection=ccrs.PlateCarree())
ax10.contourf(lon, lat,np.log10(chl_out_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax10.title.set_text('Outubro')
ax10.coastlines()

ax11 = fig.add_subplot(2,6,11, projection=ccrs.PlateCarree())
ax11.contourf(lon, lat,np.log10(chl_nov_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax11.title.set_text('Novembro')
ax11.coastlines()

ax12 = fig.add_subplot(2,6,12, projection=ccrs.PlateCarree())
ax12.contourf(lon, lat,np.log10(chl_dez_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax12.title.set_text('Dezembro')
ax12.coastlines()

fig.tight_layout()
fig.subplots_adjust(right=0.8)

im = ax.imshow(np.random.random((12,12)), vmin=-1.5, vmax=1.5)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax )
plt.show()


'''comparacao entre a media de janeiro e janeiro de 2021'''
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


fig = plt.figure()
plt.suptitle('Anomalia de chl (log10 mg/m³)',fontsize=16)
ax1 = fig.add_subplot(1,2,1, projection=ccrs.PlateCarree())
ax1.contourf(lon, lat,np.log10(chl_jan_med), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
g1 = ax1.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g1.ylabels_right = False
g1.xlabels_top = False
ax1.title.set_text('Média total de janeiro(2003-2021)')
ax1.coastlines()

ax2 = fig.add_subplot(1,2,2, projection=ccrs.PlateCarree())
plt.contourf(lon, lat,np.log10(chl_jan[18]), 60,transform=ccrs.PlateCarree(),vmin=-1.5,vmax=1.5)
ax2.title.set_text('Média de janeiro de 2021')
ax2.coastlines()
g2 = ax2.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g2.ylabels_right = False
g2.ylabels_left = False
g2.xlabels_top = False


fig.tight_layout()
fig.subplots_adjust(right=0.8)
im = ax.imshow(np.random.random((12,12)), vmin=-1.5, vmax=1.5)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax )
np.meshgrid(lon,lat)
plt.show()
