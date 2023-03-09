import xarray as xr
import json as js

def generate_json(netcdf):
    #Create a dict formatted for parsing into json

    data = xr.open_dataset(netcdf)

    var_vals = {}
    for var in data.variables:
        if var in data.dims:
            continue
        
        

