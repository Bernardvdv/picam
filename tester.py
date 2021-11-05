from picamera import PiCamera, Color
import time

camera = PiCamera()

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
time.sleep(5)
camera.stop_preview()
