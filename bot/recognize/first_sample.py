import cv2

# Считываем два изображения
img = cv2.imread('C:/Users/User/PycharmProjects/TAS/bot/recognize/cat.png')

average_image = cv2.blur(img,(3,3))
cv2.imshow('blur', average_image)
cv2.imshow('orig', img)
cv2.waitKey()