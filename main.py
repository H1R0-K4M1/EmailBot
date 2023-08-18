#!/usr/bin/python3
import pandas as pd
import smtplib
import email.message
import time, os

class bot_email(object):
    def __init__(self):
        self.env_msg()
    def env_msg(self):
        arq = open ('root_bot/menssagem.html','r')
        corpo_email = arq.read()
        arq.close()
        clientes = pd.read_excel('./root_bot/users.xlsx')
        for index, ct in clientes.iterrows():
            msg = email.message.Message()
            msg['Subject'] = 'Teste de mensagens automáticas'
            msg['From'] = 'lucasfodzap@gmail.com'
            msg['To'] = ct['email']
            password = 'goxngdokqxjodaxx'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'],msg['To'], msg.as_string().encode('utf-8'))
            print("Enviado com sucesso!\nPara:",ct['nome'],'\n')
            server.quit()
            time.sleep(5)
bot_email()

