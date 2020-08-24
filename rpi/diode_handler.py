import RPi.GPIO as GPIO
from wrapt.decorators import synchronized

class DiodeHandler:

    def __init__(self, green_pin, red_pin):
        self.running = False
        self.green_pin = green_pin
        self.red_pin = red_pin
        self.last_update = None

    @synchronized
    def start(self):
        if not self.running:
            self.running = True
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.green_pin, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.red_pin, GPIO.OUT, initial=GPIO.HIGH)
    
    @synchronized
    def stop(self):
        if self.running:
            self.running = False
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.red_pin, GPIO.LOW)
    
    @synchronized
    def set_all(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.red_pin, GPIO.HIGH)

    @synchronized
    def set_green(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.red_pin, GPIO.LOW)
    
    @synchronized
    def set_red(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.red_pin, GPIO.HIGH)
