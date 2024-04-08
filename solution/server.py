from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# problema con 
class personaje:
    def __init__(self):
        self.id = None
        self.name = None
        self.level = None
        self.role = None
        self.charisma = None
        self.strength = None
        self.dexterity = None
    def __str__(self):
        return f'{self.id} {self.name} {self.level} {self.role} {self.charisma} {self.strength} {self.dexterity}'
# builder
class personajeBuilder:
    def __init__(self):
        self.personaje = personaje()
    def setId(self, id):
        self.personaje.id = id
        return self
    def setName(self, name):
        self.personaje.name = name
        return self
    def setLevel(self, level):
        self.personaje.level = level
        return self
    def setRole(self, role):
        self.personaje.role = role
        return self
    def setCharisma(self, charisma):
        self.personaje.charisma = charisma
        return self
    def setStrength(self, strength):
        self.personaje.strength = strength
        return self
    def setDexterity(self, dexterity):
        self.personaje.dexterity = dexterity
        return self
    def build(self):
        return self.personaje
# director
class personajeDirector:
    def __init__(self):
        self.builder = personajeBuilder()
    def createPersonaje(self, id, name, level, role, charisma, strength, dexterity):
        return self.builder.setId(id).setName(name).setLevel(level).setRole(role).setCharisma(charisma).setStrength(strength).setDexterity(dexterity).build()
class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(message), "utf8"))
    