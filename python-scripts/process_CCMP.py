from mat_to_netcdf import parse_mat
import xarray as xr
import numpy as np
import os

matarray = []

#gather all the .mat files and put the resulting datasets in a list
direct = os.fsencode("Datasets\CCMP_data")
for file in os.listdir(direct):
    flname = os.fsencode(file)
    decname = os.fsdecode(flname)
    if decname.endswith('.mat'):
        matarray.append(parse_mat('Datasets/CCMP_data/' + decname, {'lat':'latitud', 'lon':'longitud', 'time':'fecha'}, ['u', 'v']))

comb = xr.concat(matarray, dim='time')
comb.to_netcdf("netCCMP.nc")
