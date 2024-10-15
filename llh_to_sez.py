# llh_to_sez.py
# Access Python through CMD: cd Desktop\Phyton
# Clear Sreen on CMD: cls
#
# Usage: python3 llh_to_sez.py lat_deg lon_deg dist_km azi_deg ele_deg
#  Example: python3 llh_to_sez.py 30.484009 -86.492698 716.392334838915 30.093824612611 47.029884151878
#  
# Parameters:
#  lat_deg: lattitude in degrees
#  long_deg: longtitude in degrees
#  dist_km: distance in km
#  azi_deg: azimuth angle in degrees
#  ele_deg: elevation angle in degrees
#  ...
# Output:
#  Print SEZ position (r_S, r_E, r_Z)
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.1363
E_E = 0.081819221456

# helper functions
def calc_denom (E_E,lat_rad):
    return math.sqrt(1.0-E_E**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
#lat_deg = float('nan') #Latitude in degrees
#lon_deg = float('nan') #Longtitude in degrees
dist_km = 0.0 #slant height 
azi_deg = float('nan')
ele_deg = float('nan')

# parse script arguments
# How many arguments are passed to python -- 5 arguments pass 6
# Converts string to float

if len(sys.argv)==4:
    #lat_deg = float(sys.argv[1])
    #lon_deg = float(sys.argv[2])
    azi_deg = float(sys.argv[1])
    ele_deg = float(sys.argv[2])
    dist_km = float(sys.argv[3])
    
else:
   print(\
    'Usage: '\
    'python3 llh_to_sez.py azi_deg ele_deg dist_km'\
   )
   exit()

#======================================

#lat_rad = lat_deg * math.pi / 180.0
#lon_rad = lon_deg * math.pi / 180.0
ele_rad = ele_deg * math.pi / 180.0
azi_rad = azi_deg * math.pi / 180.0
#denom = calc_denom(E_E,lat_rad)

#C_E = R_E_KM/denom
#S_E = (R_E_KM*(1.0-E_E**2.0)) / denom

#r_x_km = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
#r_y_km = (C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
#r_z_km = (S_E+hae_km)*math.sin(lat_rad)
#r_km = math.sqrt(r_x_km**2 + r_y_km**2 + r_z_km**2)

r_s_km = (dist_km)*math.cos(ele_rad)*-math.cos(azi_rad)
r_e_km = (dist_km)*math.cos(ele_rad)*math.sin(azi_rad)
r_z_km = (dist_km)*math.sin(ele_rad)

print(r_s_km)
print(r_e_km)
print(r_z_km)

