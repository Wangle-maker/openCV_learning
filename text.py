import cv2
print('------Hello, python!------')
src = cv2.imread("D:/Desktop/pythondata/openCV_learning/Resource/lena.png")
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)
cv2.waitKey(0)

cv2.destroyAllWindows()
