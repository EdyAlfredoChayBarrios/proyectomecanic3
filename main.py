import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply


bot=telebot.TeleBot("6256558501:AAF4Or88X9LSmobO9FNsZTggfogD03fDf_A")
photos = 'Img/taladro.png'





@bot.message_handler(commands=['start','help', 'ayuda'])
def enviar(message):
    bot.send_message(message.chat.id,"Ingrese el comando /alta para empezar")


@bot.message_handler(commands=['alta'])
def alta(message):
    markup = ForceReply()
    msg=bot.send_message(message.chat.id,"Hola como te llamas", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_edad)


def preguntar_edad(message):
    nombre=message.text
    print(f'Tu nombre es {nombre}')


if __name__=='__main__':
    print("BOT INICIADO")
    bot.infinity_polling()