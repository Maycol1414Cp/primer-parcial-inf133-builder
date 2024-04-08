from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# This will store our RPG characters data
characters = {}

class RPGCharacterHandler(BaseHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(message), "utf8"))

    def do_GET(self):
        if self.path == '/characters':
            self._send_response(characters)
        elif self.path.startswith('/characters/'):
            id = int(self.path.split('/')[-1])
            if id in characters:
                self._send_response(characters[id])
            else:
                self._send_response({'error': 'Character not found'}, 404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        character = json.loads(post_data)
        
        # Generate a new id for the character
        new_id = max(characters.keys(), default=0) + 1
        characters[new_id] = character

        self._send_response(character)

    def do_PUT(self):
        id = int(self.path.split('/')[-1])
        if id in characters:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            updated_data = json.loads(post_data)
            characters[id].update(updated_data)
            self._send_response(characters[id])
        else:
            self._send_response({'error': 'Character not found'}, 404)

    def do_DELETE(self):
        id = int(self.path.split('/')[-1])
        if id in characters:
            del characters[id]
            self._send_response({'message': 'Character deleted'})
        else:
            self._send_response({'error': 'Character not found'}, 404)

def run(server_class=HTTPServer, handler_class=RPGCharacterHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print('Starting server...')
    httpd.serve_forever()

run()