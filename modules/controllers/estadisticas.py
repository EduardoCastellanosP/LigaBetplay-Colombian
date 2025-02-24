from modules.utils.validaciones import sololetras as sl, solonumeros as sn
import os
import json
import modules.utils.corefiles as cf
import modules.controllers.players as pl
import modules.controllers.teams as tm
DB_FILE = "data/liga.json"

def addestatics(estadisticas:dict):
        while True:

            pj=sn("Ingrese los partidos jugados: ")
            pg=sn("Ingrese los partidos ganados: ")
            pe=sn("Ingrese los partidos empatados: ")
            pp=sn("Ingrese los partidos perdidos: ")
            gf=sn("Ingrese los partidos goles a favor: ")
            gc=sn("Ingrese los partidos goles en contra: ")
            
       
            
            tp=(pj+pg+pe+pp+gf+gc)
            juego={
                
                    "pj":pj,
                    "pg":pg,
                    "pe":pe,
                    "pp":pp,
                    "gf":gf,
                    "gc":gc,
                    "tp":tp

                    }

            estadisticas.update(juego )
            cf.update_json(DB_FILE,juego, ["estadisticas"])  # Actualiza el archivo JSON
            otraestad=sl("¿Desea agregar otras estadisticas? (s/n): ").lower()

            if otraestad != "s":
                print("Volviendo al menú anterior... 🔙")
                os.system("pause")  # Espera antes de regresar al menú
                break # 

                