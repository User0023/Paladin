# encoding: utf-8
# --server -s 
# --port -p 
# --ssl  -l
# --canal -c
# --botname -b
# --botmsg -m
import sys
from circ import *
#default
botname = "catlock"
botmsg = "bitch"
ssl = 0
tor = 0
Er = " não possui argumento."
if len(sys.argv)==1:
	help()
	quit()
for x in range(len(sys.argv)):
	if sys.argv[x] == "-h" or sys.argv[x] == "--help":
		help()
		quit()
	elif sys.argv[x] == "-s" or sys.argv[x] == "--server":
		try:
			server = sys.argv[x+1]
		except IndexError:
			print "[ERRO] \"-s\" "+Er
			quit()
		continue
	elif sys.argv[x] == "-p" or sys.argv == "--port":
		try:
			if sys.argv[x+1].isdigit():
				port = int(sys.argv[x+1])
			else:
				print "[ERRO]\"-p\" Digite apenas numero"
				quit()
		except IndexError:
			print "[ERRO] \"-p\""+Er
			quit()
		continue
	elif sys.argv[x] == "-c" or sys.argv[x] == "--canal":
		try:
			canal = sys.argv[x+1]
			continue
		except IndexError:
			print "[ERRO] \"-c\" "+Er
			quit()
	elif sys.argv[x] == "-l" or sys.argv[x] == "--ssl":
		ssl = 1
		continue
	elif sys.argv[x] == "-t" or sys.argv[x] == "--tor":
		tor = 1
		continue
	elif sys.argv[x] == "-b" or sys.argv[x] == "--botname":
		try:
			botname = sys.argv[x+1]
			continue
		except IndexError: 
			print "[ERRO] \"-b\" "+Er
			quit()
	elif sys.argv[x] == "-m" or sys.argv[x] == "--botmsg":
		try:
			botmsg = sys.argv[x+1]
			continue
		except IndexError:
			print "[ERRO] \"-m\" "+Er
			quit()
	else:
		if sys.argv[x].startswith("-"):
			print "[ERRO] ""\""+sys.argv[x]+"\""+" opção invalida"
			quit()
if not "server" in locals():
	print "[ERRO] Servidor não foi definido"
	quit()
if not  "port" in locals():
	print "[ERRO] Porta não foi definida"
	quit()
if not "canal" in locals():
	print "[ERRO] Canal não definido"
	quit()

print "servidor: " + server
print "porta: " + str(port)
print "canal: " + canal
print "ssl: " + str(ssl)
print "tor: " + str(tor)
print "botname: " + botname
print "botmsg: " + botmsg
raw_input("\nDigite enter para continuar...")