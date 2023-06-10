from fastapi import FastAPI
from routes.monitoreo import monitoreo

app = FastAPI()

# carga de la ruta
app.include_router(monitoreo)

