import telebot
from telebot import types
import sqlite3
from keyboa import keyboa_maker
import find_squares
from PIL import Image, ImageChops
import os
from functions_to_bot import get_all_pupils, delete, get_text_from_the_teacher_in_func, get_files_from_teacher

global Name_fsa_fsa, teacher_name_fsa_fsa
global name_of_the_teacher, name_of_the_pupil


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


files_lol = []
selected_days = []
days = ["понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота",
        "воскресенье", "✅", ]
select_of_days = [
    "понедельник", "вторник", "среда",
    "четверг", "пятница", "суббота",
    "воскресенье", "✅"
]


def xppx(message):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    select = "select id from id where fullname=?"
    data = (name_of_the_pupil,)
    l = c.execute(select, data).fetchone()[0]

    text = message.text
    bot.send_message(l, f'отправленное сообщение от {name_of_the_teacher}: \n{text}')
    sel = "SELECT id FROM id WHERE fullname=?"
    data = (name_of_the_teacher,)
    id = c.execute(sel, data).fetchone()[0]
    bot.send_message(id, f'сообщение отправлено пользователю {name_of_the_pupil}')


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def uploaded_answer_0(filename, folder1, folder2):
    global array, first
    array = find_squares.main(filename, 0, folder1, folder2)
    # print(array)
    first = array


def uploaded_answer_1(filename, folder1, folder2):
    global array, second
    array = find_squares.main(filename, 1, folder1, folder2)
    print(array)
    second = array


def difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    result = ImageChops.difference(image_1, image_2).getbbox()
    if result == None:
        return img1, 'matches'
    else:
        return 'no matches'
    return


def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter


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

bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')


def new_scanWorks_folder(filename, fullname):
    global papki  # создаем в папке учителя папку scanWorks, а в ней answers and current answers
    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files'):
        folders = dirnames
        break
        # print(filenames)
    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files/' + fullname):
        papki = dirnames

        break

    if 'scanWorks' not in papki:
        path = 'c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/'
        path = 'c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/'
        try:
            os.mkdir(path)
        except:
            pass
    # теперь нужно создавать подпапку каждого из файлов, чтобы там хранить ответы на тесты
    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/'):
        dirs_of_scan = dirnames
        break
    if len(dirs_of_scan) == 0 or filename not in dirs_of_scan:
        os.mkdir('c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename)
        os.mkdir('c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename + '/answers/')
        os.mkdir(
            'c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename + '/current_answers/')
    #     тут теперь сохранять файл в папку
    src = filename
    save_dir = 'c:/users/hp/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename

    print(fullname)
    print(src, 'FILENAME')
    # или лучше сохранять в гет ферст файл?
    # with open(save_dir + "/" + src, 'wb') as new_file:
    #     new_file.write(downloaded_file)


def get_the_first_file(message):
    global konch
    global folders, save_dir
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, 'FILENAMEEEE')
    # тут нада сохранять его в отдельную папку с учителем и сразу же обрабатывать.

    id = int(message.chat.id)
    select = "SELECT fullname from id WHERE id=?"
    data = (id,)
    l = c.execute(select, data)
    for i in l:
        print(i)
        name = i[0]
    fullname = create_name(name)
    # print(fullname, 'FULLNAME')
    latin_name = ""
    for i in fullname:
        latin_name += latinizator(i, legend)

    new_scanWorks_folder(file_name, latin_name)

    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files'):
        folders = dirnames
        break

    file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""
    # print(folders, 'FOLDERS')
    # print(fullname)
    # print(src, 'FILENAME')
    # вот тута нужно выбирать папку и сохранять

    if latin_name in folders:

        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name

    else:
        new_folder(latin_name)
        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name
    # здесь сохранить файл в папку с названием самого файла
    # img -- это фото ответов
    a = src.rsplit('.')[1]
    # print(a, 'FFFFFFFFFFFFFFFFFFFFFFF')
    konch = save_dir + "/"
    with open(save_dir + "/" + 'img' + '.' + a, 'wb') as new_file:
        new_file.write(downloaded_file)

    print('скачав')
    # bot.send_message(message.chat.id, 'сохранено.')

    bot.register_next_step_handler(message, get_the_second_file)
    # get_the_second_file(message, konch)


def get_the_second_file(message):
    global konch
    path = konch
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    id = int(message.chat.id)
    select = "SELECT fullname from id WHERE id=?"
    data = (id,)
    l = c.execute(select, data)
    for i in l:
        print(i)
        name = i[0]
    fullname = create_name(name)
    # print(fullname, 'FULLNAME')
    latin_name = ""
    for i in fullname:
        latin_name += latinizator(i, legend)

    file_name2 = message.document.file_name
    a = file_name2.rsplit('.')[1]
    file_id2 = message.document.file_name
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)

    print(path, 'PAAAAAAAAAAAAAAAAAAAAAAAAATHHHHHHH')
    with open(path + 'test' + '.' + a, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, 'сохранено.')
    konch = ""


def get_file_from_no(message):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    id = int(message.chat.id)
    select = "SELECT fullname from id WHERE id=?"
    data = (id,)
    l = c.execute(select, data)
    for i in l:
        print(i)
        name = i[0]
    fullname = create_name(name)
    # print(fullname, 'FULLNAME')
    latin_name = ""
    for i in fullname:
        latin_name += latinizator(i, legend)

    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files'):
        folders = dirnames
        break

    file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""

    if latin_name in folders:

        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name

    else:
        new_folder(latin_name)
        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name
        # здесь сохранить файл в папку с названием самого файла
        # img -- это фото ответов

    # print(a, 'FFFFFFFFFFFFFFFFFFFFFFF')
    konch = save_dir + "/"
    for dirpath, dirnames, filenames in os.walk(
            "c:/users/hp/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/'):
        break
    print(dirnames)

    if len(dirnames) == 0 or file_name not in dirnames:
        os.mkdir('c:/users/hp/PycharmProjects/TAS/files/' + latin_name + '/scanWorks/' + file_name)

    with open(save_dir + "/" + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    print('уххуху')


def get_text_from_pupil(message):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    id = int(message.chat.id)
    text = message.text
    message_id = message.message_id

    s = "SELECT name FROM sqlite_master WHERE type='table'"
    l = c.execute(s)
    tables = []
    for i in l:
        tables.append(i[0])
    for i in tables:
        select = f'SELECT * FROM {i}'
        q = c.execute(select).fetchall()
        for j in q:
            if j[0] == message.chat.id:
                pupil_name = j[1]
                normalized_teacher_name = ""
                for k in range(len(i)):
                    if i[k] != '_':
                        normalized_teacher_name += i[k]
                    else:
                        normalized_teacher_name += ' '
                print(normalized_teacher_name)
    select_teacher_id = "select id from id where fullname=?"
    data = (normalized_teacher_name,)
    offf = c.execute(select_teacher_id, data).fetchone()
    for i in offf:
        teacher_id = i
    # print(teacher_id)
    # print(pupil_name)

    bot.forward_message(teacher_id, id, message_id)
    bot.send_message(teacher_id, f'отправлено от {pupil_name}')


def get_answers(message):
    id = int(message.chat.id)
    message_id = message.message_id

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
            if j[0] == message.chat.id:
                pupil_name = j[1]
                normalized_teacher_name = ""
                for k in range(len(i)):
                    if i[k] != '_':
                        normalized_teacher_name += i[k]
                    else:
                        normalized_teacher_name += ' '
                print(normalized_teacher_name)
    select_teacher_id = "select id from id where fullname=?"
    data = (normalized_teacher_name,)
    offf = c.execute(select_teacher_id, data).fetchone()
    for i in offf:
        teacher_id = i
    print(teacher_id)
    print(pupil_name)
    bot.forward_message(teacher_id, id, message_id)
    bot.send_message(teacher_id, f'последний решенный тест от {pupil_name}')


def get_time(message):
    time = message.text
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    id = int(message.chat.id)
    se = "SELECT fullname from id WHERE id=?"
    data = (id,)
    l = c.execute(se, data)
    name = ''
    for i in l:
        name = i[0]
    fullname = create_name(name)

    data = ('12:57', None, None, None, None)
    select = "SELECT * FROM mail"
    l = c.execute(select).fetchall()
    list_of_teachers = []
    for i in l:
        list_of_teachers.append(i[1])
    print(list_of_teachers)

    if len(l) == 0:
        insert = 'INSERT INTO mail values(?,?)'
        data = (time, fullname)
        c.execute(insert, data)
        conn.commit()

    if fullname in list_of_teachers and len(l) != 0:
        insert = "UPDATE mail set time=? WHERE fullname=?"
        data = (time, fullname)
        c.execute(insert, data)
        conn.commit()
    else:
        insert = "INSERT INTO mail values(?,?)"
        data = (time, fullname)
        c.execute(insert, data)
        conn.commit()


def markup_to_cities(city, message):
    id = int(message.chat.id)

    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    print(id, 'ID')
    get_sub = "SELECT subject FROM id WHERE id=?"
    data = (id,)
    p = c.execute(get_sub, data).fetchall()

    q = ""
    for k in p:
        q = k[0]

    all = "SELECT city from id"
    l = c.execute(all).fetchall()
    kol = len(l)
    cities = []
    for i in l:
        cities.append(i[0])
    select = "SELECT * FROM id WHERE city=?"
    data = (city,)
    p = c.execute(select, data).fetchall()
    teachers = []
    kol_teachers = 0

    for j in p:
        # print(j, 'jjjjjjjjjjjj', id, "IDDD")
        if j[2] == 'yes':
            if j[1] == city:
                if j[4] == q:
                    if j[0] != id:
                        kol_teachers += 1
                        teachers.append(j[3])

    # print('sanya')

    it = []
    if len(teachers) == 0:
        markup_inline = types.InlineKeyboardMarkup()
        it.append(types.InlineKeyboardButton(
            text='на данный момент не зарегистрирован ни один преподаватель по этому предмету.',
            callback_data='no_teachers'))
        # print(teachers, "HUIABFJNEAFN<LMA<SF><S>F<L:ASFPKJDAHFIAHDFBHAD")
        markup_inline.add(it[0])
    for i in range(kol_teachers):
        markup_inline = types.InlineKeyboardMarkup()

        it.append(types.InlineKeyboardButton(text=teachers[i], callback_data=teachers[i]))

    # markup.add(list_of_items)  # , item2)
    for j in range(kol_teachers):
        # print(kol_teachers)
        # print(j, 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
        markup_inline.add(it[j])

    # print(cities)
    bot.send_message(message.chat.id, 'Выберите себе преподавателя', reply_markup=markup_inline)


def haha(message):
    global select_of_days
    # решить вопрос этим списком всратым
    id = int(message.chat.id)

    kb_fruits = keyboa_maker(items=select_of_days, copy_text_to_callback=True, auto_alignment=True)

    bot.send_message(
        chat_id=id, reply_markup=kb_fruits,
        text="выберите дни для рассылки заданий.")


# переделывать функцию так, чтобы каждый раз по клику кнопки записывать новое
def get_days_fromcall(day, message):  # , name, teacher_name):
    a = ["понедельник", "вторник", "среда",
         "четверг", "пятница", "суббота",
         "воскресенье", "✅", ]
    conn = sqlite3.connect('bot_tas.db')
    q = conn.cursor()

    id = int(message.chat.id)
    # print(teacher_name_fsa_fsa)
    teacher_fullname = create_name(teacher_name_fsa_fsa)

    print(day, 'DAYYYYYY')

    days = {"понедельник": u'0', "вторник": u"1", "среда": u"2", "четверг": u"3", "пятница": u"4", "суббота": u"5",
            "воскресенье": u"6"}

    '''for i in range(len(day)):
        day[i] = day[i].lower()

    c = list(set(day) & set(days))
    str_of_days = ""
    res = []
    for i in c:
        res.append(int(days[i]))
    res.sort(reverse=False)
    # тут заносить по имени в базу данных с учителем
    print(res, 'resssssssss')
    print(teacher_fullname, 'teacher_fullname')
    # делаю строку из списка дней для рассылки
    #
    for j in range(len(res)):

        if j != len(res) - 1:
            str_of_days += str(res[j]) + ' '
        else:
            str_of_days += str(res[j])'''
    for i in days.keys():
        if i == day:
            str_of_days = days[i]
    print(str_of_days, 'str_of_days')

    select = f"SELECT * FROM {teacher_fullname} WHERE id=?"

    data = (id,)
    l = q.execute(select, data).fetchone()
    last_day = str(l[-1])
    print(last_day, 'last_day')
    day_of_db = ""
    for i in range(len(last_day)):
        if last_day[i] != 'x':
            day_of_db += last_day[i]
    print(day_of_db, 'day_of_db')
    print(l, 'llllllllllll')
    days_x = str(l[-1])

    print(days_x, 'days_x')
    if days_x.find('x') == -1:

        insert = f"UPDATE {teacher_fullname} set days=? WHERE id=?"
        data = (str_of_days + ' ' + day_of_db, id)
        list_of_selected_days = (str_of_days + ' ' + day_of_db).rsplit(' ')

        print(list_of_selected_days)
        q.execute(insert, data)
        conn.commit()
        print(a)
        # for i in range(len(list_of_selected_days)):
        #     list_of_selected_days[i] =  int(list_of_selected_days[i])

        for i in range(len(a)):
            for j in range(len(list_of_selected_days)):
                # print(a[i], list_of_selected_days[j])
                if a[i] == get_key(days, list_of_selected_days[j]):
                    a[i] = '✓'


    else:
        insert = f"UPDATE {teacher_fullname} set days=? WHERE id=?"
        print(str_of_days, "SL:AJFLKDHFJKSJKFHSJKHFKJDSHFJKDSHKFHSDJKFHKJDSHF")
        print(type(str_of_days))
        a[int(str_of_days)] = '✓'
        data = (str_of_days, id)
        q.execute(insert, data)
        conn.commit()
        # если заканчивается на х, то типо должны заново начать считать

    # возвращать клавиатуру ахха

    kb_fruits = keyboa_maker(items=a, copy_text_to_callback=True, auto_alignment=True)

    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                          text='выберите дни для рассылки заданий.', reply_markup=kb_fruits)

    # insert = f"UPDATE {teacher_fullname} set days=? WHERE id=?"
    # data = (str_of_days, id)
    #
    # conn = sqlite3.connect('bot_tas.db')
    # c = conn.cursor()
    #
    # c.execute(insert, data)
    # conn.commit()
    # print('success')
    # bot.send_message(message.chat.id, 'записал.')
    # bot.register_next_step_handler(message, haha)


def create_name_table(name):
    # разбор имени
    final_name = ""
    for i in range(len(name)):
        if name[i] != ' ':
            final_name += name[i]
        elif name[i] == " ":
            final_name += "_"
    # print(final_name)

    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    l = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table_names = []
    for i in l:
        table_names.append(i[0])

    if name not in table_names:
        create = f"""CREATE TABLE IF NOT EXISTS {final_name}(
                   id INTEGER NOT NULL,
                   fullname TEXT ,
                   subject TEXT,
                   kol INTEGER,
                   days INTEGER
                   )"""
        c.execute(create)
        conn.commit()


def create_name(name):
    # разбор имени
    final_name = ""
    for i in range(len(name)):
        if name[i] != ' ':
            final_name += name[i]
        elif name[i] == " ":
            final_name += "_"
    return final_name


def get_id(k):
    id = int(k.from_user.id)
    return id


def get_teachers(city):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    all = "SELECT * FROM id WHERE city=?"
    data = (city,)
    l = c.execute(all, data).fetchall()
    teachers_of_city = []
    for i in l:
        if i[2] == 'yes':
            teachers_of_city.append(i)
    # print('fp[f[f[f[[f[f[[f[f[[f[f[f[[f[f')

    return teachers_of_city


@bot.message_handler(commands=['start'])
def hello(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect("bot_tas.db")
    c = conn.cursor()
    bot.send_message(message.chat.id, 'Введите свои Ф.И.О.')
    fullname = message.text
    # print(fullname)

    sql = "SELECT * from id"
    l = c.execute(sql).fetchall()

    ok = True
    for i in l:
        if int(i[0] == id):
            ok = False

    if ok:
        print("Adding new user", id)
        sql = "INSERT INTO id(id) values(?)"
        c.execute(sql, (id,))

        conn.commit()
        conn.close()

    else:
        print("User", id, "already exist")

    bot.register_next_step_handler(message, get_fullname)


def get_fullname(message):
    # print()
    id = int(message.from_user.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    fullname = message.text

    insert = "UPDATE id SET fullname = ? WHERE id=? "
    data = (fullname, id)
    c.execute(insert, data)
    conn.commit()
    bot.register_next_step_handler(message, get_subject)
    bot.send_message(message.chat.id, 'Напишите название учебного предмета, который вы хотите изучать/преподавать')


def get_subject(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    subject = message.text
    # print(subject, 'before')
    subject = subject.lower()

    # print(subject, 'subject')

    bot.send_message(message.chat.id, 'Записал.')
    insert = "UPDATE id SET subject = ? WHERE id=? "
    data = (subject, id)
    c.execute(insert, data)
    conn.commit()


@bot.message_handler(commands=['get_city'])
def prepare_to_get_city(message):
    id = int(message.from_user.id)
    print(id)
    que = "Напишите название города, в котором вы учитесь/работаете (в любой момент город можно будет изменить)"
    bot.send_message(message.chat.id, que)
    bot.register_next_step_handler(message, get_city)


# добавляем в id таблицу , но нужно по городу и в city
def get_city(message):
    id = int(message.from_user.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    city = message.text.lower()
    sql = "SELECT * FROM id"
    l = c.execute(sql).fetchall()
    ins = "UPDATE id set city = ?  WHERE id=?"
    data = (city, id)
    c.execute(ins, data)
    conn.commit()
    # conn.close()
    # print('successful')
    bot.send_message(message.chat.id, 'Записал.')
    all = "SELECT * FROM cities"
    l = c.execute(all).fetchall()
    list_of_cities = []
    for i in l:
        list_of_cities.append(i[0])

    if city not in list_of_cities:
        # print('f[[f[f')
        data = (city,)
        insert = "INSERT INTO cities values(?)"
        c.execute(insert, data)
        conn.commit()
        conn.close()
        print('success')
    # print(city)


@bot.message_handler(commands=['get_teacher_status'])
def get_teach(message):
    # bot.send_message(message.chat.id, 'эта команда присваивает вам статус преподавателя, вы правда уверены в этом?')

    # def lalala(message):
    # if message.chat.type == 'private':
    #     if message.text == 'Да':
    #         bot.send_message(message.chat.id, str(random.randint(0, 100)))
    #     elif message.text == 'Нет':
    #         вот такое нужно!!!
    global id
    id = get_id(message)
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да", callback_data='good')
    item2 = types.InlineKeyboardButton("Нет", callback_data='bad')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Вы уверены, что хотите получить статус преподавателя?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    global name_of_the_pupil

    list_of_days = ["понедельник", "вторник", "среда",
                    "четверг", "пятница", "суббота",
                    "воскресенье", "✅", ]

    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    #     тут нужно написать мол создание нормального имени

    if call.data == 'файл':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="отправьте файл с вашими ответами(этот файл будет переслан учителю)",
                              reply_markup=None)
        bot.register_next_step_handler(call.message, get_answers)

    if call.data == 'текст':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="введите текст, который будет отправлен учителю",
                              reply_markup=None)
        bot.register_next_step_handler(call.message, get_text_from_pupil)

    elif call.data == 'ДА':

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="ввведите текст, который будет отправлен всем ученикам.",
                              reply_markup=None)
        bot.register_next_step_handler(call.message, get_text_from_teacher)



    elif call.data == 'НЕТ':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="успешно",
                              reply_markup=None)
        bot.send_message(call.message.chat.id, 'задание разослано вашим ученикам.')

    # тут отправка задания
    id = int(call.message.chat.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    # id = int(message.chat.id)
    select_name = "SELECT fullname from id where id=?"
    data = (id,)
    l = c.execute(select_name, data)
    for i in l:
        name = i[0]

    teacher_name = create_name(name)
    # print(teacher_name, 'teacher_name')
    path = 'c:/users/hp/PycharmProjects/TAS/files/'

    id = int(call.message.chat.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    # id = int(message.chat.id)
    select_name = "SELECT fullname from id where id=?"
    data = (id,)
    l = c.execute(select_name, data)
    for i in l:
        name = i[0]

    teacher_name = create_name(name)
    teacher = ""
    for i in teacher_name:
        teacher += latinizator(i, legend)

    # print(teacher_name, 'teacher_name')
    path = 'c:/users/hp/PycharmProjects/TAS/files/'

    if call.data in files_lol:

        path_final = path + teacher + '/' + 'scanWorks/' + call.data
        # пробежаться по папке и получить расширения всех файлов
        for dirpath, dirnames, filenames in os.walk(path_final):
            # print(filenames)
            break



        for dirpath, dirnames, filenames in os.walk(path_final):
            break
        for i in filenames:
            if i.find('test') != -1:
                a = i.rsplit('.')[1]
                break

            else:
                full_name = i

        select_ids = f"SELECT id from {teacher_name}"
        l = c.execute(select_ids).fetchall()
        list_of_id = []
        for i in l:
            list_of_id.append(i[0])

        if 'answers' and 'current_answers' in dirnames:

            for i in list_of_id:
                try:
                    uis_pdf = open(path_final + '/test.' + a, 'rb')
                    print(path_final, 'path_final')
                    bot.send_document(i, uis_pdf)
                    uis_pdf.close()
                    print(i)
                except:
                    pass


        else:
            for dirpath, dirnames, filenames in os.walk(path_final):
                break
            for i in filenames:
                file = i
                break
            uis_pdf = open(path_final + '/' + file, 'rb')
            print(path_final, 'path_final')

            for i in list_of_id:
                try:
                    # bot.send_message(i, f'задание от {teacher_name}')
                    bot.send_document(i, uis_pdf)
                except:
                    pass

        bot.send_message(call.message.chat.id, 'введите текст, который будет приложен к тесту.')
        bot.register_next_step_handler(call.message, get_text_from_teacher)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="задание разослано вашим ученикам.",
                              reply_markup=None)

    if call.data == 'Да, будет':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="отправьте два файла : в первом будет находится вариант теста с отмеченными правильными ответами, а во втором - тест без отмеченных ответов.",
                              reply_markup=None)

        bot.register_next_step_handler(call.message, get_the_first_file)
    if call.data == 'Нет, не будет':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="отправьте файл, который будет отправлен вашим ученикам.",
                              reply_markup=None)

        # print('уххухуххухух')
        bot.register_next_step_handler(call.message, get_file_from_no)

    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    global subj, Name, subject, koli
    id = call.message.chat.id
    # print(subj, 'SUUUUUUUUUUBJJJJEEEEEEEEEEEEEECTTTTTTTTTTTTTT')
    q = "SELECT subject from id WHERE id=?"
    data = (id,)
    w = c.execute(q, data)
    for i in w:
        subj = i[0]
    global Name_fsa_fsa, teacher_name_fsa_fsa
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    all = "SELECT * FROM cities"
    l = c.execute(all).fetchall()
    kol = len(l)
    cities = []
    for i in l:
        cities.append(i[0])

    # print(cities)
    try:

        if call.data == 'good':
            conn = sqlite3.connect('bot_tas.db')
            c = conn.cursor()
            update = "UPDATE id set teacher_status = ?  WHERE id=?"
            select_name = "SELECT fullname FROM id WHERE id=?"
            data = (call.message.chat.id,)
            q = c.execute(select_name, data)
            full = ""
            for i in q:
                full = i[0]

            # print(full)
            create_name_table(full)  # спрашивается: как лучше всего хранить дату?
            # ответ есть -- просто отдельным постом

            data = ("yes", id)
            c.execute(update, data)
            conn.commit()
            conn.close()
            print('success')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="^",
                                  reply_markup=None)

            bot.send_message(call.message.chat.id, 'теперь вы получили статус преподавателя.')
            bot.send_message(call.message.chat.id,
                             'введите точное время, в которое ваши ученики будут получать задания для самостоятельного решения')
            bot.register_next_step_handler(call.message, get_time)

        elif call.data == 'bad':
            # print(call.message.chat.id)
            conn = sqlite3.connect('bot_tas.db')
            c = conn.cursor()
            bot.send_message(call.message.chat.id, "вы не получили статус преподавателя.")
            update = "UPDATE id set teacher_status = ?  WHERE id=?"

            data = ("no", id)
            c.execute(update, data)
            conn.commit()
            conn.close()
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="^",
                                  reply_markup=None)

        if call.data == 'no_teachers':
            bot.send_message(call.message.chat.id,
                             'на данный момент не зарегистрирован ни один преподаватель по этому предмету.')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="^",
                                  reply_markup=None)

        conn = sqlite3.connect('bot_tas.db')
        c = conn.cursor()

        select_cities = "select * from id"  # было city
        l = c.execute(select_cities).fetchall()
        cities = []
        for i in l:
            cities.append(i[1])
        # print(cities ,'CITIES')

        # print(call.message.chat.id, 'ID')
        w = "SELECT city from id where id=?"
        data1 = (call.message.chat.id,)

        city = c.execute(w, data1)
        data = ()
        for k in city:
            data = (k[0],)

        select = "SELECT * FROM id WHERE city=?"

        # data = ('слуцк',)   #вот тут баг какой-то, должно быть что-то вместо слуцка.

        p = c.execute(select, data).fetchall()
        teachers = []
        for j in p:
            if j[2] == 'yes':
                if j[4] == subj:
                    teachers.append(j)

        l = c.execute(all).fetchall()
        kol = len(l)
        cities = []
        for i in l:
            cities.append(i[0])

        # print(cities, 'cities')

        if call.data in cities:
            for i in cities:
                if call.data == i:
                    # markup_to_cities(cities[i], message)
                    # bot.send_message(call.message.chat.id, text='привет я Егор')
                    markup_to_cities(i, call.message)

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="$",
                                          reply_markup=None)
                    # print('f[f[f[[f[f[[f[f[')
                    break

        # выбор учителя и привязка к его личной базе данных.
        x = "SELECT fullname FROM id WHERE teacher_status=?"
        data = ('yes',)
        a = c.execute(x, data).fetchall()
        teachers_from_database = []

        # print('piska')
        select_from_id = "SELECT * FROM id WHERE id=?"

        id = call.message.chat.id
        # print(id, "IFFFFF")
        d = c.execute(select_from_id, (id,)).fetchall()
        # print('piska2')

        for j in d:
            Name, subject, koli = j[3], j[4], 0

        for i in a:
            teachers_from_database.append(i[0])
        # print(teachers_from_database)
        if call.data in teachers_from_database:

            for i in teachers_from_database:
                if call.data == i:

                    # print('алохаааа')
                    create_name_table(i)
                    # bot.send_message(call.message.chat.id, 'введите дни недели через пробел, в которые вы хотите получать задания для самостоятельного решения.')
                    Name_fsa_fsa = Name
                    teacher_name_fsa_fsa = i
                    haha(call.message)
                    # bot.register_next_step_handler(call.message, haha)#call.message, Name, i ))
                    #
                    # тут нужно добавлять все в базу данных

                    id = int(call.message.chat.id)

                    print(i, 'IIIIIIIIIIIIIIIIIIIIIII')
                    full_name = create_name(i)
                    # тут должна быть функция перевода имени в _
                    select_zh = f"SELECT * FROM {full_name}"
                    a = c.execute(select_zh).fetchall()
                    zh = []
                    for p in a:
                        zh.append(p[0])
                    # print(zh, 'ZZZZZZZZZZZZZZZZZZZ')
                    # print(type(id))

                    if id not in zh:
                        insert = f"INSERT INTO {full_name} (fullname, subject, kol, id) values(?,?,?,?) "
                        data = (Name, subject, koli, id,)
                        c.execute(insert, data)
                        conn.commit()


                    else:
                        insert = f"UPDATE {full_name} SET fullname=?,  subject=?,  kol=? WHERE id=? "
                        data = (Name, subject, koli, id,)
                        c.execute(insert, data)
                        conn.commit()

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="$",
                                          reply_markup=None)

        # здесь у нас выбор дней агада
        global days, selected_days
        # print(days)
        # как так сделать, чтобы переменная запоминалась?
        if call.data == "✅":
            conn = sqlite3.connect('bot_tas.db')
            c = conn.cursor()
            name_teacher = create_name(teacher_name_fsa_fsa)
            select = f"SELECT days from {name_teacher} WHERE id=?"
            l = c.execute(select, (id,)).fetchone()[-1]
            knopka = l + ' x'

            insert = f"UPDATE {name_teacher} set days=? WHERE id=?"

            c.execute(insert, (knopka, id))
            conn.commit()

            days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "✅", ]

            selected_days = []
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='записал.', reply_markup=None)

        if call.data in list_of_days:
            if call.data != "✅":
                # print('совпадение, ', call.data)
                get_days_fromcall(call.data, call.message)  # + функция должна возвращать мне разметочку дальнейшую.

        global name_of_the_pupil
        try:
            if call.data.find('$$$') != -1:
                pass
            else:
                call_data = call.data.split('.')

                name_of_the_pupil = call_data[1]

                numb = int(call_data[0])

                fruits_complex = [
                    [{"отписать": '###@@delete_from_database@@###'},
                     {"отправить сообщение": '#$$$send_message_to_the_pupil$$$#'}], "⏪"]
                kb_fruits_complex = keyboa_maker(items=fruits_complex, copy_text_to_callback=True)

                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb_fruits_complex,
                    text="выберите одну из предложенных функций")


        except:
            pass

        if call.data == '###@@delete_from_database@@###':
            choice = [{'нет': 'ax shit please nononononononono$$$'}, {'да': 'yessssssssssssss$#'}]
            # передача айди учителя и ученика
            kb_fruits_complex = keyboa_maker(items=choice, copy_text_to_callback=True, items_in_row=2)

            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb_fruits_complex,
                text="вы уверены в том, что хотите удалить данного ученика?")

            # print(name_of_the_pupil)

        if call.data == 'yessssssssssssss$#':
            delete(call.message.chat.id, name_of_the_pupil)
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пользователь успешно удалён.'
            )

        if call.data == 'ax shit please nononononononono$$$':
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пользователь не был удалён.'
            )

        if call.data == "#$$$send_message_to_the_pupil$$$#":
            choice = [{'отправить файл и текст': '!@#$%^&*(send_document_and_text123!@#$%^&*('},
                      {'отправить только текст': '!@#$%^&*send_only_tex!@#$%^&*'}]

            kb_fruits_complex = keyboa_maker(items=choice, copy_text_to_callback=True, items_in_row=2)

            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=kb_fruits_complex,
                text="выберите вариант отправки сообщения данному ученику.")

            # get_files_from_teacher(int(call.message.chat.id), call.message)
            # зарешать с call.data, ибо она совпадает с отправкой всем и плюс спросить, нужно ли вообще отправлять файл или чисто текст

        if call.data == "!@#$%^&*send_only_tex!@#$%^&*":
            global name_of_the_teacher
            bot.edit_message_text(
                chat_id=call.message.chat.id, message_id=call.message.message_id,
                text="введите текст, который будет отправлен данному ученику.")

            bot.register_next_step_handler(call.message, xppx)
            # как это оформить и передать айди учителя + имя ученика?

            select = "SELECT fullname FROM id where id=?"
            data = (id,)
            name_of_the_teacher = c.execute(select, data).fetchone()[0]
            if name_of_the_pupil[0] == ' ':
                name_of_the_pupil = name_of_the_pupil[1::]



        if call.data == "!@#$%^&*(send_document_and_text123!@#$%^&*(":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=".",
                                  reply_markup=None)

            get_files_from_teacher(call.message.chat.id, call.message)
        # тут пробовать с call.data что-то мутить, чтобы нормально вызывать и отправлять, не используя files_lol
        # if call.data[0::-3] in files_lol:
        # тут чекать папку с этим учителем и файлы его и если ...



        sel = "SELECT fullname from id WHERE id=?"
        data = (call.message.chat.id,)
        l = c.execute(sel, data).fetchone()[0]
        teac_name = ""

        for i in l:
            if i == ' ':
                teac_name += "_"
            else:
                teac_name += i

        teac_name = latinizator(teac_name, legend)

        print(teac_name)
        path = 'C:/Users/HP/PycharmProjects/TAS/files/' + teac_name + '/scanWorks/'
        files_teacher = []

        for dirpath, dirnames, filenames in os.walk(path):
            files_teacher = dirnames
            break
        print(files_teacher)


        if call.data[0:-3] in files_teacher:


            select = "SELECT id from id where fullname=?"
            if name_of_the_pupil[0] == ' ':
                name_of_the_pupil = name_of_the_pupil[1::]

            data = (name_of_the_pupil, )
            pupil_id = c.execute(select, data).fetchone()[0]
            print(pupil_id, 'pupil_id')

            path = 'C:/Users/HP/PycharmProjects/TAS/files/' + teac_name + '/scanWorks/' + call.data[0:-3]

            for dirpath, dirnames, filenames in os.walk(path):

                break


            for dirpath, dirnames, filenames in os.walk(path):
                break
            for i in filenames:
                if i.find('test') != -1:
                    a = i.rsplit('.')[1]
                    break

                else:
                    full_name = i
            print(call.message.chat.id)
            sele = "SELECT fullname from id where id=?"
            data = (call.message.chat.id, )
            name_of_the_teacher = c.execute(sele, data).fetchone()[0]
            if 'answers' and 'current_answers' in dirnames:

                    try:
                        uis_pdf = open(path + '/test.' + a, 'rb')
                        print(uis_pdf.name, 'nameeee')
                        print(path, 'pathxxx')

                        bot.send_message(pupil_id, f'задание от лично вам от  {name_of_the_teacher}')
                        bot.send_document(pupil_id, uis_pdf)
                        uis_pdf.close()
                        print('отправил')
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text="задание выслано данному ученику.",
                                              reply_markup=None)
                        bot.send_message(call.message.chat.id, f'введите текст, который будет отправлен ученику {name_of_the_pupil}')
                        bot.register_next_step_handler(call.message, xppx)
                    except:
                        pass


            else:
                for dirpath, dirnames, filenames in os.walk(path):
                    break
                for i in filenames:
                    file = i
                    break
                uis_pdf = open(path + '/' + file, 'rb')
                print(path, 'path')


                try:
                        bot.send_message(pupil_id, f'задание от {name_of_the_teacher}')
                        bot.send_document(pupil_id, uis_pdf)
                        print('отправил')

                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                              text="задание выслано данному ученику.",
                                              reply_markup=None)

                except:
                        pass

            # bot.send_message(call.message.chat.id, 'введите текст, который будет приложен к тесту.')
            # bot.register_next_step_handler(call.message, get_text_from_teacher)
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                       text="задание разослано вашим ученикам.",
            #                       reply_markup=None)









    except Exception as e:
        print(repr(e))


# делать отдельные таблицы с пользователями для каждого учителя.

@bot.message_handler(commands=['connect_to_the_teacher'])
def connect(message):
    # global subj
    # выбор предмета ученика и последующая показка именно учителей этого предмета.
    global items, markup, c, cities
    id = int(message.from_user.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    s_subj_of_puple = "SELECT subject FROM id WHERE id = ?"
    data = (id,)
    s = c.execute(s_subj_of_puple, data)
    subj = ""
    for i in s:
        subj = i[0]
    # значит не здесб баг


    all = "SELECT city from id"
    select_cities = "select * from id"
    l = c.execute(select_cities).fetchall()
    cities = []
    c = 0
    for i in l:

        if i[1] not in cities:

            # и не здесь
            if subj == i[4]:
                c += 1
                cities.append(i[1])

    it = []
    for i in range(c):
        markup_inline = types.InlineKeyboardMarkup()
        it.append(types.InlineKeyboardButton(text=cities[i], callback_data=cities[i]))
    # markup.add(list_of_items)  # , item2)
    for j in range(c):
        markup_inline.add(it[j])



    bot.send_message(message.chat.id, 'Укажите город, в котором хотите выбрать преподавателя',
                     reply_markup=markup_inline)


@bot.message_handler(commands=['send_document'])
def first(message):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    id = int(message.chat.id)
    s = "SELECT teacher_status from id WHERE id=?"
    data = (id,)
    l = c.execute(s, data)
    for i in l:
        status = i[0]
    if status == 'yes':
        # bot.send_message(message.chat.id, 'будет ли этот тест подвергнут проверке фирменной функцией?')
        choice = ['Да, будет', 'Нет, не будет']
        kb_fruits = keyboa_maker(items=choice, copy_text_to_callback=True, auto_alignment=True)
        bot.send_message(
            chat_id=message.chat.id, reply_markup=kb_fruits,
            text='будет ли этот тест подвергнут проверке фирменной функцией?')

        fruits = keyboa_maker()


def new_folder(teacher_name):
    folders = []
    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files'):
        folders = dirnames
        break

    if teacher_name not in folders:
        try:
            path = dirpath + '/' + teacher_name

            os.mkdir(path)
        except OSError:
            print("there was an error with creating folder %s " % path)
        else:
            print("directory created successfully %s " % path)


def get_file(message):
    global folders, save_dir
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    id = int(message.chat.id)
    select = "SELECT fullname from id WHERE id=?"
    data = (id,)
    l = c.execute(select, data)
    for i in l:
        print(i)
        name = i[0]
    fullname = create_name(name)

    for dirpath, dirnames, filenames in os.walk('c:/users/hp/PycharmProjects/TAS/files'):
        folders = dirnames
        break

    file_name = message.document.file_name
    file_id = message.document.file_name
    print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""
    print(folders)
    if fullname in folders:
        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + fullname

    else:
        new_folder(fullname)
        save_dir = "c:/users/hp/PycharmProjects/TAS/files/" + fullname

    with open(save_dir + "/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, 'сохранено.')


@bot.message_handler(commands=['send_document_to_pupils'])
def find_the_last_file(message):  # но нужно передавать message
    global files_lol
    id = int(message.chat.id)
    path = 'c:/users/hp/PycharmProjects/TAS/files/'
    conn = sqlite3.connect('bot_tas.db')
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
    # print(path)
    files = []
    names = []
    for dirpath, dirnames, filenames in os.walk(path):
        names = dirnames
        files_lol = names
        # print(names,' NAMESSS')

        break

    kb_fruits = keyboa_maker(items=names, copy_text_to_callback=True, auto_alignment=True)
    bot.send_message(
        chat_id=id, reply_markup=kb_fruits,
        text="выберите файл, который вы хотите отправить ученикам.")

    # for i in range(len(datas_of_create)):
    # print(datas_of_create[i])


def get_text_from_teacher(message):
    conn = sqlite3.connect('bot_tas.db')
    text = message.text
    print(text)
    id = int(message.chat.id)
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    # id = int(message.chat.id)
    select_name = "SELECT fullname from id where id=?"
    data = (id,)
    l = c.execute(select_name, data)
    for i in l:
        name = i[0]

    teacher_name = create_name(name)

    select_ids = f"SELECT id from {teacher_name}"
    l = c.execute(select_ids).fetchall()
    list_of_id = []
    for i in l:
        list_of_id.append(i[0])
    print(list_of_id)
    for i in list_of_id:
        try:
            bot.send_message(i, f'сообщение от {teacher_name} \n{text}')
        #         здесь уже должна происходить отправка
        except:
            pass
    # for i in range(len(list_of_id)):


@bot.message_handler(commands=['answers_to_test'])
def ans(message):
    choice = ['файл', 'текст']
    # kb_fruits = keyboa_maker(items=choice, copy_text_to_callback=True, auto_alignment=True)
    bot.send_message(message.chat.id, 'ответье на тест файлом, в котором содержатся ваши ответы')
    bot.register_next_step_handler(message, answer)


def answer(message):
    path = "c:/users/hp/PycharmProjects/TAS/files/"

    id = int(message.chat.id)
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
                # print(normalized_teacher_name)
    # print(name_)
    english_name = ""
    for i in name_:
        english_name += latinizator(i, legend)
    # print(english_name)

    text_to_reply = message
    # print(message)
    print(text_to_reply)
    try:

        file_name = message.document.file_name

    except:
        bot.send_message(message.chat.id, 'вызовите функцию заново и отправьте фотографию как файл.')
        return 0
    # print(file_name)
    # print(file_name, ';aelfkl;fl;dskfl;dskfl;kdsl;fkdsl;fkds;lfkl;dskfl;dskfl;dskfl;ksdf')
    file_name2 = message.reply_to_message.document.file_name
    # print(file_name2)
    file_id_info = bot.get_file(message.reply_to_message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    # print(file_id_info.file_path)
    directory = os.listdir("c:/users/hp/PycharmProjects/TAS/files/" + english_name + '/')
    # print(directory)
    if file_name2 in directory:
        os.remove("c:/users/hp/PycharmProjects/TAS/files/" + english_name + '/' + file_name2)
    else:
        pass
    with open("c:/users/hp/PycharmProjects/TAS/files/" + english_name + '/' + file_name2, 'wb') as new_file:
        new_file.write(downloaded_file)

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
    bool = True
    # print(dirs)
    for i in dirs:
        for dirpath, dirnames, filenames in os.walk(final_path + i + '/'):
            if len(filenames) > 1:
                # for k in filenames:

                # if k.find('test') != -1:
                # print()
                for j in filenames:
                    # print(filenames)
                    if j.find('test') != -1:

                        path_to_file = dirpath + j
                        # print(path_to_file)

                        s = difference_images(path_to_file,
                                              "c:/users/hp/PycharmProjects/TAS/files/" + english_name + '/' + file_name2)
                        # print(file_name2, 'FILENAME!@@@@@@@@@@@@@')

                        if type(s) == tuple:
                            p = s[0]
                            # print(p, 'ppppppppppppppppp')
                            # тут нужно отдельно сохранять в директорию
                            # закончить проверку и соединить файлы........
                            # сохранить файл в директорию, где он был найден, но поменять название, так как рассылка может перестать работать

                            file_name = message.document.file_name
                            file_id = message.document.file_name
                            # print(file_name, file_id)
                            file_id_info = bot.get_file(message.document.file_id)
                            downloaded_file = bot.download_file(file_id_info.file_path)
                            src = file_name
                            # uploaded_answer_0()
                            w = p.rsplit('/')
                            # print(w, 'wwww')
                            print(w.pop())
                            # print(w)
                            path_to_squares = ""

                            for i in w:
                                path_to_squares += i + "/"
                            # print(path_to_squares)
                            # print(p, 'pppppppppppppppp')
                            print(path_to_squares, 'path_to_squares')

                            # print(file_name)

                            with open(path_to_squares + file_name, 'wb') as new_file:
                                new_file.write(downloaded_file)
                            list_of_files = os.listdir(path_to_squares)
                            # print(path_to_squares)
                            # print(list_of_files)
                            select_img_path = ""
                            for g in list_of_files:
                                if g.find('img') != -1:
                                    select_img_path = g
                                    break
                            # print(select_img_path)
                            uploaded_answer_0(path_to_squares + '/' + select_img_path,
                                              path_to_squares + '/' + 'current_answers',
                                              path_to_squares + '/' + 'answers')

                            uploaded_answer_1(path_to_squares + file_name, path_to_squares + '/' + 'current_answers',
                                              path_to_squares + '/' + 'answers')
                            # print(first, second)
                            current_answers = 0
                            result = 0
                            if len(first) != len(second):
                                print(
                                    'алгоритму не удалось найти одинаковое количество квадратов в обоих файлах.')
                            else:

                                for i in range(len(first)):
                                    if first[i] == 1:
                                        current_answers += 1
                                        # print(array, 'ARRAY')
                                    if first[i] == 1 and second[i] == 1:
                                        result += 1
                                ocenka = f'итоговая предпологаемая оценка {int_r(result * 10 / current_answers)}'
                                print(f'итоговая предпологаемая оценка {int_r(result * 10 / current_answers)}')
                                bot.send_message(message.chat.id, ocenka)
                                # ищем имя ученика
                                select = "SELECT fullname from id WHERE id=?"
                                name_of_pupil = c.execute(select, (id,)).fetchone()[0]
                                message_id = message.message_id
                                print(name_of_pupil)
                                select_teacher_name = "SELECT id from id where fullname=?"
                                teacher_id = c.execute(select_teacher_name, (normalized_teacher_name,)).fetchone()[0]
                                bot.forward_message(teacher_id, id, message_id)
                                ocenka = f'итоговая предпологаемая оценка у {name_of_pupil} - {int_r(result * 10 / current_answers)}'
                                bot.send_message(teacher_id, ocenka)
                                # пересылка учителю вместе с ответом правильным
                                break
                                # поиск айди учителя , отправка ему документа и предпологаемой оценки.
                            # with open('')

                            print('yesss')

            elif len(filenames) == 1 and bool == True:

                # print(final_path + i + '/')
                # s = difference_images('c:/users/hp/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/Parks Calvert Vaux.jpg', "c:/users/hp/PycharmProjects/TAS/files/"+ english_name + '/scanWorks/' + i + '/' + filenames[0])
                # ищем имя ученика
                select = "SELECT fullname from id WHERE id=?"
                name_of_pupil = c.execute(select, (id,)).fetchone()[0]
                message_id = message.message_id
                print(name_of_pupil)
                select_teacher_name = "SELECT id from id where fullname=?"
                teacher_id = c.execute(select_teacher_name, (normalized_teacher_name,)).fetchone()[0]
                bot.forward_message(teacher_id, id, message_id)
                ocenka = f'решенный тест от {name_of_pupil}'
                # try:

                bot.send_message(teacher_id, ocenka)
                bool = False

                # except:
                #     pass

    # сохранение основного файла после того, как найдется правильная директория
    '''file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""
    with open('')'''


@bot.message_handler(commands=['get_pupils'])
def ha(message):
    get_all_pupils(message.chat.id)
    # пофиксить херню, почему он выдает еще и про тест эту фигню


print('запущено.')
bot.polling(none_stop=True)
