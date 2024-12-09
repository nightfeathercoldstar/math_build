# 随机生成一个4*4的数组，保留10以内的数，并且计算出所有元素的和
import numpy as np
#np.random.seed(num)固定随机种子
print(np.random.rand())#0-1之间
print(np.random.randint(0,100,16))#可以指定生成范围
arr=np.random.randint(0,100,16).reshape(4,4)
print(np.sum(arr[arr<=10]))