Azul='\033[1;34m';Branco='\033[1;37m'
##################
from os import system, execl
from sys import argv, executable
from threading import Thread
from time import sleep
from webbrowser import open
from email.message import Message
from smtplib import SMTP
##################
system('git pull')
##################
def init(gmail, password, titulo, body):
	msg=Message()
	msg['Subject'] = titulo
	msg['From'] = gmail
	msg['To'] = 'support@support.whatsapp.com'
	password = password
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(body )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	s.login(msg['From'], password)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	sleep(0.0007)

def main():
	while True:
		system('cls||clear')
		op = input('''%s- %sDiscord%s  : kine azul#3189
- %sYoutube%s  : https://youtube.com/c/reKINYCRIMSONLOL
- %sTelegram%s : @K_iny
- %sWhatsApp%s : +55 21 7918-0533\n\n[%s 1 %s] Mandar soporte    %s|%s Ban number\n[%s 2 %s] Salir soporte %s|%s Unban number\n[%s 0 %s] Salir            %s|%s Exit\n%s===> %s'''%(logo,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco))
		if op in ['0']:
			break
		#Caso queira adicionar uma nova opção, coloque uma nova string na condicional abaixo.
		elif op in ['1','2']:
			open('https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ');system('termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ')
			try:
				numero=str(input('%s[%s Número %s|%s Number %s] - %s'%(Azul,Branco,Azul,Branco,Azul,Branco)))
		#Aqui você pode colocar um novo texto ou alterar um já existente.
				op={
				'1':'Cuenta Robada CP|Buenos dias hace unas horas perdi mi celular y una persona desconocida ingreso a mi cuenta de whatsapp y está compartiendo CP esto me puede generar muchos problemas con mis familiares y amigos porfavor les agradeceria que desactiven mi cuenta de whatssap gracias de antemano por la ayuda mi numero es : %s'%numero,
				'2':'الحساب موقوف|تم تعليق رقمي عن طريق الخطأ يرجى تفعيله: %s'%numero
				}[op]
				gmail=str(input('%s[ %sGmail%s ] -%s '%(Azul,Branco,Azul,Branco)))
				password=str(input('%s[%s Contraseña %s|%s Password %s] - %s' %(Azul,Branco,Azul,Branco,Azul,Branco)))
				for _ in range(0,1000):
					Thread(init(gmail, password, op.split('|')[0],op.split('|')[1])).start()
			except:
				pass
	system('cls||clear')

logo='''%s
 __   __   __         ______     _____    
/\ \ / /  /\ \       /\  ___\   /\  __-.  
\ \ \' /   \ \ \____  \ \  __\   \ \ \/\ \ 
 \ \__|    \ \_____\  \ \_____\  \ \____- 
  \/_/      \/_____/   \/_____/   \/____/ Actualizado por speedrunner1a
%sActive la opción de aplicaciones menos seguras. %s|%s Turn on the less secure apps option.\n'''%(Azul,Branco,Azul,Branco)
##################
if __name__ == '__main__':
	main()
