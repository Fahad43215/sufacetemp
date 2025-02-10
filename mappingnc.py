import xarray as xr
import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

netcdf = 'https://www.ncei.noaa.gov/thredds/dodsC/noaa-global-temp-v5/NOAAGlobalTemp_v5.0.0_gridded_s188001_e202212_c20230108T133308.nc'
ds = nc.Dataset(netcdf)
xrds = xr.open_dataset(xr.backends.NetCDF4DataStore(ds))
print(xrds['anom'])
desired_date='2022-12-01'
data_for_desired_date=xrds.sel(time=desired_date)
print('data_for_desired_date')


plt.figure(figsize=(10,5))
ax=plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

data_for_desired_date['anom'].plot()
plt.show()
