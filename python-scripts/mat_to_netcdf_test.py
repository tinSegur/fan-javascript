from mat_to_netcdf import mat_to_netcdf
import numpy as np
import scipy.io as scio

mat = scio.loadmat("Datasets/CCMP_data/CCMP_Wind_Analysis_200001.mat")

#first test

temp = 15 + 8 * np.random.randn(2, 2, 3)

precip = 10 * np.random.rand(2, 2, 3)

lon = [-99.83, -99.32]

lat = [42.25, 42.21]

#pseudo mat file

testmat = {'lon':lon, 'lat':lat, 'temp':temp, 'precip':precip, 'time':[719530, 719531, 719532]}
coords = {'lon':'lon', 'lat':'lat', 'time':'time'}
vars = ['temp', 'precip']

#mat_to_netcdf(coords, vars, testmat, "testnet.nc")

#second test

temp = 15 + 8*np.random.randn(1000, 1000, 1)
precip = 10*np.random.randn(1000, 1000, 1)

lon = np.linspace(0, 100, 1000)
lat = np.linspace(0, 100, 1000)


testmat = {'lon':lon, 'lat':lat, 'temp':temp, 'precip':precip, 'time':[719530]}
#mat_to_netcdf(coords, vars, testmat, "testnet2.nc")

#third test 

coords = {'lon':'longitud', 'lat':'latitud', 'time':'fecha'}
vars = ['u', 'v']

mat_to_netcdf(coords, vars, mat, "testnet3.nc")