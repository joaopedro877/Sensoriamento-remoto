# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:27:29 2022

@author: jdebr
"""
import xarray as xr
import os, glob
import imageio




png_dir = 'C:/Users/jdebr/Documents/Iniciação Científica_Fitoplâncton_2021/Padrões de clorofila na costa brasileira'

max_chl = np.log10(chl[:12,:,:].max())
min_chl = np.log10(chl[:12,:,:].min())

for i in np.arange(12):
    plt.figure()
    #colorbar com um intervalo fixo
    plt.contourf(lon,lat,np.log10(chl[i,:,:]), levels = np.linspace(min_chl,max_chl,12)), plt.colorbar()
    plt.savefig(png_dir + 'fixed_cb_chl' + str(i) +'.png')
    
fixed_cb_images = glob.glob(png_dir + ('fix*'))  
fix = [imageio.imread(file) for file in fixed_cb_images]
imageio.mimsave(png_dir + '/chl2.gif', fix, fps = 3)
