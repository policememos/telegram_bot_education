import os
import time
from datetime import datetime as dt
import config
import telebot
import random


bot = telebot.TeleBot(config.token, parse_mode='MarkdownV2')

    
@bot.message_handler(commands=['start'])
def hi_to_user(message):
    current_time = str(dt.now().strftime("%b %d %Y %H:%M:%S"))
    usrid,fn,ln,usname = message.from_user.id ,message.from_user.first_name, message.from_user.last_name, message.from_user.username
    print(f'{current_time} юзер {usrid},{fn},{ln},{usname} запустил команду hi_to_user: {message.text}, answer: "text Hi"')
    # f = open('sounds/hi/hi1.ogg', 'rb')
    # bot.send_voice(message.chat.id, f, None)
    bot.send_message(message.chat.id, 'Помогу в *любом медицинском* вопросе \n пример: *болит ухо что делать*')
    bot.send_message('369110742', f'{current_time}\n{usrid}, {fn}, {ln} \n{usname} _*join bot*_')


    
    
@bot.message_handler(content_types=['text'])
def audio_help(message):
    indx = random.randint(0,13)

    
    files = [
        'jan1.ogg',
        'jan2.ogg',
        'jan3.ogg',
        'jan4.ogg',
        'jan5.ogg',
        'jan7.ogg',
        'jan8.ogg',
        'jan9.ogg',
        'jan10.ogg',
        'jan11.ogg',
        'jan12.ogg',
        'jan13.ogg',
        'jan13.ogg',
        'jan13.ogg',
        'jan13.ogg',
        'jan13.ogg',
        'jan13.ogg',
    ]

    f = open('sounds/'+files[indx], 'rb')
    ans = files[indx]    
    # time.sleep(3)
    bot.send_voice(message.chat.id, f, None)
    f.close()
    current_time = str(dt.now().strftime("%b %d %Y %H:%M:%S"))
    usrid,fn,ln,usname = message.from_user.id ,message.from_user.first_name, message.from_user.last_name, message.from_user.username
    mstxt= str(message.text)
    text = str(current_time)+ '\nЮзер id\:'+ str(usrid)+'\n1name:'+ str(fn)+' \nlastname:'+ str(ln)+' \nusername: '+ str(usname)+'\nЗапустил команду send\_voice\ntext\: "*' +str(mstxt)+'*" \nAnswer\: '+ ans.replace('.', '\.')
    print(f'{usrid=}, {fn=}, {ln=}, {usname=}, {message.text=}, {ans=}')
    bot.send_message('369110742', text)
    # time.sleep()
    
        

bot.infinity_polling()