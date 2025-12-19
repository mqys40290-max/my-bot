import telebot from telebot import types import os

التوكن سيتم جلبة تلقائياً من إعدادات GitHub Secrets
TOKEN = os.getenv('BOT_TOKEN')

!!! ضع رابطك الخاص هنا بدلاً من الرابط التجريبي !!!
MY_TRACKING_LINK = "

https://mqys40290-max.github.io/iraq-group/"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) def welcome(message): # إنشاء الزر الذي يحتوي على الرابط markup = types.InlineKeyboardMarkup() join_button = types.InlineKeyboardButton(text="دخول ومتابعة ✅", url=MY_TRACKING_LINK) markup.add(join_button)

# رسالة الترحيب
welcome_text = (
    f"مرحباً بك يا {message.from_user.first_name} في البوت!\n\n"
    "للبدء، يرجى الضغط على الزر أدناه لإتمام عملية التحقق."
)

bot.reply_to(message, welcome_text, reply_markup=markup)
if name == "main": bot.infinity_polling()
