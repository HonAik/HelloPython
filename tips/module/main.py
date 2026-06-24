#how to import function or variable from other files:
#1. import filename: use filename.funcitonname
#2. from filename import functionname : use functioname

# import funciton1 as f1
# import funciton1 as f1

# f1.outline()

#if you want import all, either use * or __all__

# __all__ = ["outline","NAME"],put this in the file that has these function
from funciton1 import *

outline()
print(NAME)
# print(NUM) Error because all are not inside the all