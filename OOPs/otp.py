#Generate 6 digit random number which can be used a OTP
from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
print(randrange(100000, 999999))

#%%
otp = ''
for i in range(6):
    otp = otp + str(randint(0,9))
