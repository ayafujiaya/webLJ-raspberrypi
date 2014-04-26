import pygame
import pygame.midi
from time import sleep
from socketIO_client import SocketIO, BaseNamespace
import logging
import json

#log out
#logging.basicConfig(level=logging.DEBUG)

########### Task List ###########
#make function each ligt 

#each value initialize
instrument = 0
note = 0
volume = 127
port = 2

#pygame & pygame.midi initialize
pygame.init()
pygame.midi.init()

#output midi device
for id in range(pygame.midi.get_count()):
  print pygame.midi.get_device_info(id)

#select midi device
midiOutput = pygame.midi.Output(port, 1)
midiOutput.set_instrument(instrument)

def response_1(*args):
    #print args[0]["value"]["color"]
    color = args[0]["value"]["color"]
    strobo = args[0]["value"]["strobo"]
    rotate = args[0]["value"]["rotate"]
    midiOutput.write_short(0xb0, 3, color)
    midiOutput.write_short(0xb0, 4, strobo)
    midiOutput.write_short(0xb0, 5, rotate)    

class Namespace(BaseNamespace):

    def on_connect(self):
        print '[Connected]'

#socketIO = SocketIO('http://web-lj.ayafuji.com', 80, Namespace)
#socketIO.emit('bbb', {'xxx': 'yyy'}, on_bbb_response)


with SocketIO('http://web-lj.ayafuji.com', 80) as socketIO:
    socketIO.on('message', response_1);
    socketIO.wait()

"""
while(1):

    sleep(0.1)
    midiOutput.write_short(0xb0, 3, 0)
    sleep(0.1)

    midiOutput.write_short(0xb0, 0, volume)
    sleep(0.1)

    midiOutput.write_short(0xb0, 7, 100)
    sleep(0.1)
    midiOutput.write_short(0xb0, 7, 0)
    sleep(0.1)

    midiOutput.write_short(0xb0, 4, volume)
    sleep(0.1)

    volume = volume + 25
    if volume == 125:
      volume = 0
"""
