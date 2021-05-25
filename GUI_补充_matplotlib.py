"""
Matplotlib是Python的一个绘图库，是Python中最常用的可视化工具之一，可以非常方便地创建2D图表和一些基本的3D图表。

它以各种硬复制格式和跨平台的交互式环境生成出版质量级别的图形。通过Matplotlib，开发者可能仅需要几行代码，便可以生成绘图、直方图、功率谱、条形图、错误图、散点图等。

它提供了一整套和Matlab相似的命令API，十分适合交互式地进行制图。而且也可以方便地将它作为绘图控件，嵌入GUI应用程序中。"""

# 首先，在matplotlib建议使用别名，引入包，这样方便以后模块的使用，一般以以下两句开始：
import numpy as np
import matplotlib.pyplot as plt

# 使用默认的绘图属性绘图
# np.linspace主要用来创建等差数列。
"""
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    start:返回样本数据开始点
    stop:返回样本数据结束点
    num:生成的样本数据量，默认为50
    endpoint：True则包含stop；False则不包含stop
    retstep：If True, return (samples, step), where step is the spacing between samples.(即如果为True则结果会给出数据间隔)
    dtype：输出数组类型
    axis：0(默认)或-1
"""
# 这里我们通过画出一个正弦曲线图来讲解下基本用法。
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(x), np.sin(x)
plt.plot(x, C, 'y*-')
plt.plot(x, S, 'm--')  # 画出图形
plt.show()  # 显示
"""
颜色	表示方式
    蓝色	    b
    绿色	    g
    红色	    r
    青色	    c
    品红	    m
    黄色	    y
    黑色	    k
    白色	    w
点的类型	表示方式
    点	    .
    像素	    ,
    圆	    o
    方形	    s
    三角形	^
线的类型	表示方式
    直线	    -
    虚线	    --
    点线	    :
    点划线	-.
"""

# 更多设置
# 设置 figure
# Matplotlib绘制的图形都在一个默认的 figure 中，当然了，你可以自己创建 figure，好处就是可以控制更多的参数，常见的就是控制图形的大小，这里创建一个 figure，设置大小为 (6, 3)。

plt.figure(figsize=(6, 3))
y = np.sin(x)
plt.plot(x, y)
plt.plot(x, y * 2)
plt.show()

