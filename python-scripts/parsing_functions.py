import xarray as xr
import numpy as np

def year_data_dict(dataArr, year):
    # Generate a json parsable data dict for the specified variable in the data array for the given year
    return {
        'data':map(lambda x: x if (x != np.nan) else 'null', dataArr.values.tolist()),
        'lat':dataArr['lat'].values.tolist(),
        'lon':dataArr['lon'].values.tolist(),
        'year':int(year)
        }

def filter_nans(arr):
    return list(map(lambda x: x if not (np.isnan(x)) else 'null', arr))