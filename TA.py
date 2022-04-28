import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('5minutes.csv', delimiter=',')

print(my_data)

close = my_data[:,4]

print(close)

#moving_average = talib.SMA(close, timeperiod =15)

#print(moving_average)

rsi = talib.RSI(close)

print(rsi)

