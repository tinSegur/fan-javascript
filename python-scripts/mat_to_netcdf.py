import scipy.io as scio
import numpy as np
import datetime as dt
import xarray as xr
import pandas as pd

mat = scio.loadmat("Datasets/CCMP_data/CCMP_Wind_Analysis_200001.mat")

def datenums_to_datetime(datenums):
    return pd.to_datetime(datenums-719529, unit='D')

print(mat.keys())
print(mat['__version__'])

keys = [ky for ky in mat.keys() if ky[:2] != '__']
print(keys)
#for key in keys:
    #print(key + " -> " + str(mat[key]))

print(np.datetime64(datenums_to_datetime(mat['fecha'][0, 0])))

def parse_mat(matname, coords, vars, matkeys_netkeys = {}, vars_meta = {}):
    #Parse a .mat file into am xarray dataset
    #matname must be a string with the filepath 
    #coords should be a dict with the names for lon, lat and time used in the mat filee indexed by those names 
    #vars is an array with the variable names of the variables as they are in the mat file


    mat = scio.loadmat(matname)

    coordict = {}
    coordict['lon'] = xr.Variable(['lon'], [i[0] for i in mat[coords['lon']]])
    coordict['lat'] = xr.Variable(['lat'], [i[0] for i in mat[coords['lat']]])
    coordict['time'] = datenums_to_datetime(np.array([i[0] for i in mat[coords['time']]]))

    #build dict for creation of variables
    vardict = {}
    for var in vars:
        try:
            xvar = xr.Variable(['lat', 'lon'], mat[var], vars_meta[var])
        except KeyError:
            xvar = xr.Variable(['lat', 'lon'], mat[var])

        try:
            vardict[matkeys_netkeys[var]] = xvar
        except KeyError:
            vardict[var] = xvar

    return xr.Dataset(vardict, coordict)
    


def mat_to_netcdf(coords, vars, mat, netpath, matkeys_netkeys = {}, vars_meta = {}):
    #Converts .mat file into netcdf file.
    #coords must be a dict with the names for lat lon and time in the mat file indexed by those names
    #vars must be a string array with the names of the variables (as they are in the mat file)
    #mat must be a dict indexing the data contained in the mat file by the variable name (as returned by scipy.loadmat())
    #matkeys_netkeys (optional) must be a dict indexing the variables to be written to the netcdf fille indexed by their corresponding names in the mat file
    #keys_meta (optional) is a dict with the matlab variables and their associated metadata

    
    #build dict for creation of coordinates
    coordict = {}
    #lonm, latm = np.meshgrid(mat[coords['lon']], mat[coords['lat']])
    coordict['lon'] = xr.Variable(['lon'], [i[0] for i in mat[coords['lon']]])
    coordict['lat'] = xr.Variable(['lat'], [i[0] for i in mat[coords['lat']]])
    coordict['time'] = datenums_to_datetime(np.array([i[0] for i in mat[coords['time']]]))

    #build dict for creation of variables
    vardict = {}
    for var in vars:
        try:
            xvar = xr.Variable(['lat', 'lon'], mat[var], vars_meta[var])
        except KeyError:
            xvar = xr.Variable(['lat', 'lon'], mat[var])

        try:
            vardict[matkeys_netkeys[var]] = xvar
        except KeyError:
            vardict[var] = xvar
    
    #build dataset
    datanet = xr.Dataset(vardict, coordict)
    datanet.to_netcdf(netpath)



