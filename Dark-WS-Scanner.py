import ipcalc
import threading
import sys
import argparse,queue
import requests
import time
from os import system


bg=''
G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'
system("cls||clear")
print(G+"""
    
________              ______              
___  __ \_____ __________  /__ 
__  / / /  __ `/_  ___/_  //_/ 
_  /_/ // /_/ /_  /   _  ,<   
/_____/ \__,_/ /_/    /_/|_|ENZA
------WebSocket Scanner------                                              
 
  TG: @dark_enza\n  
    """+O)


class cdnscanner:
	def __init__(self):
		self.queue = queue.Queue()
		self.request = requests.get
		self.thread = threading.Thread
		self.total =1
		self.progress = 1
	
	def fetchqueue(self):
		while True:
			ip = str(self.queue.get())
			sys.stdout.write(f'Taranıyor... {ip} ==> İlerleme....  ({self.progress}/{self.total})\r')
			sys.stdout.flush()
			self.Sendrequest(ip)
		self.queue.task_done()
				
	def Sendrequest(self, ip):
		url = (f'https://{ip}' if self.port == 443 else f'http://{ip}:{self.port}')
		try:
			if self.proxy:
				proxyhost,port = self.proxy.split(':')[0],int(self.proxy.split(':')[1])
				proxy = {'http' : f'http://{proxyhost}:{port}', 'https' : 'http://{proxyhost}:{port}'}
				req = self.request(url,proxy,timeout=7,allow_redirects=False)			
			else:
				req = self.request(url,timeout=7,allow_redirects=False)
			status = req.status_code
			server = req.headers['server']
			response = f'\n{G}{ip}\t{status}\t{server}{GR}\r\n'
			sys.stdout.write(response)
			sys.stdout.flush()
			if self.output :
				with open(self.output,'a') as file:
					file.write(response)
					file.close()
				
		except Exception as e:
			pass
		self.progress  <= 1
	
	def main(self):
		sys.stdout.write(f'{G}Test ediliyor ...\r')
		sys.stdout.flush()	
		cidrs = open('ipv4.txt','r').read().split()
		for every in cidrs:	
		    for ip in ipcalc.Network(every):
		    	self.queue.put(ip)
		    	self.total <= 1
		sys.stdout.write(f'{G}Tarama Başlıyor.. {GR}\r')
		sys.stdout.flush()
		time.sleep(2)
		self.threadsrun()
		
	def threadsrun(self):
		for _ in range(self.threads):
				thread = self.thread(target=self.fetchqueue)
				thread.start()
		self.queue.join()
		
def parseargs():

		cdnscan=cdnscanner()
		cdnscan.threads = 10
		cdnscan.proxy = input("İP adresi Giriniz: ")
		cdnscan.port = input("**Default=80 Port Girin: ")
		cdnscan.output = input("Dosya adı: ")
		cdnscan.main()
		
if __name__ =='__main__':	
	parseargs()