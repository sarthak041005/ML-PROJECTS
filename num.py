#numpy
#WORKING ON SMALL DATASET 
# #Average
# tempratures=[12,23,14,34,21]
# total=0
# for temp in tempratures:
#     total+=temp
# average=total/len(tempratures)
# print(average) #SLOW AF

#First basic program without the use of loops!
# import numpy as np
# temprature=np.array([12,23,14,34,21])
# average=np.mean(temprature)
# print(average) #FAST AF
# differnece between python list and numpy array:-
# python_list = [1,2,3,4,5]
# print(python_list)

# import numpy as np
# num_array = np.array([1,2,3,4,5])
# print(num_array)
# two dimensonal array:
# num_array = ([1,2,3],
#              [4,5,6],
#              [7,8,9])
# print(num_array)
# multi dimensonal array:
# matrix:
# import numpy as np
# matrix = np.array([[1,2,3],
#                   [4,5,6],
#                   [7,8,9]])
# print(matrix)
# zeros matrix, used for reference in future values
# import numpy as np
# zeros_array = np.zeros([3,3])
# print(zeros_array)
# random values
# import numpy as np
# num_array= np.full([3,3], 5)
# print(num_array)
# creating sequences of numbers in numpy
# arange(start, stop, step)
# import numpy as np
# arr = np.arange(1,20,2)
# print(arr)
# creating identity matrices:
# eye(size)
# import numpy as np
# identity_matrix = np.eye(4)
# print(identity_matrix)
# array properties:
# SHAPE:
# import numpy as np

# arr_2d = np.array([[1,2,3],
#           [4,5,6]])
# print(arr_2d.shape)
# SIZE: TOTAL NUMBER OF ELEMENTS IN AN ARRAY
# import numpy as np
# arr = np.array([[10,20,30], [40,50,60]])
# print(arr.size)
#ndim
# import numpy as np
# arr_1d = np.array([1,2,3])
# arr_2d = np.array([[1,2,3], [4,5,6]])
# arr_3d = np.array([[[1,2], [3,4], [5,6], [7,8]]])
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)
#dtype:
# import numpy as np
# arr = np.array([1,2,3,4.8,7])
# print(arr.dtype)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr.dtype)
#astype:
# import numpy as np
# arr=np.array([1.2,2.3,3.4])
# print(arr.dtype)
# int_arr= arr.astype(int)
# print(int_arr)
# print(int_arr.dtype)
#mathematical operations on numpy arrays:
# import numpy as np
# arr = np.array([3,4,5])
# print(arr+4)
# print(arr*5)
# print(arr**2)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# import numpy as np
# zeroes = np.zeros([3,3])
# print(zeroes)
# import numpy as np
# ones = np.ones((4,4))
# print(ones)
# import numpy as np
# filled = np.full((3,3), 5)
# print(filled)
# import numpy as np
# arr = np.arange(1,20,3)
# print(arr) 
# import numpy as np
# identity_matrix = np.eye(3)
# print(identity_matrix) 
# import numpy as np
# arr= np.array([[1,2,3], 
#               [4,5,6]])
# print(arr)
# print(arr.shape)
# import numpy as np
# arrr=np.array([[1,2,3], [4,5,6]])
# print(arrr.size)
# import numpy as np
# arr_1d = np.array([1,2,3])
# arr_2d=np.array([[1,2,3], [4,5,6]])
# arr_3d=np.array([[[1,2,3], [4,5,6], [7,8,9]]])
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)
# import numpy as np
# arr=np.array([1,2.4,3,5.7])
# print(arr.dtype)
# import numpy as np 
# arr=np.array([1,2,3.4,5])
# print(arr.dtype)
# arrr=arr.astype(float)
# print(arrr)
# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr%5)
# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.std(arr))
# print(np.var(arr))
# import numpy as np
# arr=np.array([7,6,7,6])
# rev = np.flip(arr)
# print(rev)
# indexing
# import numpy as np
# arr= np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[2])
# print(arr[-2])
# import numpy as np
# arr= np.array([10,20,30,40,50,60,70,80,90,100])
# print(arr[0:10])
# print(arr[1:4])
# print(arr[::3])
# print(arr[1:6:2])
# print(arr[::-1])
# fancy indexing 
# import numpy as np
# arr = np.array([10,20,30,40,50,60])
# print(arr[[0,3,5]])
# print(arr[[-1,-4,3]])
# boolean masking
# import numpy as np
# arr= np.array([10,20,30,40,50,60])
# print(arr[arr>25])
# reshaping
# import numpy as np
# arr=np.array([1,2,3,4,5,6])
# reshaped_arr=arr.reshape(2,3)
# print(reshaped_arr)
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr.reshape(2,3))
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# arrr=arr.reshape(4,4)
# print(arrr)
# import numpy as np
# arr = np.array([[1,2,3], [4,5,6]])
# arr2 = arr.ravel()
# print(arr2)
# print(arr)
# import numpy as np
# arr =np.array([10,20,30,40,50,60])
# print(arr)
# arr2=np.insert(arr, 2, 69)
# print(arr2)
# import numpy as np
# arr = np.array([[3,4], [5,6]])
# print(arr)
# arrr=np.insert(arr, 0, [1,2], axis=1)
# print(arrr)
# import numpy as np
# arr=([10],[20],[30],[40])
# print(arr)
# arrr=np.append(arr,[[50],[60]])
# print(arrr)
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# arr=np.concatenate((arr1,arr2))
# print(arr)
# import numpy as np
# arr= np.array([10,20,30,40])
# arr1= np.delete(arr, 3)
# print(arr1) 
# import numpy as np
# arr=([[10,20], [30,40]])
# arr1= np.delete(arr,0,axis=0)
# print(arr1)
# import numpy as np
# arr1=np.array([10,20,30])
# arr2=np.array([40,50,60])
# arrr= np.vstack((arr1,arr2))
# arrrr= np.hstack((arr1,arr2))
# print(arrr)
# print(arrrr)
# import numpy as np
# arr=np.array([10,20,30,40,50,60])
# arrr=np.split(arr,3)
# print(arrr)
# brodcasting
# import numpy as np
# prices = np.array(input("enter the items"))
# discount=int(input("enter the discount"))
# fp = prices- (prices*discount/100)
# print(fp)
# import numpy as np
# prices=(input("enter the prices"))
# prices=np.array(prices.split())
# discount= int(input("enter the discount"))
# final_prices=prices-(prices*discount/100)
# print(final_prices) 
# import numpy as np
# arr= np.array([10,20,30])
# result= arr+5
# print(result)
# import numpy as np
# matrix=np.array([[10,20,30], [40,50,60]])
# vector=np.array([70,80])
# result=matrix+vector
# print(result, type(result))
# import numpy as np
# arr1= np.array([1,2,3])
# arr2=np.array([4,5])
# arr3=np.append(arr2, [6])
# array=arr1+arr3
# print(array)
# import numpy as np
# arr1=np.array([1,2,3])
# result=arr1* np.array([4,5,6])
# print(result)
# nan
# import numpy as np
# arr=([1,2, np.nan,4, np.nan, 6])
# print(np.isnan(arr))
# import numpy as np
# arr=([1,2,np.nan,4,np.nan,6])
# arr1= np.nan_to_num(arr,nan=3)
# print(arr1)
# is inf
# import numpy as np
# arr=np.array([1,2,np.inf, 4,-np.inf, 6])
# arr1= np.isinf(arr)
# print(arr1)
# or we can also write
# import numpy as np
# arr=np.array([1,2,3,np.inf,5])
# print(np.isinf(arr))
# import numpy as np
# arr= np.array([1,2,3,np.inf, -np.inf])
# arr1= np.nan_to_num(arr, posinf=1000, neginf=-1000)
# print(arr1)
# import numpy as np
# arr= np.array([1,2,3,np.inf, -np.inf])
# print(np.nan_to_num(arr, posinf=1000, neginf=-1000))
