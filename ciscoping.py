import subprocess
import sys
import socket
from subprocess import Popen, PIPE
elhost = sys.argv[1]
try:
	socket.inet_aton(elhost)
	continuo = True
except:
        continuo = False

if continuo:
	print("pinging to: ", elhost)
	try:
		while True:
			process = subprocess.Popen(['ping','-c','3',elhost],
			stdout=PIPE, stderr=PIPE)
			stdout, stderr = process.communicate()
			packetloss = float([x for x in stdout.decode('utf-8').split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
			if packetloss != 0.0:
			    print("!", end="", flush=True)
			else:
			    print(".", end="", flush=True)
	except:
		print(stdout.decode('utf-8'))
else:
	print("Usage: ciscoping.py ip")
	print("example ciscoping.py 10.1.1.13")
