import RPi.GPIO as GPIO
import time
import signal

GREEN_PIN = 17
RED_PIN = 27

should_close = False

def handle_signals(signum, frame):
    global should_close
    should_close = True

def setup():
    # Add signal handlers
    signal.signal(signal.SIGINT, handle_signals)
    signal.signal(signal.SIGTERM, handle_signals)

    # Light both LEDS
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.HIGH)

def teardown():
    # Switch LEDs off
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)


# Run main loop
setup()

while not should_close:
    time.sleep(1)

teardown()
