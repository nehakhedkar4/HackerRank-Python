''' You are given a 2-D array with dimensions n X m.
Your task is to perform the min function over axis 1 and then find the max of that. '''

import numpy as np
n, m = map(int, input("kk : ").split())

nlis = [list(map(int, input().split("list :"))) for _ in range(n)]
narr = np.array(nlis)
print(narr,":::::::")
narr.reshape(n,m)
narr = np.min(narr, axis = 1)
print(np.max(narr))
