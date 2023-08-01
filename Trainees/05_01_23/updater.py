import time, sys


def update_plotter_file():
    data = open('readings.txt', 'r')
    sent = open('plotter.txt', 'w+')
    sent.read()
    sent.close()
    time.sleep(1)

    while True:
        sent = open('plotter.txt', 'a') 
        part = data.readline()
        sent.write(update_text(part))
        sent.close()
        time.sleep(2)
    
def update_text(String):
    Str = String.split(',')
    Str.__delitem__(1)
    #print(Str)   
    return ','.join(Str)

try:
    update_plotter_file()
except KeyboardInterrupt:
    print('Ending')
    sys.exit()

