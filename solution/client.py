import requests

# 1. Crear un nuevo personaje
new_personaje = {
    "name": "Nuevo personaje",
    "level": 1,
    "role": "Archer",
    "charisma": 10,
    "strength": 10,
    "dexterity": 10
}
response = requests.post('http://localhost:8000/personajes', data=new_personaje)
print(response.json())

# 2. Listar todos los personajes
response = requests.get('http://localhost:8000/personajes')
print(response.json())

# 3. Listar a todos los personajes del rol `Archer` con nivel igual a 5 y carisma igual a 10
params = {'role': 'Archer', 'level': '5', 'charisma': '10'}
response = requests.get('http://localhost:8000/personajes', params=params)
print(response.json())

# 4. Actualizar la carisma, fuerza y destreza de un personaje por su **id**
update_data = {
    "charisma": 15,
    "strength": 15,
    "dexterity": 15
}
response = requests.put('http://localhost:8000/personajes/1', data=update_data)
print(response.json())