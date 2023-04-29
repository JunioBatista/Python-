import smtplib
#enviar email
#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time as t 
from tkinter import *

#criação do objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))


#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')

#----------------------------------------------------------------
# modulo time

x = t.time()
print(f'Local time: {t.ctime(x)}')

"""time.struct_time gera  array com valor de tempo retornado pelas funções gmtime() e localtime()

indice 0 --> tm_year --> 2020
indice 1 --> tm_mon --> range [1, 12]
indice 2 --> tm_mday --> range [1, 31]
indice 3 --> tm_hour --> range [0, 23]
indice 4 --> tm_min --> range [0, 59]
indice 5 --> tm_sec --> range [0, 61]
indice 6 --> tm_wday --> range [0, 6] Domingo é 0
indice 7 --> tm_yday --> range [1, 366]
indice 8 --> tm_isdst --> 0,1 ou -1
indice 9 --> tm_zone --> Abreviação do nome da timezone"""


#-------------------------------------------------------
# criação de interface GUI com tkinter



janelaPrincipal = Tk()
janelaPrincipal.mainloop()

texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.place(x = 50, y = 100)
janelaPrincipal.mainloop()


def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="logoEstacio.gif")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()

