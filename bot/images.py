import os
import sqlite3
from PIL import Image, ImageChops

def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter

legend = {
'а':'a',
'б':'b',
'в':'v',
'г':'g',
'д':'d',
'е':'e',
'ё':'yo',
'ж':'zh',
'з':'z',
'и':'i',
'й':'y',
'к':'k',
'л':'l',
'м':'m',
'н':'n',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'у':'u',
'ф':'f',
'х':'h',
'ц':'ts',
'ч':'ch',
'ш':'sh',
'щ':'shch',
'ъ':'y',
'ы':'y',
'ь':"'",
'э':'e',
'ю':'yu',
'я':'ya',

'А':'A',
'Б':'B',
'В':'V',
'Г':'G',
'Д':'D',
'Е':'E',
'Ё':'Yo',
'Ж':'Zh',
'З':'Z',
'И':'I',
'Й':'Y',
'К':'K',
'Л':'L',
'М':'M',
'Н':'N',
'О':'O',
'П':'P',
'Р':'R',
'С':'S',
'Т':'T',
'У':'U',
'Ф':'F',
'Х':'H',
'Ц':'Ts',
'Ч':'Ch',
'Ш':'Sh',
'Щ':'Shch',
'Ъ':'Y',
'Ы':'Y',
'Ь':"'",
'Э':'E',
'Ю':'Yu',
'Я':'Ya',
}


path = "C:/Users/User/PycharmProjects/TAS/files/"


def difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    result=ImageChops.difference(image_1, image_2).getbbox()
    if result==None:
        print(img1,img2,'matches')
    else:
        print('no matches')
    return

# difference_images('C:/Users/User/PycharmProjects/TAS/bot/Artur_pupil.jpg', 'C:/Users/User/PycharmProjects/TAS/bot/Artur_pupil.jpg')

id = 926725842
conn = sqlite3.connect('bot_tas.db')
c = conn.cursor()


s = "SELECT name FROM sqlite_master WHERE type='table'"
l = c.execute(s)
tables = []
for i in l:
    tables.append(i[0])
for i in tables:
    select = f'SELECT * FROM {i}'
    q = c.execute(select).fetchall()
    for j in q:

        if j[0] == id:

            pupil_name = j[1]
            normalized_teacher_name = ""
            for k in range(len(i)):
                name_ = i

                if i[k] != '_':
                    normalized_teacher_name += i[k]
                else:
                    normalized_teacher_name += ' '
            print(normalized_teacher_name)
# print(name_)
english_name = ""
for i in name_:
    english_name += latinizator(i, legend)



final_path = path + english_name + '/scanWorks/'
dirs = []

for dirpath, dirnames, filenames in os.walk(final_path):
    dirs = dirnames
    break

# print(dirs)
for i in dirs:
    for dirpath, dirnames, filenames in os.walk(final_path + i + '/'):
        if len(filenames) > 1:
            # print(filenames, 'filenames')
            if filenames[1].find('test') != -1:
                # print()
                for j in filenames:
                    if j.find('test') != -1:
                        path_to_file = dirpath + j
                        # print(path_to_file)

                        difference_images(path_to_file, 'C:/Users/User/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/test.jpg')




        # print(i)

    # dirs_of_path = os.listdir(final_path + i + '/')
    # for j in dirs_of_path:
    #     print(j)
p = 'C:/Users/User/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/scanWorks/english_teacher.jpg/test.jpg'
w = p.rsplit('/')
print(w.pop())
print(w)
path_to_squares = ""
for i in w:
    path_to_squares += i + "/"
print(path_to_squares)

id = 926725842
select = "SELECT fullname from id where id=?"
l = c.execute(select, (id, )).fetchone()[0]
print(l)
