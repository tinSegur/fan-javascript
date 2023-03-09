import xarray as xr
import json as js


data= xr.open_dataset("Datasets\precipitacion_DJF_2000_2020_Patagonia.nc")

tp = data["tp"].values[0,:,:]
lat = data["latitude"].values
lon = data["longitude"].values


vardict = {
    "tp":tp.tolist(),
    "lat":lat.tolist(),
    "lon":lon.tolist()

}

obj = js.dumps(vardict)

with open("sample.json", "w") as file:
    file.write(obj)

