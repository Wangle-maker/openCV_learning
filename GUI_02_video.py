import numpy as np
import cv2

"""目标
• 学会读取视频文件，显示视频，保存视频文件
• 学会从摄像头获取并显示视频
• 你将会学习到这些函数：cv2.VideoCapture()，cv2.VideoWrite()"""

# 用摄像头捕获视频
"""为了获取视频，你应该创建一个 VideoCapture 对象。他的参数可以是
设备的索引号，或者是一个视频文件。设备索引号就是在指定要使用的摄像头。
一般的笔记本电脑都有内置摄像头。所以参数就是 0。你可以通过设置成 1 或
者其他的来选择别的摄像头。之后，你就可以一帧一帧的捕获视频了。但是最
后，别忘了停止捕获视频。"""


cap = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
