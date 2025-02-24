from modules.utils.validaciones import sololetras as sl, solonumeros as sn
import os
import json
import modules.utils.corefiles as cf
import modules.controllers.players as pl
DB_FILE="data/liga.json"
def addcuerpotec(cuerpotec:dict):
    while True:

        name=sl("Ingrese el nombre: ")
        edad=sn("Ingrese la edad: ")
        rol=sl("Ingresa el rol: ")

        cuerpot={
            'name':name,
            'edad':edad,
            'rol':rol
        }

        cuerpotec.update({name:cuerpot})
        cf.update_json(DB_FILE,cuerpotec,[name])
        otroct = sl("¿Desea agregar otro cuerpo tecnico? (s/n): ").lower()

        if otroct != "s":
            print("Volviendo al menú anterior... 🔙")
            os.system("pause")  # Espera antes de regresar al menú
            break # 
        