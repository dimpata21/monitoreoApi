from pymongo import MongoClient


uri = "mongodb+srv://dimpata:dimpata@monitoreo.r1efhyy.mongodb.net/?retryWrites=true&w=majority"

conn = MongoClient(uri)  #PERMITE HACER LA CONEXIÓN CON LA URI
