"""### IMPORT SINGLE MODULE
import random #makes random module usable

###CALL MODULE FX
random.randint (1,10)  #randint returns random value of 1-10
6

### IMPORT MULTIPLE MODULES
import random, sys, os, math 

### IMPORTS MODULE & AVOIDS CALL to MODULE.
from random import * #no longer need random.to call random module fx
randint(1,10)
4
randint(1,10)
3
"""

import sys
print('Hello')
sys.exit() #causes exit of program causing below to never print
print('Goodbye')

#THIRD PARTY MODULES - use PIP from command line appendix A