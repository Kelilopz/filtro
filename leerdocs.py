import json
import csv

import os

#Escribir al Json           
def guardarcambiosjson(datos,archivo):
    with open(archivo,'w') as archivonew:
        escritura = json.dumps(datos , indent = 4)
        archivonew.write(escritura)
        print("Tus datos han sido guardados EXITOSAMENTE")
    

#Leer al Json
def CargarDatosjson(archivo): 
    try:   
        with open(archivo,'r') as file:
            respuesta = json.load(file)
            return respuesta
    except Exception:
        return []
    
#Escribir al CSV    
def guardarcambioscsv(datos,archivo):
    with open(archivo,'w') as archivonew:
        escritura = csv.dumps(datos , indent = 4)
        archivonew.write(escritura)
        print("Tus datos han sido guardados EXITOSAMENTE")
    

#Leer al Csv
def CargarDatoscsv(archivo): 
    
    with open(archivo,"r") as csvfile:
        reader = csv.reader(csvfile)
        listaPlatos=[]
        for row in reader:
            listaPlatos.append(row)
        return (listaPlatos) 

        
def limpiarTerminal():
    # Verifica si el sistema operativo es Windows
    if os.name == 'nt':
        _ = os.system('cls')  # Limpia la terminal en Windows
    else:
        _ = os.system('clear')  # Limpia la terminal en sistemas Unix (Linux, macOS)


