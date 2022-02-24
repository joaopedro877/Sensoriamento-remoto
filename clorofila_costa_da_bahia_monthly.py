# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:09:39 2022

@author: jdebr
"""

'''Download de dados mensais de chl,resolucao espacial de 4km, entre
01/01/2003 e 31/01/2022,do sensor  MODIS abordo do satelites AQUA,no site https://oceancolor.gsfc.nasa.gov/l3/
limmites:
-11.47, -35.5, -18.3, -39.75
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
import matplotlib as mpl

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


'''vendo os dados de um mes aleatorio'''
ax = plt.axes(projection=ccrs.PlateCarree())
plt.contourf(lon, lat,(np.log10(chl_jan[10])),60,transform=ccrs.PlateCarree(),cmap='viridis',vmin=-2,vmax=1)
'''adicionando lat e lon'''
g = ax.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False

ax.coastlines(resolution = '10m')
cb=plt.colorbar()
list = [-1.44,-1.22,-0.96,-0.72,-0.48,-0.24,0.00,0.24,0.48,0.72]
for i in list:
    i = 10**i
    print(i)
cb.ax.set_yticklabels(['0.03','0.06','0.1','0.2','0.3','0.6','1','1.7','3','5'])
cb.ax.set_xlabel('clorofila(mg/m³)')
plt.suptitle('Clorofila-a na superfície  ( mg/m³) ')








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

'''valores maximos e mínimos de media, para usar o mesmo colorbar'''
max1 = ((chl_jan_med.max()))
min1=((chl_jan_med.min()))

max2 = ((chl_fev_med.max()))
min2=((chl_fev_med.min()))

max3 = ((chl_mar_med.max()))
min3=((chl_mar_med.min()))

max4 = ((chl_abr_med.max()))
min4=((chl_abr_med.min()))

max5 = ((chl_mai_med.max()))
min5=((chl_mai_med.min()))

max6 = ((chl_jun_med.max()))
min6=((chl_jun_med.min()))

max7 = ((chl_jul_med.max()))
min7=((chl_jul_med.min()))

max8 = ((chl_ago_med.max()))
min8=((chl_ago_med.min()))

max9 = ((chl_set_med.max()))
min9=((chl_set_med.min()))

max10 = ((chl_out_med.max()))
min10=((chl_out_med.min()))

max11 = ((chl_nov_med.max()))
min11=((chl_nov_med.min()))

max12 = ((chl_dez_med.max()))
min12=((chl_dez_med.min()))

max_total=max(max1,max2,max3,max4,max5,max6,max7,max8,max9,max10,max11,max12)
min_total=min(min1,min2,min3,min4,min5,min6,min7,min8,min9,min10,min11,min12)
'''plotando as medias juntas'''
fig = plt.figure()
plt.suptitle('Clorofila mensal (mg/m³)',fontsize=16)

ax1 = fig.add_subplot(2,6,1, projection=ccrs.PlateCarree())
ax1.contourf(lon, lat,np.log10(chl_jan_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax1.title.set_text('January')
ax1.coastlines()
g = ax1.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False
g.xlabels_bottom = False 


ax2 = fig.add_subplot(2,6,2, projection=ccrs.PlateCarree())
ax2.contourf(lon, lat,np.log10(chl_fev_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax2.title.set_text('February')
ax2.coastlines()
g = ax2.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=False)


ax3 = fig.add_subplot(2,6,3, projection=ccrs.PlateCarree())
ax3.contourf(lon, lat,np.log10(chl_mar_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax3.title.set_text('March')
ax3.coastlines()
g = ax3.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=False)


ax4 = fig.add_subplot(2,6,4, projection=ccrs.PlateCarree())
ax4.contourf(lon, lat,np.log10(chl_abr_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax4.title.set_text('April')
ax4.coastlines()
g = ax4.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=False)

ax5 = fig.add_subplot(2,6,5, projection=ccrs.PlateCarree())
ax5.contourf(lon, lat,np.log10(chl_mai_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax5.title.set_text('May')
ax5.coastlines()
g = ax5.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=False)

ax6 = fig.add_subplot(2,6,6, projection=ccrs.PlateCarree())
ax6.contourf(lon, lat,np.log10(chl_jun_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax6.title.set_text('June')
ax6.coastlines()
g = ax6.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=False)

ax7 = fig.add_subplot(2,6,7, projection=ccrs.PlateCarree())
ax7.contourf(lon, lat,np.log10(chl_jul_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax7.title.set_text('July')
ax7.coastlines()
g = ax7.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False



ax8 = fig.add_subplot(2,6,8, projection=ccrs.PlateCarree())
ax8.contourf(lon, lat,np.log10(chl_ago_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax8.title.set_text('August')
ax8.coastlines()
g = ax8.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.xlabels_top = False
g.ylabels_left=False

ax9 = fig.add_subplot(2,6,9, projection=ccrs.PlateCarree())
ax9.contourf(lon, lat,np.log10(chl_set_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax9.title.set_text('September')
ax9.coastlines()
g = ax9.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.ylabels_left = False
g.xlabels_top = False
g.ylabels_left=False

ax10 = fig.add_subplot(2,6,10, projection=ccrs.PlateCarree())
ax10.contourf(lon, lat,np.log10(chl_out_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax10.title.set_text('October')
ax10.coastlines()
g = ax10.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.ylabels_left = False
g.xlabels_top = False
g.ylabels_left=False

ax11 = fig.add_subplot(2,6,11, projection=ccrs.PlateCarree())
ax11.contourf(lon, lat,np.log10(chl_nov_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax11.title.set_text('November')
ax11.coastlines()
g = ax11.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.ylabels_left = False
g.xlabels_top = False
g.ylabels_left=False

ax12 = fig.add_subplot(2,6,12, projection=ccrs.PlateCarree())
ax12.contourf(lon, lat,np.log10(chl_dez_med), 60,transform=ccrs.PlateCarree(),cmap='jet',vmin=np.log10(min_total),vmax=np.log10(max_total))
ax12.title.set_text('December')
ax12.coastlines()
g = ax12.gridlines(crs=ccrs.PlateCarree(), linestyle='-.', color='gray', draw_labels=True)
g.ylabels_right = False
g.ylabels_left = False
g.xlabels_top = False
g.ylabels_left=False

fig.tight_layout()
fig.subplots_adjust(right=0.7)

chl_med = (chl_jan_med+chl_fev_med+chl_mar_med+chl_abr_med+chl_mai_med+chl_jun_med+chl_jul_med+chl_ago_med+chl_set_med+chl_out_med+chl_nov_med+chl_dez_med)/12
im = ax.imshow(chl_med,cmap='jet', vmin=np.log10(min_total),vmax=np.log10(max_total))
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cb=plt.colorbar(im, cax=cbar_ax)
list = [-1.25,-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75]
for i in list:
    i = 10**i
    print(i)
cb.ax.set_yticklabels(['0.06','0.1','0.18','0.32',' 0.56','1','1.78','3.16','5.62'])
cb.ax.set_xlabel('chl(mg/m³)')
plt.suptitle('Chlorophyll-a monthly mean ( mg/m³)')
plt.show()
plt.save_fig('media_mensal.jpg')



