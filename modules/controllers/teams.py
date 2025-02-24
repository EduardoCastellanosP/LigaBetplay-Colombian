from modules.utils.validaciones import sololetras as sl,solonumeros as sn ,numerosyletras as nl
import os
import modules.utils.corefiles as cf
import json
import modules.controllers.players as pl
import modules.controllers.teams as tm
DB_FILE="data/liga.json"

def addteams(ligabetplay:dict):
    while True:

        name=sl("Ingrese el nombre del equipo: ")
        team={
            "name": name,
            "players": {},
            "cuerpomd":{},
            "cuerpotec":{},
            "estadisticas":{
                "pj":0,
                "pp":0,
                "pg":0,
                "pe":0,
                "gf":0,
                "gc":0

            }
           
        }
        

        cf.update_json(DB_FILE,team,[name])
        team.update({'name':name})
        ligabetplay.update({len(ligabetplay)+1:team})
        otroteam=sl('Desea agregar otro Equipo S/N: ').lower()
        if otroteam !='s':
            print("Volviendo al menú anterior... 🔙")
            os.system('pause')  # Espera antes de regresar al menú
            break


    
    

