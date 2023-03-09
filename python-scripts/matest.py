import scipy.io as scio
import numpy as np
import datetime as dt
import xarray as xr

mat = scio.loadmat("Datasets/CCMP_data/CCMP_Wind_Analysis_200001.mat")

def datenum_to_date(datenum):
    return dt.datetime.fromordinal(int(datenum)) + dt.timedelta(days=datenum%1) - dt.timedelta(days=366)

print(mat.keys())
print(mat['__version__'])

keys = [ky for ky in mat.keys() if ky[:2] != '__']
print(keys)
print(mat['latitud'].shape)
print(mat['longitud'].shape)
latm, lonm  = np.meshgrid(mat['latitud'], mat['longitud'])
print(latm)
print(lonm)

print(np.datetime64(datenum_to_date(mat['fecha'][0, 0])))