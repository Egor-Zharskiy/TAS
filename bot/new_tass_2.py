import telebot
from telebot import types
import sqlite3
from keyboa import keyboa_maker

global Name_fsa_fsa, teacher_name_fsa_fsa
import os
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
items = ['item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10', 'item11',
         'item12', 'item13', 'item14', 'item15', 'item16', 'item17', 'item18', 'item19', 'item20', 'item21', 'item22',
         'item23', 'item24', 'item25', 'item26', 'item27', 'item28', 'item29', 'item30', 'item31', 'item32', 'item33',
         'item34', 'item35', 'item36', 'item37', 'item38', 'item39', 'item40', 'item41', 'item42', 'item43', 'item44',
         'item45', 'item46', 'item47', 'item48', 'item49', 'item50', 'item51', 'item52', 'item53', 'item54', 'item55',
         'item56', 'item57', 'item58', 'item59', 'item60', 'item61', 'item62', 'item63', 'item64', 'item65', 'item66',
         'item67', 'item68', 'item69', 'item70', 'item71', 'item72', 'item73', 'item74', 'item75', 'item76', 'item77',
         'item78', 'item79', 'item80', 'item81', 'item82', 'item83', 'item84', 'item85', 'item86', 'item87', 'item88',
         'item89', 'item90', 'item91', 'item92', 'item93', 'item94', 'item95', 'item96', 'item97', 'item98', 'item99',
         'item100', 'item101', 'item102', 'item103', 'item104', 'item105', 'item106', 'item107', 'item108', 'item109',
         'item110', 'item111', 'item112', 'item113', 'item114', 'item115', 'item116', 'item117', 'item118', 'item119',
         'item120', 'item121', 'item122', 'item123', 'item124', 'item125', 'item126', 'item127', 'item128', 'item129',
         'item130', 'item131', 'item132', 'item133', 'item134', 'item135', 'item136', 'item137', 'item138', 'item139',
         'item140', 'item141', 'item142', 'item143', 'item144', 'item145', 'item146', 'item147', 'item148', 'item149',
         'item150', 'item151', 'item152', 'item153', 'item154', 'item155', 'item156', 'item157', 'item158', 'item159',
         'item160', 'item161', 'item162', 'item163', 'item164', 'item165', 'item166', 'item167', 'item168', 'item169',
         'item170', 'item171', 'item172', 'item173', 'item174', 'item175', 'item176', 'item177', 'item178', 'item179',
         'item180', 'item181', 'item182', 'item183', 'item184', 'item185', 'item186', 'item187', 'item188', 'item189',
         'item190', 'item191', 'item192', 'item193', 'item194', 'item195', 'item196', 'item197', 'item198', 'item199',
         'item200', 'item201', 'item202', 'item203', 'item204', 'item205', 'item206', 'item207', 'item208', 'item209',
         'item210', 'item211', 'item212', 'item213', 'item214', 'item215', 'item216', 'item217', 'item218', 'item219',
         'item220', 'item221', 'item222', 'item223', 'item224', 'item225', 'item226', 'item227', 'item228', 'item229',
         'item230', 'item231', 'item232', 'item233', 'item234', 'item235', 'item236', 'item237', 'item238', 'item239',
         'item240', 'item241', 'item242', 'item243', 'item244', 'item245', 'item246', 'item247', 'item248', 'item249',
         'item250', 'item251', 'item252', 'item253', 'item254', 'item255', 'item256', 'item257', 'item258', 'item259',
         'item260', 'item261', 'item262', 'item263', 'item264', 'item265', 'item266', 'item267', 'item268', 'item269',
         'item270', 'item271', 'item272', 'item273', 'item274', 'item275', 'item276', 'item277', 'item278', 'item279',
         'item280', 'item281', 'item282', 'item283', 'item284', 'item285', 'item286', 'item287', 'item288', 'item289',
         'item290', 'item291', 'item292', 'item293', 'item294', 'item295', 'item296', 'item297', 'item298', 'item299',
         'item300', 'item301', 'item302', 'item303', 'item304', 'item305', 'item306', 'item307', 'item308', 'item309',
         'item310', 'item311', 'item312', 'item313', 'item314', 'item315', 'item316', 'item317', 'item318', 'item319',
         'item320', 'item321', 'item322', 'item323', 'item324', 'item325', 'item326', 'item327', 'item328', 'item329',
         'item330', 'item331', 'item332', 'item333', 'item334', 'item335', 'item336', 'item337', 'item338', 'item339',
         'item340', 'item341', 'item342', 'item343', 'item344', 'item345', 'item346', 'item347', 'item348', 'item349',
         'item350', 'item351', 'item352', 'item353', 'item354', 'item355', 'item356', 'item357', 'item358', 'item359',
         'item360', 'item361', 'item362', 'item363', 'item364', 'item365', 'item366', 'item367', 'item368', 'item369',
         'item370', 'item371', 'item372', 'item373', 'item374', 'item375', 'item376', 'item377', 'item378', 'item379',
         'item380', 'item381', 'item382', 'item383', 'item384', 'item385', 'item386', 'item387', 'item388', 'item389',
         'item390', 'item391', 'item392', 'item393', 'item394', 'item395', 'item396', 'item397', 'item398', 'item399',
         'item400', 'item401', 'item402', 'item403', 'item404', 'item405', 'item406', 'item407', 'item408', 'item409',
         'item410', 'item411', 'item412', 'item413', 'item414', 'item415', 'item416', 'item417', 'item418', 'item419',
         'item420', 'item421', 'item422', 'item423', 'item424', 'item425', 'item426', 'item427', 'item428', 'item429',
         'item430', 'item431', 'item432', 'item433', 'item434', 'item435', 'item436', 'item437', 'item438', 'item439',
         'item440', 'item441', 'item442', 'item443', 'item444', 'item445', 'item446', 'item447', 'item448', 'item449',
         'item450', 'item451', 'item452', 'item453', 'item454', 'item455', 'item456', 'item457', 'item458', 'item459',
         'item460', 'item461', 'item462', 'item463', 'item464', 'item465', 'item466', 'item467', 'item468', 'item469',
         'item470', 'item471', 'item472', 'item473', 'item474', 'item475', 'item476', 'item477', 'item478', 'item479',
         'item480', 'item481', 'item482', 'item483', 'item484', 'item485', 'item486', 'item487', 'item488', 'item489',
         'item490', 'item491', 'item492', 'item493', 'item494', 'item495', 'item496', 'item497', 'item498', 'item499',
         'item500', 'item501', 'item502', 'item503', 'item504', 'item505', 'item506', 'item507', 'item508', 'item509',
         'item510', 'item511', 'item512', 'item513', 'item514', 'item515', 'item516', 'item517', 'item518', 'item519',
         'item520', 'item521', 'item522', 'item523', 'item524', 'item525', 'item526', 'item527', 'item528', 'item529',
         'item530', 'item531', 'item532', 'item533', 'item534', 'item535', 'item536', 'item537', 'item538', 'item539',
         'item540', 'item541', 'item542', 'item543', 'item544', 'item545', 'item546', 'item547', 'item548', 'item549',
         'item550', 'item551', 'item552', 'item553', 'item554', 'item555', 'item556', 'item557', 'item558', 'item559',
         'item560', 'item561', 'item562', 'item563', 'item564', 'item565', 'item566', 'item567', 'item568', 'item569',
         'item570', 'item571', 'item572', 'item573', 'item574', 'item575', 'item576', 'item577', 'item578', 'item579',
         'item580', 'item581', 'item582', 'item583', 'item584', 'item585', 'item586', 'item587', 'item588', 'item589',
         'item590', 'item591', 'item592', 'item593', 'item594', 'item595', 'item596', 'item597', 'item598', 'item599',
         'item600', 'item601', 'item602', 'item603', 'item604', 'item605', 'item606', 'item607', 'item608', 'item609',
         'item610', 'item611', 'item612', 'item613', 'item614', 'item615', 'item616', 'item617', 'item618', 'item619',
         'item620', 'item621', 'item622', 'item623', 'item624', 'item625', 'item626', 'item627', 'item628', 'item629',
         'item630', 'item631', 'item632', 'item633', 'item634', 'item635', 'item636', 'item637', 'item638', 'item639',
         'item640', 'item641', 'item642', 'item643', 'item644', 'item645', 'item646', 'item647', 'item648', 'item649',
         'item650', 'item651', 'item652', 'item653', 'item654', 'item655', 'item656', 'item657', 'item658', 'item659',
         'item660', 'item661', 'item662', 'item663', 'item664', 'item665', 'item666', 'item667', 'item668', 'item669',
         'item670', 'item671', 'item672', 'item673', 'item674', 'item675', 'item676', 'item677', 'item678', 'item679',
         'item680', 'item681', 'item682', 'item683', 'item684', 'item685', 'item686', 'item687', 'item688', 'item689',
         'item690', 'item691', 'item692', 'item693', 'item694', 'item695', 'item696', 'item697', 'item698', 'item699',
         'item700', 'item701', 'item702', 'item703', 'item704', 'item705', 'item706', 'item707', 'item708', 'item709',
         'item710', 'item711', 'item712', 'item713', 'item714', 'item715', 'item716', 'item717', 'item718', 'item719',
         'item720', 'item721', 'item722', 'item723', 'item724', 'item725', 'item726', 'item727', 'item728', 'item729',
         'item730', 'item731', 'item732', 'item733', 'item734', 'item735', 'item736', 'item737', 'item738', 'item739',
         'item740', 'item741', 'item742', 'item743', 'item744', 'item745', 'item746', 'item747', 'item748', 'item749',
         'item750', 'item751', 'item752', 'item753', 'item754', 'item755', 'item756', 'item757', 'item758', 'item759',
         'item760', 'item761', 'item762', 'item763', 'item764', 'item765', 'item766', 'item767', 'item768', 'item769',
         'item770', 'item771', 'item772', 'item773', 'item774', 'item775', 'item776', 'item777', 'item778', 'item779',
         'item780', 'item781', 'item782', 'item783', 'item784', 'item785', 'item786', 'item787', 'item788', 'item789',
         'item790', 'item791', 'item792', 'item793', 'item794', 'item795', 'item796', 'item797', 'item798', 'item799',
         'item800', 'item801', 'item802', 'item803', 'item804', 'item805', 'item806', 'item807', 'item808', 'item809',
         'item810', 'item811', 'item812', 'item813', 'item814', 'item815', 'item816', 'item817', 'item818', 'item819',
         'item820', 'item821', 'item822', 'item823', 'item824', 'item825', 'item826', 'item827', 'item828', 'item829',
         'item830', 'item831', 'item832', 'item833', 'item834', 'item835', 'item836', 'item837', 'item838', 'item839',
         'item840', 'item841', 'item842', 'item843', 'item844', 'item845', 'item846', 'item847', 'item848', 'item849',
         'item850', 'item851', 'item852', 'item853', 'item854', 'item855', 'item856', 'item857', 'item858', 'item859',
         'item860', 'item861', 'item862', 'item863', 'item864', 'item865', 'item866', 'item867', 'item868', 'item869',
         'item870', 'item871', 'item872', 'item873', 'item874', 'item875', 'item876', 'item877', 'item878', 'item879',
         'item880', 'item881', 'item882', 'item883', 'item884', 'item885', 'item886', 'item887', 'item888', 'item889',
         'item890', 'item891', 'item892', 'item893', 'item894', 'item895', 'item896', 'item897', 'item898', 'item899',
         'item900', 'item901', 'item902', 'item903', 'item904', 'item905', 'item906', 'item907', 'item908', 'item909',
         'item910', 'item911', 'item912', 'item913', 'item914', 'item915', 'item916', 'item917', 'item918', 'item919',
         'item920', 'item921', 'item922', 'item923', 'item924', 'item925', 'item926', 'item927', 'item928', 'item929',
         'item930', 'item931', 'item932', 'item933', 'item934', 'item935', 'item936', 'item937', 'item938', 'item939',
         'item940', 'item941', 'item942', 'item943', 'item944', 'item945', 'item946', 'item947', 'item948', 'item949',
         'item950', 'item951', 'item952', 'item953', 'item954', 'item955', 'item956', 'item957', 'item958', 'item959',
         'item960', 'item961', 'item962', 'item963', 'item964', 'item965', 'item966', 'item967', 'item968', 'item969',
         'item970', 'item971', 'item972', 'item973', 'item974', 'item975', 'item976', 'item977', 'item978', 'item979',
         'item980', 'item981', 'item982', 'item983', 'item984', 'item985', 'item986', 'item987', 'item988', 'item989',
         'item990', 'item991', 'item992', 'item993', 'item994', 'item995', 'item996', 'item997', 'item998', 'item999', ]
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


bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')


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


def latinizator(letter, dic):
    for i, j in dic.items():
        letter = letter.replace(i, j)
    return letter





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


def get_days_fromcall(day, message):  # , name, teacher_name):
    # day = day.split(' ')
    print(teacher_name_fsa_fsa)
    teacher_fullname = create_name(teacher_name_fsa_fsa)

    print(day)

    days = {"понедельник": u'0', "вторник": u"1", "среда": u"2", "четверг": u"3", "пятница": u"4", "суббота": u"5",
            "воскресенье": u"6"}

    conn = sqlite3.connect('bot_tas.db')
    q = conn.cursor()

    for i in range(len(day)):
        day[i] = day[i].lower()

    c = list(set(day) & set(days))
    id = int(message.chat.id)
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
            str_of_days += str(res[j])

    insert = f"UPDATE {teacher_fullname} set days=? WHERE id=?"
    data = (str_of_days, id)

    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    c.execute(insert, data)
    conn.commit()
    print('success')
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

    # else:
    #     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


# def cities(message):


# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     if message.chat.type == 'private':
#         if message.text == 'Да':
#             bot.send_message(message.chat.id, str(random.randint(0, 100)))
#         elif message.text == 'Нет':
#             вот такое нужно!!!
# markup = types.InlineKeyboardMarkup(row_width=2)
# item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
# item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
#
# markup.add(item1, item2)
#
# bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
# else:
#     bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
#


# вот здесь разобраться и добавлять в базу данных как учителя или как ученика.
@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    conn = sqlite3.connect('bot_tas.db')
    c = conn.cursor()

    #     тут нужно написать мол создание нормального имени
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
    path = 'C:/Users/User/PycharmProjects/TAS/files/'
    ril_teacher_name = ""
    for i in teacher_name:
        ril_teacher_name += latinizator(i, legend)

    if call.data in files_lol:
        path_final = path + ril_teacher_name + '/' + call.data
        print(path_final, 'path_final')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="производится отправка.",
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
            print(call.message.chat.id)
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
            # print(j, 'jJJJJJJJJJJJJJJJJJJJJJJJJJJ')
            Name, subject, koli = j[3], j[4], 0

        for i in a:
            teachers_from_database.append(i[0])
        # print(teachers_from_database)
        if call.data in teachers_from_database:
            print(call.data, 'CALLDATDAATDATDTADTATDATDATDTAD')
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
        print(days)
        # как так сделать, чтобы переменная запоминалась?
        if call.data == "✅":
            conn = sqlite3.connect('bot_tas.db')
            c = conn.cursor()

            days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "✅", ]
            print(selected_days, "SELECTED DAYS")
            get_days_fromcall(selected_days, call.message)

            selected_days = []
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='записал.', reply_markup=None)

        for i in range(len(days)):

            if call.data == days[i]:
                if call.data != "✅":
                    selected_days.append(days[i])
                    print(selected_days, 'selected_days')
                    days[i] = '✓'

                    kb_fruits = keyboa_maker(items=days, copy_text_to_callback=True, auto_alignment=True)

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text='выберите дни для рассылки заданий.', reply_markup=kb_fruits)


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
    # print(subj, "SUBJJJJJJJJJJJJJJJJJEEEEEEEEEEEEEEEEEECTTTTTTTTTTTTTTTTTTT")

    all = "SELECT city from id"
    select_cities = "select * from id"
    l = c.execute(select_cities).fetchall()
    cities = []
    c = 0
    for i in l:

        if i[1] not in cities:
            # print(subj, "SUBJJJJJJJJJJJJJJJJJEEEEEEEEEEEEEEEEEECTTTTTTTTTTTTTTTTTTT")
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

    # print(cities)

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
        bot.send_message(message.chat.id, 'отправьте файл, в котором будут выделены задания для учащихся')
        bot.register_next_step_handler(message, get_file)
    else:
        bot.send_message(message.chat.id, 'Вы не обладаете статусом учителя, чтобы воспользоваться данной функцией.')


def new_folder(teacher_name):
    folders = []
    for dirpath, dirnames, filenames in os.walk('C:/Users/User/PycharmProjects/TAS/files'):
        folders = dirnames
        break
    latino_teacher_name = ""
    for i in teacher_name:
        latino_teacher_name += latinizator(i, legend)


    if latino_teacher_name not in folders:
        try:
            path = dirpath + '/' + latino_teacher_name

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
    teacher_name = ""
    for i in fullname:
        teacher_name += latinizator(i, legend)

    if teacher_name in folders:
            save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + teacher_name

    else:
            new_folder(teacher_name)
            save_dir = "C:/Users/User/PycharmProjects/TAS/files/" + teacher_name

    with open(save_dir + "/" + src, 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, 'сохранено.')


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
    ril_teacher_name = ""
    for i in teacher_name:
        ril_teacher_name += latinizator(i, legend)
    # print(teacher_name)
    path = path + ril_teacher_name + '/'
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


    normalized_name = ""
    for i in range(len(teacher_name)):
        if teacher_name[i] != '_':
            normalized_name += teacher_name[i]
        else:
            normalized_name += ' '
    print(normalized_name)


    for i in list_of_id:
        try:
            bot.send_message(i, f'сообщение от {normalized_name} \n{text}')

        #         здесь уже должна происходить отправка
        except:
            pass
    bot.send_message(message.chat.id, 'задание разослано вашим ученикам.')
    # for i in range(len(list_of_id)):



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



print('как всё запущено...')
bot.polling(none_stop=True)
