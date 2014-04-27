import pygame
import pygame.midi
from time import sleep
from socketIO_client import SocketIO, BaseNamespace
import logging
import json

#log out
#logging.basicConfig(level=logging.DEBUG)

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

    if args[0]["value"]["deviceID"] == "quadphase_1" :
      color = args[0]["value"]["color"]
      strobo = args[0]["value"]["strobo"]
      rotate = args[0]["value"]["rotate"]
      uid = args[0]["value"]["uid"]
      midiOutput.write_short(0xb0, 0, color)
      midiOutput.write_short(0xb0, 1, strobo)
      midiOutput.write_short(0xb0, 2, rotate)
      midiOutput.write_short(0xb0, 3, 127)
      sleep(0.05)
      midiOutput.write_short(0xb0, 3, 0)
      print "uid : " + str(uid) + ", color : " + str(color) + ", strobo : " + str(strobo) + ", rotate : " + str(rotate)

    if args[0]["value"]["deviceID"] == "strobo_1" :
      speed = args[0]["value"]["speed"]
      power = args[0]["value"]["power"]
      uid = args[0]["value"]["uid"]
      midiOutput.write_short(0xb0, 4, speed)
      midiOutput.write_short(0xb0, 5, power)
      sleep(0.05)
      midiOutput.write_short(0xb0, 5, 0)
      print "uid : " + str(uid) + ", speed : " + str(speed) + ", power : " + str(power)


with SocketIO('http://web-lj.ayafuji.com', 80) as socketIO:
    socketIO.on('message', response_1);
    socketIO.wait()



