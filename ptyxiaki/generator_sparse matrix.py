import numpy as np
# from scipy.sparse import random
from scipy.sparse import random

np.random.seed(10)

matrix = random(5, 5, format='csr', density=0.25)
# matrix= matrix.toarray()

print(matrix.A)
# matrix = (10-5)*matrix + 5*matrix.ceil()
print("---------------------------------------------------")
print(matrix)
# with open('output.txt', 'w') as f:
#     for item in matrix:
#         for index,inner in enumerate(item):
#             if index == len(item)-1:
#                 f.write("%s" % str(inner), )
#             else:
#                 f.write("%s\t" % str(inner), )
#         f.write("\n")

for item in matrix.A:
    print(item)
