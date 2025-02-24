from modules.utils.validaciones import sololetras as sl, solonumeros as sn
import os
import json
import modules.utils.corefiles as cf
import modules.controllers.players as pl
DB_FILE="data/liga.json"

def addcuerpomedico(cuerpomd:dict):
    while True:
        name=sl("Ingrese el nombre del cuerpo medico:")
        edad =sn("Ingrese la edad del cuerpo medico: ")
        rol= sl("Ingrese el rol delcuerpo medico: ")

        cuerpomd= {
            'name':name,
            'edad':edad,
        'rol': rol
        }
       
        cf.update_json(DB_FILE,cuerpomd,[name])

        otrocm = sl("¿Desea agregar otro cuerpo medico? (s/n): ").lower()

        if otrocm != "s":
            print("Volviendo al menú anterior... 🔙")
            os.system("pause")  # Espera antes de regresar al menú
            break # 
        
       
