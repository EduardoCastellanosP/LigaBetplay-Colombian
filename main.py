#ligabetplay por modulos, debo hacer todo de la liga betplay e ingresarlo a modulos, con funciones y poniendo las validaciones.
import modules.utils.menus as msg
import modules.utils.opcion as op
import modules.controllers.teams as tm
import modules.controllers.players as pl
import modules.controllers.cuerpomedico as cm
import modules.controllers.cuerpotecnico as ct
import modules.controllers.estadisticas as st
import modules.controllers.fechas as fe
from modules.utils.validaciones import sololetras as sl,solonumeros as sn ,numerosyletras as nl
import os
import json
DB_FILE="data/liga.json"

ligabetplay={}

ligabetplay={}

if __name__ == "__main__":

    while True:
        
        print(msg.title)
        msg.crearmenu1()
        opcion=op.opciones()
        
        match opcion:
            case 1:
                while True:
                    msg.crearmenu2()
                    opcion2=op.opcion2()
                    os.system('cls')

                    match opcion2:
                        case 1:
                            print(msg.title2)
                            for key, value in ligabetplay.items():
                                print(f'{key}.{value.get('name')}')
                            tm.addteams(ligabetplay)
                            os.system('cls')
                            
                        case 2:
                            while True:
                                print(msg.title3)
                                os.system('cls')
                                for key, value in ligabetplay.items():
                                    print(f"{key}. {value.get('name')}")
                                
                                teamselect=sn("Seleccione el equipo donde desea agregar el jugador: ")
                                
                                if teamselect in ligabetplay:
                                     
                                     pl.addplayers(ligabetplay.get(teamselect).get('players'))  
                                     break  
                                else:
                                     print("⚠️ Equipo no encontrado. Intente de nuevo.")
                                     

                        case 3:
                            while True:
                                print(msg.title4)
                                for key, value in ligabetplay.items():
                                    print(f'{key}. {value.get('name')}')
                                teamselect=sn("Seleccion el equipo donde desea agregar el cuerpo medico: ")

                                if teamselect in ligabetplay:
                                    cm.addcuerpomedico(ligabetplay.get(teamselect).get('cuerpomd'))
                                    break
                                else:
                                    print("⚠️ Equipo no encontrado. Intente de nuevo.")

                        
                
                        case 4:
                            while True:
                                print(msg.title5)

                                for key, value in ligabetplay.items():
                                    print(f'{key}. {value.get('name')}')
                                teamselect=sn("Seleccione el equipo donde desea agregar el cuerpo tecnico: ")
                                if teamselect in ligabetplay:
                                    ct.addcuerpotec(ligabetplay.get(teamselect).get('cuerpotec'))
                                    break
                                else:
                                        print("⚠️ Equipo no encontrado. Intente de nuevo.")

                        case 5:
                            while True:
                                print(msg.title6)
                                for key, value in ligabetplay.items():
                                    print(f'{key}.{value.get('name')}')
                                teamselect=sn("Seleccione el equipo: ")

                                if teamselect in ligabetplay:
                                    st.addestatics(ligabetplay.get(teamselect).get('estadisticas'))
                                    break
                                else:
                                    print("⚠️ Equipo no encontrado. Intente de nuevo.")
                          

                        case 6:
                            print("Volviendo al menú principal... 🔙")
                            break

                        case _:
                            print("Opcion invalida")
            case 2:
              
                while True:
                    print(msg.title7)
                    
                    for key, value in ligabetplay.items():
                        print(f"{key}. {value.get('name')}")

                    # Pedir equipos sin usar key directamente en el mensaje
                    teamselect1 = sn("Seleccione el equipo 1: ")
                    teamselect2 = sn("Seleccione el equipo 2: ")

                    if teamselect1 not in ligabetplay or teamselect2 not in ligabetplay:
                        print("⚠️ Uno o ambos equipos no existen. Intente de nuevo.")
                        continue  # Volver a pedir los equipos si la selección es incorrecta

                    print(f"{ligabetplay.get(teamselect1).get('name')} 🆚 {ligabetplay.get(teamselect2).get('name')}")

                    # Pasar los equipos a la función
                    fecha = fe.addfechaspartidos()
                    

                    print(msg.title7)
                    print(f" {ligabetplay[teamselect1]['name']} vs {ligabetplay[teamselect2]['name']} ")
                    print(f'{fecha}')
                    

                    break  


                

            case 3:
                print("Saliendo, adios")
                break
