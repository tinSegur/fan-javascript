import xarray as xr
import json as js
import numpy as np
import os
from datetime import datetime, timedelta
from parsing_functions import filter_nans

oisst_array = []
direct = os.fsencode("C:/Users/marti/Documents/Practica FAN/Datasets/OISST - FAN/")
for file in os.listdir(direct):
    flname = os.fsencode(file)
    decname = os.fsdecode(flname)
    if decname.endswith('.nc'):
        oisst_array.append(xr.open_dataset("Datasets/OISST - FAN/" + decname)["sst"].loc[:, :, -60.0:-35.0, -95.0+360:-55.0+360])

#for i in range(10):
#    print(oisst_array[-i-1]["time"].values)

big_comb = xr.concat(oisst_array, dim='time')
big_comb = big_comb.groupby('time.year').mean(dim='time', keep_attrs=True)
print(big_comb)


attrs_dict = big_comb.attrs
attrs_dict['valid_min'] = int(attrs_dict['valid_min'])
attrs_dict['valid_max'] = int(attrs_dict['valid_max'])

metadict = {**attrs_dict,
    'shape':big_comb.shape,
    "lat_interval":{
        "start":float(big_comb["lat"].values[0]),
        "end":float(big_comb["lat"].values[-1])
        }, 
    "lon_interval":{
        "start":float(big_comb["lon"].values[0]), 
        "end":float(big_comb["lon"].values[-1])
        },
    'year_interval':big_comb['year'].values.tolist()
}

vardicts = []
for year in big_comb["year"].values:
    year_data = big_comb.loc[year, :, :, :]
    vardict = {
        "data":filter_nans(year_data.values.flatten().tolist()),
        "lat":big_comb["lat"].values.tolist(),
        "lon":big_comb["lon"].values.tolist(),
        "year":int(year)
    }
    vardicts.append(vardict)

with open("C:\\Users\\marti\\Documents\\Practica FAN\\fan-javascript\\vis_data\\sst\\sst_meta.json", 'w') as meta_file:
    metadict["valid_min"] = int(metadict["valid_min"])
    metadict["valid_max"] = int(metadict["valid_max"])
    obj = js.dumps(metadict)
    meta_file.write(obj)

for data in vardicts:
    with open("C:\\Users\\marti\\Documents\\Practica FAN\\fan-javascript\\vis_data\\sst\\sst_data\\sst-mean-"+str(data["year"])+".json", 'w') as data_file:
        obj = js.dumps(data)
        data_file.write(obj)

#yearly_means = []
#for i in range(20):
#    print(i)
#    daily_data = oisst_array[i*365:(i+1)*365]
#    daily_data = [dts["sst"][dict(lat=slice(-60, -35), lon=slice(-95+360, -55+360))] for dts in daily_data]
#    comb = xr.concat(daily_data, dim='time')
#    comb_mean = comb.mean(dim='time', keep_attrs=True)
#    yearly_means.append(comb_mean)



    