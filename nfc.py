#	 NFC interface between Arduino Leonardo and PC

from serial import Serial

io = Serial('/dev/ttyACM0', 9600, timeout=1)

while 1:
	raw = io.readline()
	print raw


 
