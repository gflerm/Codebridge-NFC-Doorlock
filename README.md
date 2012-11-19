Codebridge-NFC-Doorlock
=======================

Arduino based doorlock controller using a NFC reader module and an Arduino Leonardo.

Card gets scanned by a card reader, controlled by the Leonardo, and send the info to the PC via serial port.

Csrd info get autthenticated by a python script, and if succesfull, sends a command back to the Lenoardo to send a pulse to unlock the electronic doorlock.

Python script was created by Vaughan from Codebridge.


