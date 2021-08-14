#создавать новую директорию для каждого нового тестика, там будут answers и current_answers, сам тестовый файл.
import find_squares
import telebot
import os.path, time
import sqlite3
from datetime import datetime
from PIL import Image, ImageChops
from keyboa import keyboa_maker
global files_lol, konch
global first
first = []
global second
second = []


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num




konch = ""
files_lol = []



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
    result=ImageChops.difference(image_1, image_2).getbbox()
    if result==None:
        return img1,'matches'
    else:
        return 'no matches'
    return



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




# ну тут прописать поиск квадратиков Артура..........
# print("last modified: %s" % time.ctime(os.path.getmtime(file)))
# print("created: %s" % time.ctime(os.path.getctime(file))) #вот это нужно

bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')

def new_scanWorks_folder(filename, fullname):
    global papki# создаем в папке учителя папку scanWorks, а в ней answers and current answers
    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
        folders = dirnames
        break
        # print(filenames)
    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files/' + fullname):
        papki = dirnames

        break

    if 'scanWorks' not in papki:
        path = 'C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/'
        try:
            os.mkdir(path)
        except:
            pass
    # теперь нужно создавать подпапку каждого из файлов, чтобы там хранить ответы на тесты
    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/'):
        dirs_of_scan = dirnames
        break
    if len(dirs_of_scan) == 0 or filename not in dirs_of_scan:
        os.mkdir('C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename)
        os.mkdir('C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename + '/answers/')
        os.mkdir('C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename + '/current_answers/')
#     тут теперь сохранять файл в папку
    src = filename
    save_dir = 'C:/Users/User/PycharmProjects/TAS/files/' + fullname + '/scanWorks/' + filename

    print(fullname)
    print(src, 'FILENAME')
    #или лучше сохранять в гет ферст файл?
    # with open(save_dir + "/" + src, 'wb') as new_file:
    #     new_file.write(downloaded_file)





def new_folder(teacher_name):
    folders = []
    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
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


def get_text_from_pupil(message): #+

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

def get_the_first_file(message):
    global konch
    global folders, save_dir
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, 'FILENAMEEEE')
    #тут нада сохранять его в отдельную папку с учителем и сразу же обрабатывать.


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

    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
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

        save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name

    else:
        new_folder(latin_name)
        save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name
    #здесь сохранить файл в папку с названием самого файла
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



    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
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

        save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name

    else:
        new_folder(latin_name)
        save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/' + file_name
        # здесь сохранить файл в папку с названием самого файла
        # img -- это фото ответов

    # print(a, 'FFFFFFFFFFFFFFFFFFFFFFF')
    konch = save_dir + "/"
    for dirpath, dirnames, filenames in os.walk("C:/Users/User/PycharmProjects/TAS/files/" + latin_name + '/scanWorks/'):
        break
    print(dirnames)

    if len(dirnames) == 0 or file_name not in dirnames:
        os.mkdir('C:/Users/User/PycharmProjects/TAS/files/' + latin_name + '/scanWorks/' + file_name)


    with open(save_dir + "/" + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    print('уххуху')

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

    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
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
            save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + fullname

    else:
            new_folder(fullname)
            save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + fullname

    with open(save_dir + "/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, 'сохранено.')

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





    file_name = message.document.file_name
    file_id = message.document.file_name
    print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""
    # print(folders)
    # if fullname in folders:
    #         save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + fullname
    #
    # else:
    #         new_folder(fullname)
    #         save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + fullname
    #
    # with open(save_dir + "/" + src, 'wb') as new_file:
    #     new_file.write(downloaded_file)
#


def create_name(name):
    # разбор имени
    final_name = ""
    for i in range(len(name)):
        if name[i] != ' ':
            final_name += name[i]
        elif name[i] == " ":
            final_name += "_"
    return final_name


@bot.message_handler(commands=['send_document_to_pupils'])



def find_the_last_file(message):#но нужно передавать message
    global files_lol
    id = int(message.chat.id)
    path = 'C:/Users/User/PycharmProjects/TAS/files/'
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    # id = int(message.chat.id)
    select_name = "SELECT fullname from id where id=?"
    data = (id, )
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
    '''datas_of_create = []
    for i in files:
        final_path = path + i'''
        # print(final_path)
        # datas_of_create.append(datetime.fromtimestamp(os.path.getctime(final_path)).strftime('%Y-%m-%d %H:%M:%S'))
        #нужно как-то разбирать дату на то, чтобы получилось сравнивать их
    #     нужно сделать типо чтобы учитель выбирал сам файлы на отправку

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




    # print(teacher_name)





@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()
    print(call.data, 'call.data')
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
                              text="зочим ты нит нажал",
                              reply_markup=None)

    #тут отправка задания
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
    path = 'C:/Users/User/PycharmProjects/TAS/files/'


    if call.data in files_lol:
        # короче, я мудак, тут короче нужно не call.data, а test.?
        path_final = path + teacher + '/' + 'scanWorks/' + call.data
        #пробежаться по папке и получить расширения всех файлов
        for dirpath, dirnames, filenames in os.walk(path_final):
            # print(filenames)
            break

        # print(call.data, 'CALLDATA')

        for dirpath, dirnames, filenames in os.walk(path_final):
            break
        for i in filenames:
            if i.find('test') != -1:
                a = i.rsplit('.')[1]
                full_name = i
                # print(full_name, 'full_name')
                break

            else:
                full_name = i
                # print(full_name, 'full_name')
        print(full_name)
        print(path_final, 'patpj')

        select_ids = f"SELECT id from {teacher_name}"
        l = c.execute(select_ids).fetchall()
        list_of_id = []
        for i in l:
            list_of_id.append(i[0])
        print(list_of_id)



        if 'answers' and 'current_answers' in dirnames:

            uis_pdf = open(path_final + '/test.' + a, 'rb')
            print(path_final, 'path_final')
            print(uis_pdf.name, 'ухуххуху')
            # uis_pdf.close()
            # uis_pdf = open(path_final, 'rb')
            # print(uis_pdf.name)
            for i in list_of_id:
                try:
                    # bot.send_message(i, f'задание от {teacher_name}')
                    bot.send_document(i, uis_pdf)
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




        #отсюда пошло мое новое
    if call.data == 'Да, будет':
           bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="отправьте два файла : в первом будет находится вариант теста с отмеченными правильными ответами, а во втором - тест без отмеченных ответов.",
                          reply_markup=None)

           bot.register_next_step_handler(call.message, get_the_first_file)
    if call.data == 'Нет, не будет':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="отправьте файл, который будет отправлен вашим ученикам.",
                              reply_markup=None)

        print('уххухуххухух')
        bot.register_next_step_handler(call.message, get_file_from_no)


@bot.message_handler(commands=['answers_to_test'])
def ans(message):
    choice = ['файл', 'текст']
    # kb_fruits = keyboa_maker(items=choice, copy_text_to_callback=True, auto_alignment=True)
    bot.send_message(message.chat.id, 'ответье на тест файлом, в котором содержатся ваши ответы')
    bot.register_next_step_handler(message, answer)

def answer(message):
    path = "C:/Users/User/PycharmProjects/TAS/files/"

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

    file_name = message.document.file_name
    # print(file_name, ';aelfkl;fl;dskfl;dskfl;kdsl;fkdsl;fkds;lfkl;dskfl;dskfl;dskfl;ksdf')
    file_name2 = message.reply_to_message.document.file_name
    # print(file_name2)
    file_id_info = bot.get_file(message.reply_to_message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    # print(file_id_info.file_path)
    directory = os.listdir("C:/Users/User/PycharmProjects/TAS/files/" + english_name + '/')
    # print(directory)
    if file_name2 in directory:
        os.remove("C:/Users/User/PycharmProjects/TAS/files/" + english_name + '/' + file_name2)
    else:
        pass
    with open("C:/Users/User/PycharmProjects/TAS/files/" + english_name + '/' + file_name2, 'wb') as new_file:
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

                                s = difference_images(path_to_file, "C:/Users/User/PycharmProjects/TAS/files/" + english_name + '/' + file_name2)
                                # print(file_name2, 'FILENAME!@@@@@@@@@@@@@')

                                if type(s) == tuple:
                                    p = s[0]
                                    # print(p, 'ppppppppppppppppp')
                                    # тут нужно отдельно сохранять в директорию
                                    #закончить проверку и соединить файлы........
                                    #сохранить файл в директорию, где он был найден, но поменять название, так как рассылка может перестать работать

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
                                    uploaded_answer_0(path_to_squares + '/' + select_img_path, path_to_squares + '/' + 'current_answers',  path_to_squares + '/' + 'answers')
                                    #damn
                                    uploaded_answer_1(path_to_squares + file_name, path_to_squares + '/' + 'current_answers',  path_to_squares + '/' + 'answers')
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
                                        #ищем имя ученика
                                        select = "SELECT fullname from id WHERE id=?"
                                        name_of_pupil = c.execute(select, (id, )).fetchone()[0]
                                        message_id = message.message_id
                                        print(name_of_pupil)
                                        select_teacher_name = "SELECT id from id where fullname=?"
                                        teacher_id = c.execute(select_teacher_name, (normalized_teacher_name, )).fetchone()[0]
                                        bot.forward_message(teacher_id, id, message_id)
                                        ocenka = f'итоговая предпологаемая оценка у {name_of_pupil} - {int_r(result * 10 / current_answers)}'
                                        bot.send_message(teacher_id, ocenka)
                                        #пересылка учителю вместе с ответом правильным
                                        break
                                        #поиск айди учителя , отправка ему документа и предпологаемой оценки.
                                    # with open('')

                                    print('yesss')

            elif len(filenames) == 1:
                print()
                print()
                print(i, 'iiiiii')
                print(filenames)
                print(path_to_file, 'akfo')
                print("C:/Users/User/PycharmProjects/TAS/files/" + english_name + '/scanWorks/' + i + '/' + filenames[0])
                print()

                # print(final_path + i + '/')
                s = difference_images('C:/Users/User/PycharmProjects/TAS/files/Zharskiy_Egor_Aleksandrovich/Parks Calvert Vaux.jpg', "C:/Users/User/PycharmProjects/TAS/files/"+ english_name + '/scanWorks/' + i + '/' + filenames[0])

                print(s)

                print(filenames)
    #сохранение основного файла после того, как найдется правильная директория
    '''file_name = message.document.file_name
    file_id = message.document.file_name
    # print(file_name, file_id)
    file_id_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    src = file_name
    save_dir = ""
    with open('')'''

# print(c)

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
        # bot.send_message(message.chat.id, 'отправьте файл, в котором будут выделены задания для учащихся')

        # bot.register_next_step_handler(message, get_file)
    # else:
    #     bot.send_message(message.chat.id, 'Вы не обладаете статусом учителя, чтобы воспользоваться данной функцией.')

print('запущено')
bot.polling(none_stop=True)
