import numpy as np

# List Data
ldata = [1,2,3,4,5]

# Tuple Data
tdata = (1,2,3,4,5)

# Creating rank 1 array from list
print("----------------------------------------------------------------")
print("Creating rank 1 array from list")
lar1 = np.array(ldata)
print(lar1)
print(lar1.dtype)

# Creating rank 2 array from list
print("----------------------------------------------------------------")
print("Creating rank 2 array from list")
lar2 = np.array([ldata,ldata])
print(lar2)
print(lar2.dtype)

# Accessing array index
print("----------------------------------------------------------------")
print("Accessing array index")
ar3 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("Accessing all elements",end=' : ')
for i in range(len(ar3)):
    for j in range(len(ar3[i])):
        print(ar3[i,j],end=' ')
print()
print("Accessing particular elements at indexes (0,1), (2,0), (3,2):",ar3[[0,2,3],[1,0,2]])

# Performing basic operations on array
print("----------------------------------------------------------------")
ar4 = np.array([1,2,3,4,5])
ar5 = np.array([5,4,3,2,1])
print("Performing basic operations on arrays:",ar4,ar5)
print("Adding 1 to every elements:",ar4+1)
print("Subtracting 1 to every elements:",ar4-1)
print("Sum of all array elements:",ar4.sum())
print("Adding arrays",ar4,"and",ar5,":",ar4+ar5)

# Stacking numpy arrays
print("----------------------------------------------------------------")
ar6 = np.array([[1,10],[2,9]])
ar7 = np.array([[3,8],[4,7]])
print("Stacking numpy arrays:",ar6,ar7,sep='\n')
print("Vertical stacking:",np.vstack((ar6,ar7)))
print("Horizontal stacking:",np.hstack((ar6,ar7)))
print("Column stacking:",np.column_stack((ar6,ar7)))
print("Concatenate 2 arrays at 2nd axis:",np.concatenate((ar6,ar7),1))

# Splitting numpy arrays
print("----------------------------------------------------------------")
ar8 = np.array([[1,3,5,7,9,11],[0,2,4,6,8,10]])
print("Splitting numpy arrays:",ar8,sep='\n')
print("**Splitting parts should give equal elements on split in arrays otherwise would throw exception**")
print("Horizontal splitting into 2 parts:",np.hsplit(ar8,2),sep='\n')
print("Vertical splitting into 2 parts:",np.vsplit(ar8,2),sep='\n')
