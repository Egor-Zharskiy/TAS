import telebot
from telebot import types
import sqlite3
import datetime
import time
import random
import colorama
from telebot import TeleBot
from keyboa import keyboa_maker
# спросить у сани, как это можно пофиксить, типо что с глобальной не пашет


selected_days = []

days = ["понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота",
        "воскресенье", "✅", ]



select_of_days = [
    "понедельник", "вторник", "среда",
    "четверг", "пятница", "суббота",
    "воскресенье", "✅"
  ]


global Name_fsa_fsa, teacher_name_fsa_fsa
bot = telebot.TeleBot('1279191350:AAFMba9tw-jvy2F_2JRfy6b_Jv8WZjG075g')
@bot.message_handler(commands=['hi'])
def haha(message):
  global select_of_days
  # решить вопрос этим списком всратым
  id = int(message.chat.id)


  kb_fruits = keyboa_maker(items=select_of_days, copy_text_to_callback=True, auto_alignment=True)

  bot.send_message(
    chat_id=id, reply_markup=kb_fruits,
    text="выберите дни для рассылки заданий.")


@bot.callback_query_handler(func=lambda call: True)

def callback(call):
    global days, selected_days
    print(days)
    # как так сделать, чтобы переменная запоминалась?
    if call.data == "✅":
        days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье", "✅", ]
        print(days, 'days')
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

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='выберите дни для рассылки заданий.', reply_markup=kb_fruits)



    # if call.data == '✅':


bot.polling(none_stop=True)
