import pyfirmata
board = pyfirmata.Arduino("COM5")
SENSOR_PIN = 0
value = 1
en = board.get_pin('d:9:o')
Ia = board.get_pin('d:10:o')
Ib = board.get_pin('d:11:o')


it = pyfirmata.util.Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()


while True:
    
    value = board.analog[0].read()
    if value== None:
        pass
        
    else:
        value1 = (value*488.7)
        print("Reading is : %s " %value1)
        board.pass_time(5)
##        if (value1 <= 25):
##            print("hi")
##            #board.digital[en].write(1)
##
##            Ia.write(1)
##            
##
##            Ib.write(0)
##            
##
##
##        else:
##            #board.digital[en].write(1)
##            Ia.write(0)
##            Ib.write(1)



        
