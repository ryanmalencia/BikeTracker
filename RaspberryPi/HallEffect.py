import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)


def onRise(channel):
    print("Detected magnet")

GPIO.add_event_detect(21, GPIO.RISING, callback=onRise, bouncetime=30)

while(True):
    x = 1
