import requests
import json

# POST /characters
character = {
    "name": "Gandalf",
    "level": 10,
    "role": "Wizard",
    "charisma": 15,
    "strength": 10,
    "dexterity": 10
}
response = requests.post('http://localhost:8000/characters', data=json.dumps(character))
print(response.json())

# GET /characters
response = requests.get('http://localhost:8000/characters')
print(response.json())

# GET /characters/?role=Archer&level=5&charisma=10
# response = requests.get('http://localhost:8000/characters', params={'role': 'Archer', 'level': 5, 'charisma': 10})
# print(response.json())

# PUT /characters/2
character_update = {
    "charisma": 20,
    "strength": 15,
    "dexterity": 15
}
response = requests.put('http://localhost:8000/characters/2', data=json.dumps(character_update))
print(response.json())

# DELETE /characters/3
response = requests.delete('http://localhost:8000/characters/3')
print(response.json())

# POST /characters
character = {
    "name": "Legolas",
    "level": 5,
    "role": "Archer",
    "charisma": 15,
    "strength": 10,
    "dexterity": 10
}
response = requests.post('http://localhost:8000/characters', data=json.dumps(character))
print(response.json())

# GET /characters
response = requests.get('http://localhost:8000/characters')
print(response.json())