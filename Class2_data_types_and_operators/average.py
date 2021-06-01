# Calculate the average of 23, 32 and 64

# Mode1: direct
print ((23+32+64)/3)

# Mode2: Numpy
from Numpy import mean
print (mean([23,32,64]))

# Mode3: Statistics
from statistics import mean
print (mean([23,32,64]))

# Mode4: Con operaciones de lista
list = [23,32,64]
print (sum(list)/len(list))
