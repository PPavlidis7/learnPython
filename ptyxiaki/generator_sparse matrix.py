import numpy as np
# from scipy.sparse import random
import scipy.sparse as x
np.random.seed(2)

matrix = x.random(10, 10, dtype=int, density=0.25)
print(matrix)
matrix = matrix.toarray()


with open('output.txt', 'w') as f:
    for item in matrix:
        for index,inner in enumerate(item):
            if index == len(item)-1:
                f.write("%s" % str(inner), )
            else:
                f.write("%s\t" % str(inner), )
        f.write("\n")

