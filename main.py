# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:55:35 2021

@author: Dasha
"""
TOKEN = "1585095785:AAEm6uWijaZbeSU_QXBBAhGrMl2KuTj8nTg"
import telebot
import random
import tekstaro

bot = telebot.TeleBot("1585095785:AAEm6uWijaZbeSU_QXBBAhGrMl2KuTj8nTg", parse_mode="Markdown")

@bot.message_handler(commands=['komencu', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Mi komencas igi vian babiladon pli interesa!\nSe vi volas alvoki min, skribu _\"Kiel vi fartas?\"_")
    
@bot.message_handler(func=lambda m: True)
def i_donisto(message):
    
     if (message.text =='Kiel vi fartas?'):
         
        frazilo = random.randint(0,9)
        idilo = random.randint(0,9)
        
        print(frazilo, " ", idilo)
        if (frazilo==5):
            bot.reply_to(message, tekstaro.frazoj[frazilo])
        else:
            bot.reply_to(message, tekstaro.frazoj[frazilo] + tekstaro.ideoj[idilo]) 
        
bot.polling()
