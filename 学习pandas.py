import pandas as pd
df=pd.read_excel("1.xlsx","Sheet1",engine="openpyxl")
# 提取数据的前几行
print(df.head(10))
print(type(df ))

data={"样本号":[1,2,3],"等边长":[8,7,6],"类型":[2,3,4]}
datadf=pd.DataFrame(data)
print(datadf)

#基础信息
print(df.info())

#缺失值处理
print(df.head())
df=df.dropna()
print(df.head())

#数据类型转换
# df[key]=df[key].astype(type) 

#选择和过滤
# 见图