import os
from math import sqrt
import time
import numpy as np
import cv2 as cv


def angle_cos(p0, p1, p2):
    d1, d2 = (p0 - p1).astype('float'), (p2 - p1).astype('float')
    return abs(np.dot(d1, d2) / np.sqrt(np.dot(d1, d1) * np.dot(d2, d2)))


def distance(a1, a2):
    a1 = a1.tolist()
    return int(sqrt((pow(a1[0][0] - a2[0][0], 2) + pow(a1[0][1] - a2[0][1], 2))))


# увеличил с 15 до 20: кол-во квадратов было 42, а надо 40. Помогло

def isInList(cnt, squares):
    for i in range(len(squares)):
        if (distance(cnt, squares[i]) < 15):
            return True
    return False


def find_squares(img):
    # print(img)
    img = cv.GaussianBlur(img, (5, 5), 0)
    squares = []

    for gray in cv.split(img):
        for thrs in range(0, 255, 26):
            if thrs == 0:

                bin = cv.Canny(gray, 0, 50, apertureSize=5)
                bin = cv.dilate(bin, None)

            else:
                _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)
            contours, _ = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                cnt_len = cv.arcLength(cnt, True)
                cnt = cv.approxPolyDP(cnt, 0.02 * cnt_len, True)

                square = cv.contourArea(cnt)
                if len(cnt) == 4 and square < 5000 and square > 50 and cv.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)

                    if (isInList(cnt, squares)):
                        continue

                    max_cos = np.max([angle_cos(cnt[i], cnt[(i + 1) % 4], cnt[(i + 2) % 4]) for i in range(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares


def to_crop(img, square):
    pt1 = square[0]
    pt2 = square[1]
    pt3 = square[2]
    pt4 = square[3]

    I = img
    polygon = [[pt1, pt2, pt3, pt4]]

    minX = I.shape[1]
    maxX = -1
    minY = I.shape[0]
    maxY = -1
    for point in polygon[0]:

        x = point[0]
        y = point[1]

        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    cropedImage = np.zeros_like(I)
    for y in range(0, I.shape[0]):
        for x in range(0, I.shape[1]):
            if x < minX or x > maxX or y < minY or y > maxY:
                continue

            if cv.pointPolygonTest(np.asarray(polygon), (x, y), False) >= 0:
                cropedImage[y, x, 0] = I[y, x, 0]
                cropedImage[y, x, 1] = I[y, x, 1]
                cropedImage[y, x, 2] = I[y, x, 2]

    finalImage = cropedImage[minY:maxY, minX:maxX]
    return finalImage


def comp(a, b):
    return a[0][1] < b[0][1]


def delete_content(folder):
    import os, shutil
    folder = folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def main(filename, type, folder1, folder2):
    if (type):
        # print('current_answers')
        folder = folder1
        # print(folder)

    else:
        folder = folder2
        # print('answers')
    delete_content(folder)

    img = cv.imread(filename)
    squares = find_squares(img)

    squares_ = squares
    squares = []

    for square in squares_:
        im = to_crop(img, square)
        percentage = im.shape[0] * 100 / (im.shape[0] + im.shape[1])
        # print(percentage)
        if (percentage >= 45 and percentage <= 55):
            squares.append(square)

    squares = sorted(squares, key=lambda square: (square[0][1], square[0][0]), reverse=False)
    pred = squares[0][0][1]
    # print(squares[0][0][1], 'axaxax')

    # Квест, попробуй понять, что я делаю и для чего

    for i in range(1, len(squares)):
        if (abs(squares[i][0][1] - pred) <= 5):
            squares[i][0][1] = pred
        else:
            pred = squares[i][0][1]

    squares = sorted(squares, key=lambda square: (square[0][1], square[0][0]), reverse=False)
    # end

    amount = 0
    array = []
    for i in range(len(squares)):
        im = to_crop(img, squares[i])

        im_to_save = im
        cv.imwrite(os.path.join(folder, 'img' + str(i) + '.jpg'), im_to_save)
        # print(os.path.join(folder, 'img' + str(i) + '.jpg'))
        amount += 1

        sought = [255, 255, 255]
        white = np.count_nonzero(np.all(im == sought, axis=2))
        sought = [0, 0, 0]
        black = np.count_nonzero(np.all(im == sought, axis=2))
        # print(black, white)
        if black / (black + white) > 0.8:
            array.append(1)
        else:
            array.append(0)

    print("Found " + str(amount) + ' squares')

    print(array)
    kol = 0
    for i in array:
        if i == 1:
            kol += 1
    # print(kol)
    return array


# start_time = time.time()
# print('------------------------------')

# main('C:/Users/HP/PycharmProjects/TAS/create_sample/old_format.png', 1, 'C:/Users/HP/PycharmProjects/TAS/the_second_files/klmnk926725842/scanWorks/teacher.jpg/current_answers', 'C:/Users/HP/PycharmProjects/TAS/the_second_files/klmnk926725842/scanWorks/teacher.jpg/answers' )

# print("--- %s seconds ---" % (time.time() - start_time))

