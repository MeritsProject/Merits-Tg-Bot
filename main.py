import os
import telebot


bot = telebot.TeleBot("5170739237:AAEZ5oKFb_PQmdHP4oPAl0OXr0ko-_6lGMM")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "සාදරයෙන් පිළිගන්නවා merits chat bot")

  @bot.message_handler(commands=["Class"])
def send_welcome(message):
  bot.reply_to(message, "Class තියනවද කියලා දැන ගැනීම සදහා අපගේ වෙබ් පිටුවට යන්න")
  
  @bot.message_handler(commands=["today"])
def send_welcome(message):
  bot.reply_to(message, "අද හොද දවසක්")
  
  @bot.message_handler(commands=["whats yor name?"])
def send_welcome(message):
  bot.reply_to(message, "Hello I'm Merits Chat Bot")
  
@bot.message_handler(commands=["bot creater team"])
def send_welcome(message):
  bot.reply_to(message, "ප්‍රධාන අනුග්‍රහය දැක් dragon තාක්ෂණය, bot creatre ඔමිදු අංජන")
  
  
@bot.message_handler(commands=["subscribe"])
def send_message(message):
  bot.send_message(message.chat.id, "ලින්කය තව මාසෙකින් ලබාදෙනු ඇත")



bot.polling()
