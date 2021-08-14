# этот будет как рабочий вариант если чё.

import telebot
import os.path, time
import sqlite3
from datetime import datetime
from keyboa import keyboa_maker
global files_lol
files_lol = []
file = 'C:/Users/User/PycharmProjects/TAS/files/Жарский_Егор_Александрович/20200925_170144.docx'
# print("last modified: %s" % time.ctime(os.path.getmtime(file)))
# print("created: %s" % time.ctime(os.path.getctime(file))) #вот это нужно

bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')


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

    teacher_name = create_name(name)
    # print(teacher_name)
    path = path + teacher_name + '/'
    # print(path)
    files = []
    for dirpath, dirnames, filenames in os.walk(path):

        files = filenames
        print(files, "FILES")
        files_lol = files
        break
    datas_of_create = []
    for i in files:
        final_path = path + i
        # print(final_path)
        # datas_of_create.append(datetime.fromtimestamp(os.path.getctime(final_path)).strftime('%Y-%m-%d %H:%M:%S'))
        #нужно как-то разбирать дату на то, чтобы получилось сравнивать их
    #     нужно сделать типо чтобы учитель выбирал сам файлы на отправку

    kb_fruits = keyboa_maker(items=files, copy_text_to_callback=True, auto_alignment=True)
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
    # print(teacher_name, 'teacher_name')
    path = 'C:/Users/User/PycharmProjects/TAS/files/'


    if call.data in files_lol:
        path_final = path + teacher_name + '/' + call.data
        print(path_final, 'path_final')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="производится отправка.",
                              reply_markup=None)

        choice = ['ДА', 'НЕТ']
        kb_fruits = keyboa_maker(items=choice, copy_text_to_callback=True, auto_alignment=True)
        bot.send_message(
            chat_id=id, reply_markup=kb_fruits,
            text='не хотите ли вы прибавить какой-либо текст, который будет отправлен ученикам?')

        # вот это оформить в отдельную функцию для отправки срочного сообщения

        select_ids = f"SELECT id from {teacher_name}"
        l = c.execute(select_ids).fetchall()
        list_of_id = []
        for i in l:
            list_of_id.append(i[0])
        print(list_of_id)
#         здесь уже должна происходить отправка
        '''uis_pdf = open('files/' + uis_login + '.pdf', 'rb')
bot.send_document(message.chat.id, uis_pdf)
uis_pdf.close()'''
        for i in range(len(list_of_id)):
            uis_pdf = open(path_final, 'rb')
            try:
                bot.send_document(list_of_id[i], uis_pdf)
            except:
                pass
        bot.send_message(call.message.chat.id, 'задание разослано вашим ученикам.')


@bot.message_handler(commands=['answers_to_test'])
def ans(message):
    choice = ['файл', 'текст']
    kb_fruits = keyboa_maker(items=choice, copy_text_to_callback=True, auto_alignment=True)
    bot.send_message(
        chat_id=message.chat.id, reply_markup=kb_fruits,
        text='выберите, каким способом будут отправлены ответы на тест.')



    bot.register_next_step_handler(message, answer)
def answer(message):
    text_to_reply = message.text


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
        bot.send_message(message.chat.id, 'отправьте файл, в котором будут выделены задания для учащихся')

        bot.register_next_step_handler(message, get_file)
    else:
        bot.send_message(message.chat.id, 'Вы не обладаете статусом учителя, чтобы воспользоваться данной функцией.')


bot.polling(none_stop=True)
