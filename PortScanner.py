import socket 
import sys     #exit prog or arg receive
import time    #scanning time
import threading  #for parallel ports

usage = "python3  PortScanner.py  Target   Start Port   End Port"  

if(len(sys.argv) != 4):
   print(usage)
   sys.exit()
   

try:
     target = socket.gethostbyname(sys.argv[1])  #Resolve DNS to IP
except socket.gaierror:	                         #(getaddresserror)
      print("Name Resolution Error")   	 
      sys.exit()

start_port = int(sys.argv[2])   #typecast as we take input as char
end_port = int(sys.argv[3])

print("Scanning target:",target)

def scan_port(port):
    print("Scanning port:",port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)   #timeout for one port scan
    conn = s.connect_ex((target,port))    #connect_ex as it wont terminate the program if it returns nothing and goes to next port
    if(not conn):
        print("Port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port+1): # +1 as it doesnot consider end port
   
     thread = threading.Thread(target = scan_port, args = (port,)) #port is int
     thread.start()