# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:55:35 2021
upd: 07.02.2020 21:31
@author: Dasha
"""
TOKEN = "1585095785:AAEm6uWijaZbeSU_QXBBAhGrMl2KuTj8nTg"
#TOKEN = "1684189121:AAFzYn7v_kVhBRylzU-fugyPfZ7fzPnhEW8"

versio="0.3"

import telebot
import random
import tekstaro


bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
 
    

@bot.message_handler(commands=['komencu', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Mi komencas igi vian babiladon pli interesa!\nSe vi volas alvoki min, skribu _\"Kiel vi fartas?\"_")
    
@bot.message_handler(commands=["versio"])
def send_version(message):
    bot.reply_to(message, "Versio " + versio)

@bot.message_handler(commands=["diru"])  
def ĝisdatigo_checker(message):
    for i in range(0,20):   
        bot.reply_to(message, tekstaro.ideoj[i])
    
@bot.message_handler(func=lambda m: True)
def i_donisto(message):
    
     print(message.text.find("fartas"))
           
     babilido = str(message.chat.id)
     print("Nova mesaĝo ĉe " + babilido + "\n")
     
     #if (message.text.lower() =='kiel vi fartas?' or message.text.lower() == "fartas kiel vi?" or message.text.lower() == "kiel fartas vi?" or message.text.lower() == "fartas vi kiel?" or message.text.lower() == "vi fartas kiel?" or message.text.lower() == "vi kiel fartas?"):
     if (message.text.lower().find('fartas') != -1 and message.text.lower().find('kiel') != -1):
        
        frazilo = random.randint(0,11)
        idilo = random.randint(0,19)
        
        print(frazilo, " ", idilo)
        if (frazilo==5):
            bot.reply_to(message, tekstaro.frazoj[frazilo])
        else:
            bot.reply_to(message, tekstaro.frazoj[frazilo] + tekstaro.ideoj[idilo]) 
            
     elif(message.text.lower().find("fartas") != -1):
         #bot.reply_to(message, "Mi estas stulta boto. Mi vidas vorton \"fartas\", sed mi ne certas ĉu vi demandis \"Kiel vi fartas?\"")
         bot.reply_to(message, "Mi jam lacis diri, ke mi estas stulta boto. Skribu \"Kiel vi fartas?\" normale")
       
     elif(message.text.lower()=="ĉu mi estas finvenkisto?"):     
        bot.reply_to(message, "Jes, vi estas")
     
     elif(message.text.lower().find('stulta') != -1 and message.text.lower().find('boto') != -1):
        bot.reply_to(message, "Ege malrespekte")

bot.polling()

