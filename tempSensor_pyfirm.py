import pyfirmata
board = pyfirmata.Arduino("COM5")


sensor = board.get_pin('d:7:i')
it = pyfirmata.util.Iterator(board)
it.start()
sensor.enable_reporting()
while True:
    value = str(sensor.read())
    value = (value + 2)
    print("The temperature is : %s" %value)
    board.pass_time(5)
    
