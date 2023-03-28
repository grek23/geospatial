from netCDF4 import Dataset
import numpy as np

f = Dataset("/Users/grekrichmond/Downloads/precip.V1.0.2012.nc")

# print(f.variables)
print("Climate Data")
print(f.variables)
print(f.variables['precip'])

preciper = f.variables['precip'][:, :, :]

print(f"type of preciper = {type(preciper)}")
print(f"preciper[0] = {preciper[0][0][0]}")

print('The maximum value is', np.max(preciper),
      f.variables['precip'].units)

print('The minimum value is', np.min(preciper),
      f.variables['precip'].units)

for name in f.variables:
    print(name)

longe = f.variables['lon'][:]
latter = f.variables['lat'][:]
rain = f.variables['precip'][:]
tm = f.variables['time'][:]

# print(f"rain = {rain[0]}")


print(f"lat = {latter}")
print()
print(f"long = {longe}")
print()
print(f"time = {tm}")
print()
print(f"rain = {rain[5][:][5]}")
print()
