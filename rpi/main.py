import time
import signal
from diode_handler import DiodeHandler
from server import StatusHandler
from http.server import HTTPServer
from threading import Thread


class ServerThread(Thread):

    def __init__(self, server):
        threading.Thread.__init__(self)
        self.server = server

    def run(self):
        self.server.serve_forever()


should_close = False

def handle_signals(signum, frame):
    global should_close
    should_close = True

def start():
    global server_thread

    # Add signal handlers
    signal.signal(signal.SIGINT, handle_signals)
    signal.signal(signal.SIGTERM, handle_signals)

    # Start diode handling and server
    diode_handler.start()
    server_thread = ServerThread(server)
    server_thread.start()

def stop():
    diode_handler.stop()
    server.shutdown()
    server_thread.join()


GREEN_PIN = 17
RED_PIN = 27
diode_handler = DiodeHandler(GREEN_PIN, RED_PIN, 10)

HTTP_PORT = 8000
server = HTTPServer(('', HTTP_PORT), StatusHandler(diode_handler))
server_thread = None

# Run main loop
start()
diode_handler.set_green()

while not should_close:
    time.sleep(1)
    diode_handler.ping()

stop()
