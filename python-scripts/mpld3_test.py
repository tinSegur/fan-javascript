from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import mpld3 as d3

fig1 = plt.figure(1, figsize=[12, 4])

left = 0.07
width = 0.2
height = 0.7
bottom = 0.1
left2 = left + width + 0.05
width2 = 1-left2 - 0.05


ax1 = fig1.add_axes([left, bottom, width, height])

lt0 = -48
ln0 = -73.

delta_lt = 8
delta_ln = 6.5


lllt, urlt = (lt0 - delta_lt, lt0 + delta_lt)
llln, urln = (ln0 - delta_ln, ln0 + delta_ln)


map = Basemap(llcrnrlon=llln, llcrnrlat=lllt, urcrnrlat=urlt, urcrnrlon=urln,
             resolution='h', projection='tmerc', lat_0 = lt0, lon_0 = ln0, ax=ax1)

map.drawcoastlines(linewidth=0.2)

data = xr.open_dataset(r"C:\Users\marti\Documents\Practica FAN\Datasets\precipitacion_DJF_2000_2020_Patagonia.nc")
timeline = [str(dt)[:10] for dt in data["time"].values]
avgdata = [np.nan for dt in data["time"].values]

singlestep = data["tp"].values[0,:,:]
x = data["longitude"].values
y = data["latitude"].values

xx, yy = np.meshgrid(x, y)

level_color = np.linspace(0, 30, 5)

cnt = map.contourf(xx, yy, singlestep, extend='both', latlon= True, levels=level_color, cmap='Blues')
colorbar = map.colorbar(cnt, location='right', pad=0.2, ax=ax1)
date = str(data["time"].values[0])[:10]
ax1.set_title(date, fontsize=8)

plt.title('Precipitación fluvial en la Patagonia en meses de verano, en mm')

d3.show()
