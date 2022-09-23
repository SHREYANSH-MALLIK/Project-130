import pandas as pd
import csv

df = pd.read_csv("main.csv")
print(df.shape)

del df['pl_orbpererr1']
del df['pl_orbpererr2']

print(df.shape)

print(list(df))

df = df.rename({
    'pl_hostname' : 'solar_system_name',
    'pl_discmethod' : 'planet_discovery_method',
    'pl_orbincl' : 'planet_orbital_inclination',
    'pl_dens' : 'planet_density',
    'ra_str' : 'right_ascension',
    'dec_str' : 'declination',
    'st_teff' : 'host_temperature',
    'st_mass' : 'host_mass',
    'st_rad' : 'host_radius'
},axis = "columns")

print(list(df))

df.to_csv("main.csv")