import xarray as xr
import json as js
import numpy as np
from parsing_functions import filter_nans

precipitation = xr.open_dataset(r"C:\Users\marti\Documents\Practica FAN\Datasets\precipitacion_DJF_2000_2020_Patagonia.nc")

yearly_means = precipitation.groupby("time.year").mean(dim='time', skipna=True, keep_attrs=True)
tp_data = yearly_means['tp']
print(tp_data)

tp_meta = {
    **tp_data.attrs,
    'shape':tp_data.shape,
    'lat_interval':{
        'start':float(tp_data['latitude'].values[0]),
        'end':float(tp_data['latitude'].values[-1])
    },
    'lon_interval':{
        'start':float(tp_data['longitude'].values[0]),
        'end':float(tp_data['longitude'].values[-1])
    },
    'year_interval':yearly_means['year'].values.tolist()
}

for key in tp_meta.keys():
    if isinstance(tp_meta[key], np.int16):
        tp_meta[key] = int(tp_meta[key])
    if isinstance(tp_meta[key], np.float64) or isinstance(tp_meta[key], np.float32):
        tp_meta[key] = float(tp_meta[key])
print(tp_meta)

with open(r'C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\tp\tp_meta.json', 'w') as meta_json:
    meta_obj = js.dumps(tp_meta)
    meta_json.write(meta_obj)

for year in tp_data['year'].values:
    year_data = tp_data.loc[year, :, :]
    data_dict = {
        'data':filter_nans(year_data.values.flatten().tolist()),
        'lat':year_data['latitude'].values.tolist(),
        'lon':year_data['longitude'].values.tolist(),
        'year':int(year)
    }
    
    with open(r'C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\tp\tp_data\tp-mean-'+str(year)+'.json', 'w') as data_file:
        data_obj = js.dumps(data_dict)
        data_file.write(data_obj)

