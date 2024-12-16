
#                                      Must install the following
#          pip3 install python-telegram-bot
#          import requests

###--------------------------------------SETTING UP TELEGRAM BOT----------------------------------###

#                        create the telegram bot with botfather on telegram
#                          Message telegram bot in group chat or privately
#                          Message Telegram Bot in terminal to get CHAT ID
TOKEN = [TELEGRAM BOT TOKEN]
URL = "https://api.telegram.org/bot{TOKEN}/GETUPDATES"
print(requests.get(url).json())
#                              pull the chat id from the print command                  #

###----------------------------------------------IPIFY INTEGRATION------------------------------------###

def telegram_bot:
    ipify = requests.get("https://api.ipify.org?format=json")
    data = website.json()
    TOKEN = [TELEGRAM BOT TOKEN / GET FROM BOT FATHER]
    CHAT_ID = [CHAT ID / GET FROM MESSAGING TELEGRAM THROUGH TERMINAL]
    text = (f"{data}")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=({text}"
    r = requests.get(url)
