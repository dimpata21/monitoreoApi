from fastapi import APIRouter
from config.db import conn
from schemas.monitoreo import monitoreoEntity, muchosMonitoreosEntity
from models.monitoreo import Monitoreo
import datetime 

monitoreo = APIRouter()

@monitoreo.get('/monitoreo/tempratura')
def find_all_monitoreo():
    return muchosMonitoreosEntity(conn.monitoreo.dato.find({"temperatura":{"gt":30}}))

@monitoreo.post('/monitoreo')
def save_monitoreo(mon: Monitoreo):
    new_mon = dict(mon)
    new_mon["createdAt"] = datetime.datetime.utcnow()
    new_mon["updatedAt"] = datetime.datetime.utcnow()
    conn.monitoreo.dato.insert_one(new_mon)
    return "Dato almacenado"

@monitoreo.put('/monitoreo')
def update_monitoreo():
    return "Actualizacion de dato de monitoreo"

@monitoreo.delete('/monitoreo')
def delete_monitoreo():
    return "Dato borrado"