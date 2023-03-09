from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import mpld3 as d3

fig = plt.figure(1)

data = xr.open_dataset(r"C:\Users\marti\Documents\Practica FAN\Datasets\precipitacion_DJF_2000_2020_Patagonia.nc")
timeline = [str(dt)[:10] for dt in data["time"].values]
avgdata = []

i = 0
for dt in data["time"].values:
    avgdata.append(data["tp"].values[i,:,:].mean())
    i += 1

plt.plot(timeline, avgdata)

d3.show()
