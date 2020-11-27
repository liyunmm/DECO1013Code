from microbit import *
from gesture import *
import music
import random

gesture = Gesture()

gesture_map = {
    'right': Image.ANGRY,
    'left': Image.ANGRY,
    'up': Image.SAD,
    'down': Image.SAD
    #various facial expressions
    #right, left, up, down used to cover a variety of user movement
}

while True:
    g = gesture.read()
    if g == 'right':
        display.show(gesture_map[g])
        music.play(music.DADADADUM)
        display.clear()
        sleep(300)
    if g == 'left':
        display.show(gesture_map[g])
        music.play(music.DADADADUM)
        display.clear()
        sleep(300)
    if g == 'up':
        display.show(gesture_map[g])
        music.play(music.DADADADUM)
        display.clear()
        sleep(300)
    if g == 'down':
        display.show(gesture_map[g])
        music.play(music.DADADADUM)
        display.clear()
        sleep(300)
        #gesture reactions
    if accelerometer.was_gesture('shake'):
        display.show(Image.SURPRISED)
        sleep(15000)
        #shake to rest for 15 seconds
    else:
        display.show(Image.HAPPY)
        #shown when device is idle


while True:
    if g == 'right':
        pin0.write_digital(1)
        sleep(300)
        pin0.write_digital(0)
        sleep(300)
    if g == 'left':
        pin0.write_digital(1)
        sleep(300)
        pin0.write_digital(0)
        sleep(300)
    if g == 'up':
        pin0.write_digital(1)
        sleep(300)
        pin3.write_digital(0)
        sleep(300)
    if g == 'down':
        pin0.write_digital(1)
        sleep(300)
        pin3.write_digital(0)
        sleep(300)
    #dictates how LED lights up (blinking)
    #lights up for the same duration as paired tune