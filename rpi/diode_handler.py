import RPi.GPIO as GPIO
from wrapt.decorators import synchronized
import time

class DiodeHandler:

    def __init__(self, green_pin, red_pin, timeout_secs):
        self.running = False
        self.green_pin = green_pin
        self.red_pin = red_pin
        self.last_update = None
        self.timeout_secs = timeout_secs

    @synchronized
    def start(self):
        if not self.running:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.green_pin, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(self.red_pin, GPIO.OUT, initial=GPIO.HIGH)

            self.running = True
            self.last_update = time.time()
    
    @synchronized
    def stop(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.red_pin, GPIO.LOW)

            self.running = False
            self.last_update = time.time()
    
    @synchronized
    def set_all(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.red_pin, GPIO.HIGH)
            self.last_update = time.time()

    @synchronized
    def set_green(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.red_pin, GPIO.LOW)
            self.last_update = time.time()
    
    @synchronized
    def set_red(self):
        if self.running:
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.red_pin, GPIO.HIGH)
            self.last_update = time.time()
    
    @synchronized
    def ping(self):
        time_now = time.time()
        delta = time_now - self.last_update
        if delta > self.timeout_secs:
            self.set_all()

