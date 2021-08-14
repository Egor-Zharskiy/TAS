import telebot
import datetime
import random
import time
bot = telebot.TeleBot('1491623763:AAEG3nz32639Mgpc9wq21D5sN5E-oJDtELI')

@bot.message_handler(commands=['start'])
def first(message):
    print(message.from_user.id)



# time = datetime.datetime.now()
# print(time.hour)
# print(time.minute)
text = 'с ' \
       'днем рождения, Аня! я желаю тебе всего самого наилучшего в этом, 2021-м году: счастья, здоровья, любви, отличной учебы, успехов во всех твоих начинаниях! И не забывай, что я всегда помогу по мере своих возможностей! с новым годом, сладуся❤❤❤'
variables = ['с новым годом, сладуся!', 'с новым годом, пупсик!',
             'с новым годом, солнышко!!', 'с новым годом, зайка!!!!!', '❤❤❤❤❤❤❤❤❤❤❤❤', 'с новый годом поздравляю лучшую девочку!!!!❤', 'пупсик!', 'зайка!!!'
    ,'сладуся!', "самая лучшая!", "для тебя был создан отдельный бот! простой , но все же!", "сладость ты "]

# while True:
#     now  = datetime.datetime.now()
    # if now.hour == 0 or  now.minute == 0:
    #     bot.send_message(1431047914, text)
    #     bot.send_message(926725842, text)

    # if now.minute > 0 and now.hour < 22:
    #     bot.send_message(1431047914, random.choice(variables))
    #     bot.send_message(926725842, random.choice(variables))
    #     time.sleep(25)

bot.send_message(1431047914, 'на сегодня всё.')
bot.send_message(926725842, 'на сегодня всё.')