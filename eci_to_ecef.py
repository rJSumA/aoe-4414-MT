# eci_to_ecef.py
# Access Python through CMD: cd Desktop\Phyton
# Clear Sreen on CMD: cls
#
# Usage: eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
#  Example: python3 eci_to_ecef.py 2054 4 29 11 29 3.3 5870.038832 3389.068500 3838.027968
#  eci_to_ecef.py 2024 9 29 16 0 0.0 -5561.874359687406 1434.499390824219 3846.747642588853
#  Output: 
#      6778.1369996526555
#      -0.028633407850520598
#      3838.027968     
#           

# Parameters:
#  (year, month, day, hour, minute, second) in UTCG
#  (x,y,z) location in ECI
#  ...
# Output:
#  (x,y,z) location in ECEF
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
w = 7.292115 * (10**-5)

# helper functions
def calc_denom (E_E,lat_rad):
    return math.sqrt(1.0-E_E**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments

# Time variables
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0.0

#ECI coordinates
eci_x_km = 0.0
eci_y_km = 0.0 
eci_z_km = 0.0

# parse script arguments
# How many arguments are passed to python -- 9 arguments pass 10
# Converts string to float

if len(sys.argv)==10:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    eci_x_km = float(sys.argv[7])
    eci_y_km = float(sys.argv[8])
    eci_z_km =  float(sys.argv[9])
    
else:
   print(\
    'Usage: '\
    'python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
   )
   exit()

#======================================
#--Fractional JD Script----------------------------------------------

#JDt1 = 1461 * (year + 4800 + (month-14) // 12) // 4
#JDt2 = 367 * (month - 2 - (month-14) // 12 * 12) // 12
#JDt3 = -3 * ((year + 4900 + (month-14) // 12) / 100) // 4

JD = \
day-32075.0 \
+int(1461.0*(year+4800.0+int((month-14.0)/12.0))/4.0) \
+int(367.0*(month-2.0-int((month-14.0)/12.0)*12.0)/12.0) \
-int(3.0*(int((year+4900.0+int((month-14.0)/12.0))/100.0))/4.0)

JDmid = JD - 0.5
Dfrac = (second + 60*(minute+60*hour))/86400

jd_frac = JDmid + Dfrac
#jd_frac = 2471386.978510

#--------------------------------------------------------------------

Tut1 = (jd_frac - 2451545.0) / 36525
GMST_sec = 67310.54841+((876600*60*60)+8640184.812866)*Tut1 + (0.093104*(Tut1**2))-(6.2*(10**-6))*(Tut1**3)
GMST_rad = math.fmod(GMST_sec,86400) * w + 2*math.pi
GMST_rad = math.fmod(GMST_rad, 2*math.pi)

#GMST_rad = 0.523603

ecef_x_km = eci_x_km*math.cos(-GMST_rad) - eci_y_km*math.sin(-GMST_rad)
ecef_y_km = eci_x_km*math.sin(-GMST_rad) + eci_y_km*math.cos(-GMST_rad)
ecef_z_km = eci_z_km

#======================================
print(GMST_rad)
print(jd_frac)
print('')
print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
