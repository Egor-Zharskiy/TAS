import telebot
import sqlite3
import os
import keyboa
from keyboa import keyboa_maker
import codecs

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
    conn = sqlite3.connect(path + '/' + 'bot_tas.db')
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
    select = f"SELECT * FROM {sql_name}"
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

    # отделять имя от точки с цифрой, потом как-то сделать функции удаления, отправки определенному ученику файла.


def delete(id, name):
    conn = sqlite3.connect('bot_tas.db')
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


    dal = f"DELETE FROM {name_of_teacher} WHERE id=?"

    data = (id_of_pupil,)

    c.execute(dal, data)

    conn.commit()

    select = "SELECT * FROM id"

    bot.send_message(id_of_pupil, f'преподаватель {l} забрал у вас доступ от своих заданий.')
    conn.close()


def send_message_to_the_pupil(id, name, text):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    sql = "SELECT id FROM id WHERE fullname=?"
    data = (name,)
    name_of_the_pupil = c.execute(sql, data).fetchone()[0]
    # тут надо отправлять файл из списка всех отправленных учителем файлов


def get_files_from_teacher(id, message):

    # global files_lol

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


#при каждом отправленном тесте нужно заносить в файл оценку ученика, потом функцией вызывать что-то наподобие списка


def enter_mark(w, path, ocenka):

    f = codecs.open(f"{path}"
    #тут эксель нужооооооон
             "/marks_of_the_pupils!!@#$%^&.txt", mode='r', encoding='utf-8')
    s = f.read().splitlines()
    print(s)

    f.close()

    flag = True
    if len(s) == 0:
        f = open(path + '/marks_of_the_pupils!!@#$%^&.txt', 'w')
        print(w + f' -  {str(ocenka)}')
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
            print(s, flag)
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
            print(flag, s)
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


# enter_mark('Жарский Никита Александрович', 'C:/Users/HP/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/scanWorks/teacher.jpg', 6)
