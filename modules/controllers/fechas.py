import os
from modules.utils.validaciones import sololetras as sl,solonumeros as sn ,numerosyletras as nl
import json
import modules.utils.corefiles as cf
import modules.controllers.players as pl
import modules.controllers.teams as tm
DB_FILE="data/liga.json"

def addfechaspartidos():
    while True:

        dia=sn('Ingrese el dia del partido: ')
        mes=sn('Ingrese el mes del partido: ')
        año=sn('Ingrese el año del partido: ')
        

        fecha=(f"{dia}/{mes}/{año}")
        fechas={
            'fecha':fecha,
            'equipos':{}
        }
        cf.update_json(DB_FILE,fechas,[fecha])
        otrafecha=sl("Desea agregar otras fechas ? S/N").lower()
        if otrafecha != 's':
            os.system("pause")
            return fecha
            

