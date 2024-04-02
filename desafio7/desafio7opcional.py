# Librerias
import json
import requests

# Variables
url = "https://reqres.in/api/users"

#Información de los usuarios: users_data
request = requests.request("GET", url, headers={}, data={})
users_data = json.loads(request.text)
print("********************************************")
print(users_data)
print("********************************************")
print(request)

#Crear usuario Ignacio
data_ignacio = {"6": {"id": 7, "first_name": "Ignacio", "work": "Profesor"}}
created_user = requests.post(url, json=data_ignacio)
print("********************************************")
print(created_user.text)
print("********************************************")
print(created_user)

#Actualizar usuario morpheus
url_put = "https://reqres.in/api/users/1"
data_morpheus = {"first_name": "morpheus", "residence": "zion"}
updated_user = requests.put(url_put, data_morpheus)
print("********************************************")
print(updated_user.text)
print("********************************************")
print(updated_user)

# 4. Elimine usuario Tracey. 
Tracey = requests.delete("https://reqres.in/api/users/6")
print("********************************************")
print(Tracey)