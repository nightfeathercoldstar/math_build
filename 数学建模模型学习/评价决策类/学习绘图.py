import matplotlib.pylab as plt
import numpy as np
x=np.linspace(0,10,100)
y=np.sin(x)
plt.plot(x,y)
plt.title("y=sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# 不划线只花点
plt.scatter(x,y,marker="*",c="r",linestyle="--",label="***")
plt.show()