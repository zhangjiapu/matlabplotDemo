import numpy as np
import matplotlib.pyplot as plt

def func1():
    x = np.linspace(0,10,1000) # 生成0-10之间的1000个点，作为自变量集合
    y = np.sin(x) # 生成正弦函数的因变量集合
    z = np.cos(x**2) # 生成余弦函数的因变量集合

    plt.figure(figsize=(10,6)) # 生成的图片的大小（长：10*80 像素；宽：6*80 像素）

    # 用plot函数绘图 ，label里面的 $ 可用可不用
    # b-- 是 color = bule 和 虚线
    plt.plot(x,y,label="$sin(x)$",color='red',linewidth=2)
    plt.plot(x,z,"b--",label="$cos(x^2)$")

    plt.xlabel("Times(s)") # 横坐标的标识
    plt.ylabel("Volt") # 纵坐标的标识
    plt.title("Pyplot First Example") # 整个图的表头
    plt.ylim(-1.2,1.2) # y轴的范围
    plt.legend() # 显示图例
    plt.show() # 显示图像







def func2():
    plt.subplot(333,facecolor = 'red') # 3行3列的第三个（一共9个图），也就是第一行的第三个，红色
    plt.subplot(312,facecolor = 'blue') # 3行1列的的第二个（一共3个图），也就是第二行一整行，蓝色
    plt.subplot(338,facecolor = '#123454')# 3行3列的第八个（一共9个图），也就是第三行的第二个，随便啥颜色
    plt.show()

if __name__ == '__main__':
    func2()