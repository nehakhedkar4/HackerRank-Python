# import numpy
# n,m = map(int, input("enter n x m").split())
# lst = []
# for i in range(n):
#     for j in range(m):
#         lst.append(input(""))
#         arr = numpy.array(lst)
# print(arr,"+++++++++++")
# print(arr.reshape(n,m))
# arr = arr.reshape(n,m)
# print(arr,"*************")
# print(numpy.transpose(arr),"-------------------transpose")
# print(arr.flatten(),"-------------------flatten")

''' You are given a n X m integer array matrix with space separated elements (n = rows and m = columns).
Your task is to print the transpose and flatten results. '''

import numpy

n,m=map(int,input().split())

lista=[list(map(int,input().split())) for i in range(n)]
a=numpy.array(lista)

print(numpy.transpose(a))
print(a.flatten())



# 2 2
# 1 2
# 3 4