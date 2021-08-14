import time
import cv2
from PIL import Image, ImageChops, ImageDraw, ImageFont
import telebot
import sqlite3
import os
import keyboa
from keyboa import keyboa_maker
import codecs
import csv
import requests
import random

bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')
legend = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'yo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shch',
    'ъ': 'y',
    'ы': 'y',
    'ь': "'",
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',

    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'Yo',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ъ': 'Y',
    'Ы': 'Y',
    'Ь': "'",
    'Э': 'E',
    'Ю': 'Yu',
    'Я': 'Ya',
}


def create_name(name):
    # разбор имени
    final_name = ""
    for i in range(len(name)):
        if name[i] != ' ':
            final_name += name[i]
        elif name[i] == " ":
            final_name += "_"
    return final_name


def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter


def get_all_pupils(id):
    path = os.getcwd()
    print(path)
    conn = sqlite3.connect('db_2.db')
    c = conn.cursor()
    select = "SELECT * FROM id"
    l = c.execute(select).fetchall()
    for i in l:
        yes = 0
        if id == i[0]:
            if i[2] == 'yes':
                yes = 1
                break
    if yes == 0:
        bot.send_message(id, 'сорямба, ты не учитель')

    else:
        name = i[3]

    sql_name = ""
    for i in name:
        if i == ' ':
            sql_name += '_'
        else:
            sql_name += i
    select = f"SELECT * FROM klmnk{id}"
    l = c.execute(select)
    list_of_pupils = []
    j = 1
    for i in l:
        list_of_pupils.append(str(j) + '. ' + str(i[1]))
        j += 1

    # bot.send_message(id, str(list_of_pupils))
    kb_fruits = keyboa_maker(items=list_of_pupils, copy_text_to_callback=True, items_in_row=1)
    bot.send_message(
        chat_id=id, reply_markup=kb_fruits,
        text='список ваших учеников')

  

def delete(id, name):
    conn = sqlite3.connect('db_2.db')
    c = conn.cursor()

    select = "SELECT fullname from id where id=?"
    data = (id,)
    l = c.execute(select, data).fetchone()[0]

    name_of_teacher = ""
    for i in l:
        if i == " ":
            name_of_teacher += "_"
        else:
            name_of_teacher += i

    axa = "SELECT id from id where fullname=?"
    select = "SELECT * from id where fullname=?"

    if name[0] == ' ':
        name = name[1:]

    data = (name,)

    z = c.execute(select, data).fetchone()

    id_of_pupil = z[0]
    print(id_of_pupil, 'id_of_pupilid_of_pupilid_of_pupilid_of_pupilid_of_pupil')
    


    dal = f"DELETE FROM klmnk{id} WHERE id=?"

    data = (id_of_pupil,)

    c.execute(dal, data)

    conn.commit()

    select = "SELECT * FROM id"

    bot.send_message(id_of_pupil, f'преподаватель {l} забрал у вас доступ от своих заданий.')
    conn.close()


def send_message_to_the_pupil(id, name, text):
    conn = sqlite3.connect('db_2.db')
    c = conn.cursor()
    sql = "SELECT id FROM id WHERE fullname=?"
    data = (name,)
    name_of_the_pupil = c.execute(sql, data).fetchone()[0]
    # тут надо отправлять файл из списка всех отправленных учителем файлов


def get_files_from_teacher(id, message):

    # global files_lol

    id = int(message.chat.id)
    path = 'c:/users/hp/PycharmProjects/TAS/files/'
    conn = sqlite3.connect('db_2.db')
    c = conn.cursor()
    select_name = "SELECT fullname from id where id=?"
    data = (id,)
    l = c.execute(select_name, data)

    for i in l:
        name = i[0]

    teacher = ""
    teacher_name = create_name(name)
    for i in teacher_name:
        teacher += latinizator(i, legend)
    # print(teacher_name)
    path = path + teacher + '/scanWorks/'
    files = []
    names = []
    for dirpath, dirnames, filenames in os.walk(path):
        names = dirnames
        files_lol = names

        break
    mass_of_files = [0] * len(names)

    for i in range(len(names)):
        mass_of_files[i] = names[i] + '$$$'


    w = []
    for i in range(len(names)):
            w.append({names[i]: mass_of_files[i]})



    kb_fruits = keyboa_maker(items=w, copy_text_to_callback=True, auto_alignment=True)
    bot.send_message(
        chat_id=id, reply_markup=kb_fruits,
        text="выберите файл, который вы хотите отправить данному ученику")

def get_text_from_the_teacher_in_func(message, name):
    text = message.text
    # bot.send_message()


# def send_text(id_of_pupil, text):
    # bot.send_message(id_of_pupil, )

# def get_marks(message):


#при каждом отравленном тесте нужно заносить в файл оценку ученика, потом функцией вызывать что-то наподобие списка

def enter_mark(name, path, ocenka):
    global flag
    # print(name, path, ocenka)
    FILE = os.path.join(path, 'marks_of_the_pupils!!@#$%^&.csv')


    # FILE = os.path.join(path, 'marks_of_the_pupils!!@#$%^&.csv')
    # print(FILE, 'file')
    kol = -1234
    with open(FILE, newline='') as f:
        global flag

        reader = csv.reader(f, delimiter='|')# quoting=csv.QUOTE_NONE)
        # print(type(reader))
        dic = list(reader)
        # print(dic[0][1] == name, 'axaxax')
        flag = False
        # print('axaxaax')
        for row in dic:
            #делать все через итерацию!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            flag = False

            for i in row:
                # print(i, 'axaxaxaxaxax', row)
                if i == name:
                    print(i, name, "IIIII< NAMEEEEE")

                    flag = True
                    row.append(str(ocenka))

                    break
                    # print(row,'roworworw')
        print(flag, 'uqqqq')
        if flag == False:
            print('бред ебучий')
            dic.append([name, str(ocenka)])

    for row in dic:
        for i in row:
            if i == '':
                row.remove(i)
            if i == ' ':
                row.remove(i)
    # print(dic, 'dic')
    print(dic)





    with open(FILE, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in dic:
            spamwriter.writerow(row)
            # print('sdjffdhsflksdklflksdjflkjsdlkfjlsdf')



        # spamwriter.writerow(('Жарский Егор Александрович', '12'))
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



def marks_NONE(w, path, ocenka):

    f = codecs.open(f"{path}"
    #тут эксель нужооооооон
             "/marks_of_the_pupils!!@#$%^&.txt", mode='r', encoding='utf-8')
    s = f.read().splitlines()
    # print(s)

    f.close()

    flag = True
    if len(s) == 0:
        f = open(path + '/marks_of_the_pupils!!@#$%^&.txt', 'w')
        # print(w + f' -  {str(ocenka)}')
        f.write(w + f' - {str(ocenka)}')
        f.close()
    else:
        for i in range(len(s)):

            if i == len(s) - 1:
                print(i)
                flag = False
            if s[i].find(w) != -1:
                flag = True
                break

        if not flag:
            # print(s, flag)
            s.append(w + f' - {ocenka}')
            line = ""
            for i in range(len(s)):
                if i != len(s) - 1:
                    line += s[i] + "\n"
                else:
                    line += s[i]

                f = open(f"{path}"
                         "/marks_of_the_pupils!!@#$%^&.txt", 'w', encoding='utf-8')
                f.write(line)

        elif flag:
            # тут ищем этого чела в списке и добавляем ему оценку
            # print(flag, s)
            for i in range(len(s)):
                if s[i].find(w) != -1:
                    s[i] = s[i] + f'  {str(ocenka)}'

            line = ""
            for i in range(len(s)):
                if i != len(s) - 1:
                    line += s[i] + '\n'
                else:
                    line += s[i]

                    f = open(f"{path}"
                             "/marks_of_the_pupils!!@#$%^&.txt", 'w', encoding='utf-8')
                    f.write(line)
                    f.close()
        # оформить в виде функции.
        #damn


def delete_test(message):
    conn = sqlite3.connect('db_2.db')
    c = conn.cursor()
    sel = 'SELECT teacher_status from id where id=?'
    data = (message.chat.id,)
    status = c.execute(sel, data).fetchone()[0]
    print(status)
    if status == 'yes':
        # print('teacher')
        pass
    else:
        bot.send_message(message.chat.id, 'вы не обладаете статусом учителя.')
        return 0
    path = f'C:/Users/HP/PycharmProjects/TAS/the_second_files/klmnk{message.chat.id}/scanWorks/'
    print(path)
    dirnames = []
    for _, dirnames, _ in os.walk(path):
        dirnames = dirnames

        break
    print(dirnames)
    b = []
    for i in dirnames:
        b.append({i : f'!!!@@@@@###{i}!!!@@@@@###'})
    print(b)
    maker = keyboa_maker(items=b, copy_text_to_callback=True, items_in_row=2)
    bot.send_message(
            chat_id=message.chat.id, reply_markup=maker,
            text="выберите файл, который вы хотите удалить.")



def create_white_square(id, kol):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #квадраты 20х20
    #расстояние между квадратами 10 пикселей
    img = Image.open('C:/Users/HP/PycharmProjects/TAS/create_sample/square.png', 'r')
    img_w, img_h = img.size
    #
    font_size = 20
    fnt = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    font_size2 = 15
    fnt2 = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    fnt_little = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', 15)
    background = Image.new('RGBA', ((kol[0] * 30) + 20, (kol[1] * 30) + 36), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    draw_text = ImageDraw.Draw(background)
    print(background.size)
    q, w = 25, 20
    # q, w = background.size[0] // kol[0] ,background.size[1] // kol[1]
    # x = background.size[0] // kol[0]
    # y = background.size[1] // kol[1]
    x, y = 25, 20
    print(x, y, 'x y')
    # x, y = 20, 10
    xx, yy = 12, 10
    ya = 1
    for i in range(kol[1]):
        if i == 0:
            for k in range(1, kol[0] + 1):
                if k > 9:
                    draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt_little)
                else:
                        draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt)
                x += 30
                if k + 1 == kol[0]:
                    print('uf')
                    y += 17
        if i != 0:
            y += 30
        x = q
        for j in range(kol[0]):
            background.paste(img, (x, y))
            x += 30
            if j == 0:
                # print(x)
                draw_text.text((q - 20, y), alphabet[i], fill=('#1C0606'), font=fnt2)
            # if j == 0:
                # for z in range(0, kol[1] + 1, 1):
                #     ya += 25
                #     draw_text.text((13, ya), alphabet[z], fill=('#1C0606'), font=fnt2)

                #     if z == kol[1]:
                #         x+=30


    # offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    # background.paste(img, (10, 10))
    path = f'C:/Users/HP/PycharmProjects/TAS/create_sample/{id}_white_out.png'
    # background.show()
    background.save(path)
    return path


def create_black_square(id, kol):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # квадраты 20х20
    # расстояние между квадратами 10 пикселей
    img = Image.open('C:/Users/HP/PycharmProjects/TAS/create_sample/black_square.png', 'r')
    img_w, img_h = img.size
    #
    font_size = 20
    fnt = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    font_size2 = 15
    fnt2 = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', font_size)
    fnt_little = ImageFont.truetype('C:/Users/HP/PycharmProjects/TAS/create_sample/JAi_____.TTF', 15)
    background = Image.new('RGBA', ((kol[0] * 30) + 20, (kol[1] * 30) + 36), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    draw_text = ImageDraw.Draw(background)
    print(background.size)
    q, w = 25, 20
    # q, w = background.size[0] // kol[0] ,background.size[1] // kol[1]
    # x = background.size[0] // kol[0]
    # y = background.size[1] // kol[1]
    x, y = 25, 20
    print(x, y, 'x y')
    # x, y = 20, 10
    xx, yy = 12, 10
    ya = 1
    for i in range(kol[1]):
        if i == 0:
            for k in range(1, kol[0] + 1):
                if k > 9:
                    draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt_little)
                else:
                    draw_text.text((x + 2, yy), str(k), fill=('#1C0606'), font=fnt)
                x += 30
                if k + 1 == kol[0]:
                    print('uf')
                    y += 17
        if i != 0:
            y += 30
        x = q
        for j in range(kol[0]):
            background.paste(img, (x, y))
            x += 30
            if j == 0:
                # print(x)
                draw_text.text((q - 20, y), alphabet[i], fill=('#1C0606'), font=fnt2)
            # if j == 0:
            # for z in range(0, kol[1] + 1, 1):
            #     ya += 25
            #     draw_text.text((13, ya), alphabet[z], fill=('#1C0606'), font=fnt2)

            #     if z == kol[1]:
            #         x+=30

    # offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    # background.paste(img, (10, 10))
    path = f'C:/Users/HP/PycharmProjects/TAS/create_sample/{id}_black_out.png'
    # background.show()
    background.save(path)
    return path


#
'''def create_black_square(id, kol):

    #kol = (162, 162)
    # квадраты 20х20
    # расстояние между квадратами 10 пикселей
    img = Image.open('C:/Users/HP/PycharmProjects/TAS/create_sample/black_square.png', 'r')
    img_w, img_h = img.size
    #
    background = Image.new('RGBA', (kol[0] * 32, kol[1] * 32), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    x, y = 10, 10
    for i in range(kol[1]):
        if i != 0:
            y += 30
        x = 10
        for j in range(kol[0]):
            background.paste(img, (x, y))
            x += 30

    # offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    # background.paste(img, (10, 10))
    path = f'C:/Users/HP/PycharmProjects/TAS/create_sample/{id}_black_out.png'
    background.save(path)
    return path'''
# enter_mark('Жарский Никита Александрович', 'C:/Users/HP/PycharmProjects/TAS/the_second_files/klmnk926725842/scanWorks/current_unnamed.png', 6)


def check_answer(size, id):
    path = 'C:/Users/HP/PycharmProjects/TAS/create_sample'
    s = create_black_square(id, size)
    print(s)
    return s
# check_answer((8, 6), 926725842)
#тут нужно уже в саму проверку теста лезть. и попробовать считать оценку на квадратах новых. да для начала все реализовать надо.

def search(first, second, id):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    small_image = cv2.imread(first)
    large_image = cv2.imread(second)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    im = Image.open(second)
    im1 = im.crop((MPx, MPy, MPx+ tcols, MPy+trows))
    print((MPx, MPy), (MPx + tcols, MPy + trows))
    # Display the original image with the rectangle around the match.
    # cv2.imshow('output',large_image)
    # im1.show()
    im1.save(f'C:/Users/HP/PycharmProjects/TAS/create_sample/search_for_{id}.png')
    # The image is only displayed if we call this
    # cv2.waitKey(0)

    path = f'C:/Users/HP/PycharmProjects/TAS/create_sample/search_for_{id}.png'
    return path


def req(subj):
    f = open('passwords.txt', 'r')
    f = f.read()
    f = f.split('\n')
    password = f[random.randint(0, 99)]
    print(password)
    r = requests.get(f'https://tas.na4u.ru//post_value/{subj}/{password}')
    print(r.text)
    print(r.status_code)
    if r.status_code == 200:
        print('success')

    return r.json()

