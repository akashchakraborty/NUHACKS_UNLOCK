import urllib
import requests
from bs4 import BeautifulSoup

import pyfirmata
board = pyfirmata.Arduino("COM5")
SENSOR_PIN = 0
value = 1

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()


while(value != 0):
    
    value = board.analog[0].read()
    if value== None:
        pass
        
    else:
        value1 = (value*488.7)
        print("Reading is : %s " %value1)
        data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=AQLJZMDD9CV6IRK1&field1="+str(value1))
        print (data)
        board.pass_time(10)
#data = urllib.urlopen("GET https://api.thingspeak.com/update?api_key=AQLJZMDD9CV6IRK1&field1="+str(value1));
#print (data);
