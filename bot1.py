import os
import telebot

bot = telebot.TeleBot('') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, Estoy a tu disposicion")
    print("Mandaron saludo")

@bot.message_handler(commands=['nombre', 'name'])
def nombre(mensaje):
    bot.reply_to(mensaje, "Mi nombre es Jarvis")
    print("Mandaron nombre")

@bot.message_handler(commands=['edad', 'age'])
def edad(mensaje):
    bot.reply_to(mensaje, "Tengo 25 años")
    print("Mandaron edad")

@bot.message_handler(commands=['direccion', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "Barrio San Jose Morazan Yoro")
    print("Mandaron Direccion")

@bot.message_handler(commands=['horario'])
def direccion(mensaje):
    bot.reply_to(mensaje, "Lunes a Viernes 08:00am a 04:00 pm")
    print("Mandaron Direccion")

bot.polling()