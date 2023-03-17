''' You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array. '''

import numpy
lst = list(map(int, input("").split()))  
arr = numpy.array(lst)
print(arr.reshape(3,3))