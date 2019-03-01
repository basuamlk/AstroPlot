
"""
Created on Thu Nov 15 21:28:14 2018

"""

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import math
from matplotlib import pylab
from scipy.optimize import curve_fit
import numpy.polynomial.polynomial as poly



path = 'Input_Project2_MarsEphemeris.txt'



tp = pd.read_csv(path, sep="\s{2,}" ,chunksize=1,engine='python', encoding = "ISO-8859-1", iterator=True, error_bad_lines=False, header=None, skiprows=3)


df = pd.concat(tp, ignore_index=True)


headdf = pd.read_csv(path, sep="\n" ,chunksize=1,engine='python', encoding = "ISO-8859-1", iterator=True, error_bad_lines=False, header=None, nrows=3)


head = pd.concat(headdf, ignore_index=True)

a = head[0][0].strip().split()



b = re.split("\s{2,}", head[0][1].strip())


print(head)
print(df)

print("Apparent R.A for: " + df[0][10] + " is "+ df[1][10] + " and the declination is "+ df[2][10])#a = df[1][1]


#Part 2
def dms2dd(num):
    sign = num[0]
    num2 = num[1:].strip().split()
    dd = float(num2[0]) + float(num2[1])/60 + float(num2[2])/(60*60);
    if sign == '-':
        dd *= -1
    return dd

def hours2dec(num):
    num2 = num.strip().split()
    result = float(num2[0]) * 3600 + float(num2[1]) * 60 + float(num2[2])
    return result

df[2] = df[2].apply(lambda x: dms2dd(x))
df[1] = df[1].apply(lambda x: hours2dec(x))


size = []
for i in df[3]:
    size.append(((3.14*(3389.4)*3389.4)*float(i))/500000) #scaled by 500,000
    #print(i)

plt.scatter(df[1], df[2], s=size)

#Labes
plt.title('Retrograde of Mars')
plt.xlabel('Apparent RA')
plt.ylabel('Apparent Declination')
plt.legend()   


x = df[1].values
y = df[2].values


coefs = poly.polyfit(x, y, 4)
ffit = poly.polyval(df[1], coefs)
#plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
plt.plot(df[1], ffit)
plt.show()
