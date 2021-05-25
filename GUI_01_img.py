import cv2
import numpy as np

# print('------Hello, python!------')
# src = cv2.imread("D:/Desktop/pythondata/openCV_learning/Resource/lena.png")
# cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input image", src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""读入图像
使用函数 cv2.imread() 读入图像。
这幅图像应该在此程序的工作路径，或者给函数提供完整路径，第二个参数是要告诉函数应该如何读取这幅图片。"""
"""
    cv2.IMREAD_COLOR : 默认使用该种标识。加载一张彩色图片，忽视它的透明度。
    cv2.IMREAD_GRAYSCALE : 加载一张灰度图。
    cv2.IMREAD_UNCHANGED : 加载图像，包括它的Alpha通道。     友情链接：Alpha通道的概念
    提示：如果觉得以上标识太麻烦，可以简单的使用1，0，-1代替。（必须是整数类型）
"""
# 加载彩色灰度图像
img = cv2.imread('Resource/lena.png', cv2.IMREAD_ANYCOLOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 警告：就算图像的路径是错的，OpenCV 也不会提醒你的，但是当你使用命令print img时得到的结果是None。


"""显示图像
使用函数 cv2.imshow() 显示图像。
窗口会自动调整为图像大小。第一个参数是窗口的名字，其次才是我们的图像。你可以创建多个窗口，只要你喜欢，但是必须给他们不同的名字"""
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
"""
    一 种 特 殊 的 情 况 是， 你 也 可 以 先 创 建 一 个 窗 口， 之 后 再 加 载 图 像。 这 种 情 况 下， 你 可 以 决 定 窗 口 是 否 可 以 调 整 大 小。 
    使 用 到 的 函 数 是 cv2.namedWindow()。 
    初 始 设 定 函 数 标 签 是 cv2.WINDOW_AUTOSIZE。
    但 是 如 果 你 把 标 签 改 成 cv2.WINDOW_NORMAL，你就可以调整窗口大小了。当图像维度太大，或者要添加轨迹条时，调整窗口大小将会很有用
"""
cv2.imshow('image', img)
cv2.waitKey(0)
"""cv2.waitKey() 是一个键盘绑定函数。需要指出的是它的时间尺度是毫
秒级。函数等待特定的几毫秒，看是否有键盘输入。特定的几毫秒之内，如果
按下任意键，这个函数会返回按键的 ASCII 码值，程序将会继续运行。如果没
有键盘输入，返回值为 -1，如果我们设置这个函数的参数为 0，那它将会无限
期的等待键盘输入。"""
cv2.destroyAllWindows()
# cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口。


"""保存图像"""
# 使用函数 cv2.imwrite() 来保存一个图像。首先需要一个文件名，之后才是你要保存的图像。
cv2.imwrite('hanpi.png', img)
# 如果不写保存路径的时候默认的保存路径是与当前代码同位置的

