import xarray as xr
import json as js
from parsing_functions import filter_nans

ccmp = xr.open_dataset("C:/Users/marti/Documents/Practica FAN/netCCMP.nc")

year_mean = ccmp.groupby("time.year").mean(dim='time', skipna=True, keep_attrs=True)
print(year_mean)

u_data = year_mean['u']
v_data = year_mean['v']

u_meta = {
    'long_name':'Yearly average zonal wind speed',
    'units':'Metres per second',
    'shape':u_data.shape,
    'lat_interval':{
        'start':float(u_data['lat'].values[0]),
        'end':float(u_data['lat'].values[-1])
    },
    'lon_interval':{
        'start':float(u_data['lon'].values[0]),
        'end':float(u_data['lon'].values[-1])
    },
    'year_interval':year_mean['year'].values.tolist()
}

with open(r'C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\u\u_meta.json', 'w') as u_meta_file:
    u_obj = js.dumps(u_meta)
    u_meta_file.write(u_obj)


v_meta = {
    'long_name':'Yearly average meridional wind speed',
    'units':'Metres per second',
    'shape':v_data.shape,
    'lat_interval':{
        'start':float(v_data['lat'].values[0]),
        'end':float(v_data['lat'].values[-1])
    },
    'lon_interval':{
        'start':float(v_data['lon'].values[0]),
        'end':float(v_data['lon'].values[-1])
    }
}

with open(r'C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\v\v_meta.json', 'w') as v_meta_file:
    v_obj = js.dumps(v_meta)
    v_meta_file.write(v_obj)




u_dicts = []
v_dicts = []
for year in year_mean['year'].values:
    udata_dict = {
        'data':filter_nans(u_data[year-2000].values.flatten().tolist()),
        'lat':u_data['lat'].values.tolist(),
        'lon':u_data['lon'].values.tolist(),
        'year':int(year)
    }
    u_dicts.append(udata_dict)
    with open(r"C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\u\u_data\u-mean-"+str(year)+".json", 'w') as year_json:
        udata_obj = js.dumps(udata_dict)
        year_json.write(udata_obj)

    vdata_dict = {
        'data':filter_nans(v_data[year-2000].values.flatten().tolist()),
        'lat':v_data['lat'].values.tolist(),
        'lon':v_data['lon'].values.tolist(),
        'year':int(year)
    }
    v_dicts.append(vdata_dict)
    with open(r"C:\Users\marti\Documents\Practica FAN\fan-javascript\vis_data\v\v_data\v-mean-"+str(year)+".json", 'w') as year_json:
        vdata_obj = js.dumps(vdata_dict)
        year_json.write(vdata_obj)
