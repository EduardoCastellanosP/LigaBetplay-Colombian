import os
from modules.utils.validaciones import sololetras as sl,solonumeros as sn ,numerosyletras as nl
import json
import modules.utils.corefiles as cf
import modules.controllers.players as pl

DB_FILE="data/liga.json"

def addplayers(players: dict):
    
    while True:
        nombre = sl("Escriba el nombre del jugador: ")
        dorsal = sn("Ingrese el número de la dorsal: ")
        edad = sn("Ingrese la edad: ")

        player = {
            'dorsal': dorsal,
            'namePlayer': nombre,
            'edad': edad
        }
        players.update({dorsal: player})  # Usa la dorsal como identificador único
        cf.update_json(DB_FILE, players, [nombre])  # Actualiza el archivo JSON
        otroplayer = sl("¿Desea agregar otro jugador? (s/n): ").lower()

        if otroplayer != "s":
            print("Volviendo al menú anterior... 🔙")
            os.system("pause")  # Espera antes de regresar al menú
            break # Regresa al menú sin cerrar el programa
