from PIL import Image, ImageChops
# import secrets
# import string
#
# s = '926725842'
#
# alphabet = string.ascii_letters + string.digits
# password = s[0:4].join(secrets.choice(alphabet) for i in range(3))
# print(password)
#резать айди пополам и тогда шифровать
s = (8, 5)
a = []
q = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

for i in range(s[1]):
    print()
    e = []
    a.append(e)

    for j in range(i, len(q), s[0]):

        e.append(q[j])
        # a.append([q[i : i * s[1]]])
        # print(j, end=' ')
print()
print(a)
# for i in range(s[1]):
#     kol = 0
#     a.append([q[kol:kol+s[0]]])
#     kol += s[0]
# print(a)
# for i in range(len(q)):
#     print(i)



#[1, 1, 0, 0, 0, 0, 0, 0,
# 1, 0, 0, 0, 0, 0, 0, 0,
# 1, 1, 0, 0, 0, 0, 0, 0,
# 1, 0, 0, 0, 0, 0, 0, 0,
# 1, 1, 1, 0, 0, 0, 0, 0]
# f = open('C:/Users/HP/PycharmProjects/TAS/the_second_files/klmnk926725842/scanWorks/vau.png/size@@@@@@@@@@@@.txt')
# p = f.read()
# print(p)

def difference_images(img1, img2):
    global result
    result = 0
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    try:
        result = ImageChops.difference(image_1, image_2).getbbox()
    except:
        pass
    if result == None:
        return img1, 'matches'
    else:
        return 'no matches'
    return
print(difference_images('C:/users/hp/pycharmprojects/TAs/the_second_files/klmnk926725842/test.png', 'C:/users/hp/pycharmprojects/TAs/the_second_files/klmnk926725842/scanWorks/9wLk1Y2RSr8.jpg/test.jpg'))