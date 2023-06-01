import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
import database

bot=telebot.TeleBot("6256558501:AAF4Or88X9LSmobO9FNsZTggfogD03fDf_A")
usuarios={}

photos = 'Img/taladro.png'



#inicio

@bot.message_handler(commands=['start','help', 'ayuda'])
def enviar(message):
    bot.send_message(message.chat.id,"Ingrese el comando /alta para empezar")


@bot.message_handler(commands=['alta'])
def alta(message):
    markup = ForceReply()
    msg=bot.send_message(message.chat.id,"Hola como te llamas", reply_markup=markup)
    bot.register_next_step_handler(msg, insertarDatos)







def insertarDatos(message):
    database.insertar(f"""{message.text}""", message.chat.id)
    nombre=message.text
    print(f'Tu nombre es {nombre}')
    markup=ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Pulsa alguna opcionm"
    ,resize_keyboard=True)
    markup.add("HACER PEDIDO", "RECONOCER IMAGEN")
    msg=bot.send_message(message.chat.id, 'Cual es tu opcion', reply_markup=markup)
    bot.register_next_step_handler(msg,validarOpcion)


def validarOpcion(message):
    if message.text != "HACER PEDIDO" and  message.text != "RECONOCER IMAGEN":
        bot.send_message(message.chat.id, "ERROR: argumento no valido")
        volverAValidar(message)
    else:
        bot.send_message(message.chat.id, "ES CORRECTO")
        opciones(message)

def volverAValidar(message):
    markup=ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Pulsa alguna opcionm"
    ,resize_keyboard=True)
    markup.add("HACER PEDIDO", "RECONOCER IMAGEN")
    msg=bot.send_message(message.chat.id, 'Cual es tu opcion', reply_markup=markup)
    bot.register_next_step_handler(msg,validarOpcion)



@bot.message_handler(content_types=['text'])
def opciones(message):
    if message.text == "HACER PEDIDO":
        bot.send_message(message.chat.id, "VAMOS HACER EL PEDIDO")
    elif message.text == "RECONOCER IMAGEN":
        bot.send_message(message.chat.id, "MIREMOS LA IMAGE")
    else:
        bot.send_message(message.chat.id, "COMANDO INCORRECTO")



if __name__=='__main__':
    print("BOT INICIADO")
    bot.infinity_polling()