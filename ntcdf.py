import xarray as xr
import netCDF4 as nc

netcdf = 'CTD_station_P1_NLEG01-1_-_Nansen_Legacy_Cruise_-_2021_Joint_Cruise_2-1.nc'
ds = nc.Dataset(netcdf)
xrds = xr.open_dataset(xr.backends.NetCDF4DataStore(ds))

dimensions=xrds.dims
coordinate=xrds.coords
databar=xrds.data_vars['TEMP'].values
print(dimensions,coordinate,databar)
