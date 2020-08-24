import time
import signal
from diode_handler import DiodeHandler

GREEN_PIN = 17
RED_PIN = 27
diode_handler = DiodeHandler(GREEN_PIN, RED_PIN, 10)

should_close = False

def handle_signals(signum, frame):
    global should_close
    should_close = True

def setup():
    # Add signal handlers
    signal.signal(signal.SIGINT, handle_signals)
    signal.signal(signal.SIGTERM, handle_signals)

    diode_handler.start()

def teardown():
    diode_handler.stop()


# Run main loop
setup()

while not should_close:
    diode_handler.set_red()
    time.sleep(1)
    diode_handler.set_green()
    time.sleep(1)

teardown()
