# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  Determines the output shape and operation count of a convolution layer
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
#
# Output:
#  Prints the output channel count, output height count, output width count, # of + 
#  performed, # of x performed, # of / performed
#
# Written by Elise Turka
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
c_in = float('nan') 
n_wv = float('nan')

# parse script arguments
if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   ' python3 conv_ops.py c_in n_wv'\
  )
  exit()


#calculating
h_out = 1
w_out = 1
muls = n_wv*c_in
adds = n_wv*c_in
c_out = n_wv
divs = 0


#printing output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))