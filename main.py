import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
import database
import respuesta

bot = telebot.TeleBot("6256558501:AAF4Or88X9LSmobO9FNsZTggfogD03fDf_A")
usuarios = {}


# inicio

@bot.message_handler(commands=['start', 'help', 'ayuda'])
def enviar(message):
    bot.send_message(message.chat.id, "Ingrese el comando /alta para empezar")


@bot.message_handler(commands=['alta'])
def alta(message):

    respuesta=database.consultaNombre(message.chat.id)

    if respuesta[0][0] == "0":
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "Hola como te llamas", reply_markup=markup)
        bot.register_next_step_handler(msg, insertarDatos)
    else:
        bot.send_message(message.chat.id, f"""Holaaaa  {respuesta[0][0]} como te puedo ayudar """)
        volverAValidar(message)




def insertarDatos(message):
    database.insertar(f"""{message.text}""", message.chat.id)
    nombre = message.text
    print(f'Tu nombre es {nombre}')
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Pulsa alguna opcionm"
                                 , resize_keyboard=True)
    markup.add("HACER PEDIDO", "RECONOCER IMAGEN")
    msg = bot.send_message(message.chat.id, 'Cual es tu opcion', reply_markup=markup)
    bot.register_next_step_handler(msg, validarOpcion)


def validarOpcion(message):
    if message.text != "HACER PEDIDO" and message.text != "RECONOCER IMAGEN":
        bot.send_message(message.chat.id, "ERROR: argumento no valido")
        volverAValidar(message)
    else:
        bot.send_message(message.chat.id, "ES CORRECTO")
        opciones(message)


def volverAValidar(message):
    markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder="Pulsa alguna opcionm"
                                 , resize_keyboard=True)
    markup.add("HACER PEDIDO", "RECONOCER IMAGEN")
    msg = bot.send_message(message.chat.id, 'Cual es tu opcion', reply_markup=markup)
    bot.register_next_step_handler(msg, validarOpcion)


@bot.message_handler(content_types=['text'])
def opciones(message):
    if message.text == "HACER PEDIDO":
        bot.send_message(message.chat.id, "VAMOS HACER EL PEDIDO")
    elif message.text == "RECONOCER IMAGEN":
        bot.send_message(message.chat.id, "MIREMOS LA IMAGE")
        msg = bot.send_message(message.chat.id, 'Cual es tu opcion')
        bot.register_next_step_handler(msg ,get_broadcast_picture)
        # respuesta.respuesta('Img/espatula.jpeg')
    else:
        bot.send_message(message.chat.id, "COMANDO INCORRECTO")


@bot.message_handler(func=lambda m: True, content_types=['photo'])
def get_broadcast_picture(message):
    file_path = bot.get_file(message.photo[0].file_id).file_path
    file = bot.download_file(file_path)
    with open("python1.png", "wb") as code:
        code.write(file)
    nuevo=respuesta.respuesta('python1.png')
    mostrarMenu(nuevo,message)

def mostrarMenu(respuesta,message):

    resultados=database.consuiltaProducto(respuesta)
    for fila in resultados:
        photos = f"""{fila[3]}"""
        bot.send_photo(chat_id=message.chat.id, photo=open(photos, 'rb'))
        bot.send_message(chat_id=message.chat.id, text=f"""El PRODUCTO ES  {fila[1]} con precio de Q {fila[4]}""")



if __name__ == '__main__':
    print("BOT INICIADO")
    bot.infinity_polling()
