# 导入模块

import numpy as np

  

# 创建数组

arr=np.array([1,2,3,4,5])

  

#创建二维数组

arr1=np.array([[1,2,3,4,5],[1,2,3,4,5]])

  

#打印数组

print(arr)

  

# 生成数组维度

print("数组形状",arr1.shape)

  

#索引和切片

print(arr[0])

print(arr[0:3])

# 二维数组切片先在第一维度上面切片，再切第二维

print(arr1[0:3])

  

# 运算，等于对应位置上的相加

print(np.array([1,2,3])+np.array([1,2,3]))

print(np.array([1,2,3])*np.array([1,2,3]))

# 相乘运算只是对应位置上的数相乘

  

# 数组形状操作

arr=np.array([[1,2,2],[1,2,3],[2,3,4],[4,2,6]])

print(arr.shape)

new_arr=arr.reshape(3,4)

print(new_arr)

  

#数组的转制操作

new_arrT=new_arr.transpose()

print(new_arrT)

  

# 线性代数

arr1=np.array([1,2,3])

arr2=np.array([4,5,6])

# 数组的点乘

arr1_dot_arr2=np.dot(arr1,arr2)

print(arr1_dot_arr2)

  

#计算数组的平均值

print("数组的平均值",arr1.mean())

print("数组的最大值",arr1.max())

print("数组的最小值",arr1.min())

print("数组的标准差",arr1.std())  

print("数组的排序",np.sort(arr1))

# 把数组缩减成一行

arr.reshape(-1)

# 筛选

print(arr[(arr>10)&(arr>5)])

  

# 保存和导入

np.save("arr",arr)

arr=np.load("arr.npy")

print(arr)