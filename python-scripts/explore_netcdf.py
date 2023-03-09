import xarray as xr
import sys

if __name__ == '__main__':
    data = xr.open_dataset(sys.argv[1])
    print(data.values)