import RPi.GPIO as GPIO

class DiodeHandler:

    def __init__(self, green_pin, red_pin):
        self.green_pin = green_pin
        self.red_pin = red_pin

    def start(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.green_pin, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.red_pin, GPIO.OUT, initial=GPIO.HIGH)
    
    def stop(self):
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.output(self.red_pin, GPIO.LOW)
    
    def set_green(self):
        GPIO.output(self.green_pin, GPIO.HIGH)
        GPIO.output(self.red_pin, GPIO.LOW)
    
    def set_red(self):
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.output(self.red_pin, GPIO.HIGH)
