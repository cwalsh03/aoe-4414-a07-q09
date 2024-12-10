# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  
# Written by Connor Walsh
# Other contributors: Brad Dumby
#

# import Python modules
# e.g., import math # math module
import sys # argv
import math 

# "constants"
# e.g., R_E_KM = 6378.137
# e_E = 0.081819221456
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line
c = 2.99792458e8

L_l = 10**(-1/10)
L_a = 10**(0/10)

tx_w = float('nan') 
tx_gain_db = float('nan') 
freq_hz = float('nan') 
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
     'Usage: '\
     'max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()


wavelength = c/freq_hz
tx_gain = 10**(tx_gain_db/10)
rx_gain = 10**(rx_gain_db/10)
C = tx_w * L_l * tx_gain * L_a * rx_gain * (wavelength/(4*math.pi*dist_km))**2
N = n0_j*bw_hz

r_max = bw_hz*math.log2( 1+C/N )

print(math.floor(r_max))
