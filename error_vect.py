# error_vect.py
#
# Usage: python3 error_vect.py 595.4532282387947 -5712.938247174647 3846.747289639383
#                              595.4507082220091 -5712.939116540728 3846.747642588853
#  Finds error magnitude from two vectors 
# Parameters:
#  v1_(x,y,z): Vector 1 in x,y,z
#  v2_(x,y,z): Vector 2 in x,y,z -- must be same coordinate system
#  ...
# Output:
#  Error vector magnitude
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

def vector_mag (v_x,v_y,v_z):
    return math.sqrt(v_x**2 + v_y**2 + v_z**2)

if len(sys.argv)==7:
    v1_x = float(sys.argv[1])
    v1_y = float(sys.argv[2])
    v1_z = float(sys.argv[3])
    v2_x = float(sys.argv[4])
    v2_y = float(sys.argv[5])
    v2_z = float(sys.argv[6])
    
else:
   print(\
    'Usage: '\
    'python3 error_vect.py v1_x v1_y v1_z v2_x v2_y v2_z'\
   )
   exit()
#================================

v1_mag = vector_mag(v1_x,v1_y,v1_z)
v2_mag = vector_mag(v2_x,v2_y,v2_z)

error_mag = abs(v1_mag-v2_mag)

print(error_mag)