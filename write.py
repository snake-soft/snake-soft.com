from time import sleep
from random import random, uniform
from pynput.keyboard import Controller
keyboard=Controller()
#keyboard.type('TESTAA')

sleep(3)

content = ''
with open('write.txt', 'r') as file:
    for line in file:
        content += line

#print(content)
#sleep(5)   

interval = 0
for char in content:
    if char in (' '):
        interval = uniform(0.05, 0.2)
    else:
        sleep(interval)
    keyboard.type(char)



#with open('output.txt', 'w') as file:
    #file.write(content)

        #print(interval)

    #import pdb; pdb.set_trace()  # <---------
    
