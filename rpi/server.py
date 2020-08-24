from diode_handler import DiodeHandler
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from status import Status

PORT = 8000

class StatusHandler(BaseHTTPRequestHandler):

    def __init__(self, diode_handler):
        self.webcam_status = Status.UNKNOWN
        self.diode_handler = diode_handler

    def __call__(self, *args):
        super().__init__(*args)

    def update_diodes(self):
        if self.webcam_status is Status.FREE:
            self.diode_handler.set_green()
        elif self.webcam_status == Status.IN_USE:
            self.diode_handler.set_red()
        else:
            self.diode_handler.set_all()

    def handle_update(self):
        try:
            content_length = int(self.headers["Content-Length"])
            data = json.loads(self.rfile.read(content_length).decode("utf-8"))
            self.webcam_status = Status(int(data['status']))
            self.send_response(200)
        except ValueError:
            self.webcam_status = Status.UNKNOWN
            self.send_response(404)

        self.update_diodes()
        response = json.dumps({
                'status': self.webcam_status.value
            }) + "\n"

        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))
    
    def do_POST(self):
        if self.path != '/update':
            self.send_response(404)
            self.end_headers()
        else:
            self.handle_update()
