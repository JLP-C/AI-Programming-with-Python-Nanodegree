# Calculate the average of 23, 32 and 64

# Mode1: direct
print ((23+32+64)/3)

# Mode4: Con operaciones de lista
list = [23,32,64]
print (sum(list)/len(list))

# Mode3: Statistics (libreria preinstalada con python 3.9.1)
from statistics import mean
print (mean([23,32,64]))

# Mode2: Numpy (librería que hay que instalar aparte)
from Numpy import mean
print (mean([23,32,64]))
