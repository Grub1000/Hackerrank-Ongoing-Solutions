import numpy

NM = list(map(int,input().split()))
numList = []
for i in range(NM[0]):
    numList.append(list(map(int,input().split())))

numpyArray = numpy.array(numList)

print(numpy.max(numpy.min(numpyArray, axis=1)))


# Task
# You are given a 2-D array with dimensions N X M.
# Your task is to perform the min function over axis 1 and then find the max of that.

# Sample Input
# 4 2
# 2 5
# 3 7
# 1 3
# 4 0

# Sample Output
# 3