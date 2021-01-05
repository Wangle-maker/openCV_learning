import cv2


def video_demo():
    capture = cv2.VideoCapture(0)
    while 1:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow("video", frame)
        c = cv2.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)


print('------Hello, python!------')
# src = cv2.imread("D:/Desktop/pythondata/openCV_learning/Resource/lena.png")
# cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input image", src)
video_demo()
cv2.waitKey(0)

cv2.destroyAllWindows()
