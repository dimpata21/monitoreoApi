import requests

dato = {"lugar":"Girardota", "temperatura":25, "humedad":67}

#el post los recibe el monitoreo en 8000
requests.post("localhost:8000/monitoreo", json=dato)

print(res.text)