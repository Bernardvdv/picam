#Raspberry-Pi pan and tilt using arrow keys script
#must be run from Pi's terminal!
#use code "python KeyboardPanTilt.py" after you cd into the correct folder!

#importing required libraries
import curses
import os
import time
import picamera
import pantilthat

#setting up camera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview(fullscreen=False, window = (100,20,640,480))

#flipping the camera for so its not upside down
camera.vflip = True
camera.hflip = True

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

#setting start up serrvo positions
a = .5
b = .5

pantilthat.pan(a)
pantilthat.tilt(b)

#Set up what number the first picture will be tagged with 
pic = 1

#This section will determine what happens when certain keys are pressed. I have it set up so P
#will take a picture, Q will quit the application, Arrow keys will control the Pan Tilt Camera (5 Degree angles)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            #if q is pressed quit
            break
        if char == ord('p'):
            #if p is pressed take a photo!
            camera.capture('image%s.jpg' % pic)
            pic = pic + 1
            screen.addstr(0, 0, 'picture taken! ')
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right ')
            if b > -90:
                b = b - 5
            pantilthat.tilt(b)
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            if b < 90:
                b = b + 5
            pantilthat.tilt(b)
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            if a < 90:
                a = a + 5
            pantilthat.pan(a) 
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up ')
            if a > -90:    
                a = a - 5
            pantilthat.pan(a)
            time.sleep(0.005)
            
            
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
