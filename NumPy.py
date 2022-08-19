import numpy as np
import sys


#a = np.array([1,2,3] , dtype='int64')
#b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
#print(b.ndim)  #2
#print(a.ndim)   #1
#print(a.shape)      #3,
#print(b.shape)     #2,3
#c = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(c.ndim)       #2
#print(c.shape)  #3,3
#print(c.dtype)      #int 32  standart
#print(b.itemsize)       #4 bytes

#print(a.size)
#print(a.itemsize)
#print(a.size * a.itemsize) #24   #= print(a.nbytes)
#print(a.nbytes)            #24
#print(c.nbytes)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])        #[r,c] ->[[0,1]]  -> [[0,1,2,3,4,5,6],[0,1,2,3,4,5,6]]

#print(a.shape)
#print(a[-2,-1])  #=(a[0,6])

#print(a[0, :])      #[1 2 3 4 5 6 7]
#print(a[ :,3])      # [ 4 11]
#print(a[ :,2:5])        #[[ 3  4  5]
                         # [10 11 12]]
#print(a[0,0:6:2])       #[1 3 5]
#a[1,5] = 20         #[[ 1  2  3  4  5  6  7]
#print(a)            #[ 8  9 10 11 12 20 14]]
a[ :,-1] = [1,2]
print(a)