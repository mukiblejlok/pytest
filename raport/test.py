import time
import telnetlib
HOST ="www.google.com"
tn=telnetlib.Telnet(HOST,"80")
tn.write(b"GET /index.html HTTP/1.1\nHost: " + str(HOST) + "\n\n")
l=tn.read_all()
print (l)