import xarray as xr
import netCDF4 as nc
import matplotlib.pyplot as plt

netcdf = 'datasets.nc'
ds = nc.Dataset(netcdf)
xrds = xr.open_dataset(xr.backends.NetCDF4DataStore(ds))

print(xrds['CHLOROPHYLL_A_TOTAL'].values)
xr.plot.line(xrds['CHLOROPHYLL_A_TOTAL'].dropna('DEPTH'))
plt.show()