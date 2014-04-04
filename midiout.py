import pygame
import pygame.midi
from time import sleep

instrument = 0
note = 0
volume = 127

pygame.init()
pygame.midi.init()
for id in range(pygame.midi.get_count()):
  print pygame.midi.get_device_info(id)

port = 2
midiOutput = pygame.midi.Output(port, 1)
midiOutput.set_instrument(instrument)

#.midi_out.write_short(0xb0, 17, 123)

while(1):
  for note in range(4, 7):
    sleep(0.2)
    volume = 0
    midiOutput.write_short(0xb0, note, volume)
    print str(note) + " : " + str(volume)
    if note == 5:
      sleep(1)
      volume = 95
    else:
      sleep(1)
      volume = 100
    midiOutput.write_short(0xb0, note, volume)
    print str(note) + " : " + str(volume)

    #midiOutput.note_off(note,volum)
    #midiOutput.note_on(note,volume)
    #del midiOutput
    #pygame.midi.quit()
