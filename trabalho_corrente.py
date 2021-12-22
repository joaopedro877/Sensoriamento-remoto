# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:46:25 2021

@author: jdebr
"""

'''Download de dados mensais de corrente e camada de mistura, do modelo do Copernicus, disponivel em
https://resources.marine.copernicus.eu/products. Coordenadas : -50,-30,-10,-30, dados sao de 2019
a 2021.'''

import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt
import os
from cartopy import config
import cartopy.crs as ccrs

"abrindo o arquivo de corrente e camada de mistura"
fn = 'C:/Users/jdebr/Documents/Oceanografia/Disciplinas/Semestre_2021.2/Introducao_a_geotecnologias/ATV/corrente_e_camada_de_mistura_2019_2021.nc'
ds = nc.Dataset(fn)
print(ds)

'''vendo as dimensoes do array'''
for dim in ds.dimensions.values():
    print(dim)

'''vendo as variaveis'''
for var in ds.variables.values():
    print(var)
    

''' plotando a camada de mistura em janeiro somente'''
####3
'''definindo a  variavel mld como a resultan.'''
mld = ds['mlotst'][:]
mld_jan = mld[0:26:12]

'''definindo lat e lon'''
lat =ds['latitude'][:]
lon = ds['longitude'][:]

'''plotando'''
fig = plt.figure()
plt.suptitle('Espessura da camada de mistura em janeiro, em metros',fontsize=16)
ax1 = fig.add_subplot(1,3,1, projection=ccrs.PlateCarree())
ax1.contourf(lon, lat,mld_jan[0], 60,transform=ccrs.PlateCarree(),vmin=6,vmax=34)
ax1.coastlines()
g1 = ax1.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g1.ylabels_right = False
g1.xlabels_top = False
ax1.title.set_text('2019')



ax2 = fig.add_subplot(1,3,2, projection=ccrs.PlateCarree())
plt.contourf(lon, lat,mld_jan[1], 60,transform=ccrs.PlateCarree(),vmin=6,vmax=34)
ax2.title.set_text('2020')
g2 = ax2.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g2.ylabels_right = False
g2.ylabels_left = False
g2.xlabels_top = False
ax2.coastlines()
plt.show()

ax2.streamplot(x,y,u[1],v[1],transform=ccrs.PlateCarree(),linewidth=2, density=2,color='red',arrowstyle='wedge')


ax3 = fig.add_subplot(1,3,3, projection=ccrs.PlateCarree())
plt.contourf(lon, lat,mld_jan[2], 60,transform=ccrs.PlateCarree(),vmin=6,vmax=34)
ax3.title.set_text('2021')
ax3.set_xticks([-50,-40,-30], crs=ccrs.PlateCarree())
ax3.set_yticks([-10,-20,-30], crs=ccrs.PlateCarree())
ax3.coastlines()
plt.show()
ax3.streamplot(x,y,u[2],v[2],transform=ccrs.PlateCarree(),linewidth=2, density=2,color='red',arrowstyle='wedge')

#colorbar

fig.subplots_adjust(right=0.8)
im = ax.imshow(np.random.random((10,10)), vmin=6, vmax=34)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
fig.colorbar(im, cax=cbar_ax)


''' definindo as variaveis de corrente'''


'''resultante da corrente na coluna d'agua'''
comp_v = np.sum(ds['vo'],axis=1)
comp_u =np.sum(ds['uo'],axis=1)

'''corrente em janeiro'''
v=comp_v[0:26:12]
u=comp_u[0:26:12]
u[u < (-100)] = 0
v[v<(-100)]=0
u=u[1][0:241:5,0:241:5]
v=v[1][0:241:5,0:241:5]
x,y = lon[0:241:5],lat[0:241:5]

'''plotando a corrente nos supbplots'''
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat, mld_jan[1], 60,transform=ccrs.PlateCarree())
ax.coastlines()
plt.colorbar()


plt.quiver(x,y,u,v, scale_units='dots', scale=0.4,linewidth=2,)
ax.coastlines()
plt.show()



