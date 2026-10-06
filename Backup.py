import os #Interprete del sistema
import shutil #Powershell
import time #Tiempo
from datetime import datetime #Fechas

carpeta_trabajo = "D:\\VS_Code_3\\Python" # Almacenando ruta de la carpeta que se va utilizar
carpeta_backup = "D:\\VS_Code_3\\Backup_Automatico" # Almacenando ruta de la carpeta donde se va almacenar el archivo.zip
j = 1


def hacer_backup(): #delcaracion de la funcion
    try:
        #Crear la carpeta de backups si no exite:
        if not os.path.exists(carpeta_backup): #Si no(el interprete del sistema.en la direccion.existe(carpeta_backup = Ruta de la carpeta donde se va a almacenar))
            os.makedirs(carpeta_backup) #Interprete del sistema. crea una carpeta(carpeta_backup = ruta donde se va a almacenar)
            print(f"Carpeta de backups creada: {carpeta_backup}") #Mensaje de carpeta creada
        
        fecha = datetime.now().strftime("%Y%m%d_%H%M%S") #Almacenando la fecha actual.de la siguiente forma(ano, mes, dia_ hora, minutos, segundos)
        nombre_zip = f"backup_{fecha}.zip" # Almacenando el nombre de el archivo.zip 
        
        #Verificar que la carpeta de trabajo existe
        if not os.path.exists(carpeta_trabajo): #Si no( elinterprete del sistema.en la direccion.exixte(carpeta_trabajo = ruta en la que se trabaja))
            print(f"❌Error: La carpeta {carpeta_trabajo} no existe") #Mostrando mensaje de error pq la carpeta de trabajo no existe
            return #Salir del try
        
        shutil.make_archive(nombre_zip.replace('.zip', ''), 'zip', carpeta_trabajo) # El powershell.creame un archivo .zip(nombre_zip = nombre del archivo. remplazame(el .zip,por un espacio), y comprimelo en un zip, con el contenido de carpeta_trabajo = ruta de la carpeta que se usa)
        shutil.move(nombre_zip, os.path.join(carpeta_backup, nombre_zip)) #El powershell.mueve este archivo con el nombre(nombre_zip = nombre del archivo, interprete del sistema.en la siguiente direccion.junta esto(carpeta_backup = ruta donde se va a almacenar, nombre del archivo))
        print(f"Backup guardado: {nombre_zip}") #Mensaje de confirmacion exitosa
        
        print("El programa se esta corriendo correctamente: ") #Mensaje de que se esta corriendo correctamente: 
        
    except Exception as e:
        print(f"❌Error en backup: {e}") # Mensaje de error
    
#Ejecutar una vez antes del bucle
hacer_backup()

#Luego el bucle infinito
while True:
    hora_registro = datetime.now().strftime("%H / %M / %S")
    time.sleep(300) #Espera 5 min
    print(f"{j} Registro: {hora_registro}")
    j += 1
    hacer_backup() #LLamando la funcion