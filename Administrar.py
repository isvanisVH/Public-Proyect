import os
import shutil

CARPETA = input("Introdusca la ruta de la carpeta a organizar: ")
CATEGORIAS = {
    "Imagenes": [".jpg", ".png", ".gif", ".jpeg"],
    "Document": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Comprimidos": [".zip", ".rar", ".7z"],
    "Codigo": [".py", ".js", ".html",".css"] ,
    "Ejecutables": [".exe"]
}

def organizar():
    for archivo in os.listdir(CARPETA):#Iteramos en la carpeta dada
        ruta = os.path.join(CARPETA, archivo) #direccion y archivo
        if os.path.isfile(ruta):#si hay un archivo en la ruta 
            _, extension = os.path.splitext(archivo)# Desenpaquetamos (nombre, extencion)
            for categoria, extensiones in CATEGORIAS.items():#Iteramos en el diccionario
                if extension.lower() in extensiones:#si la extencion esta dentro de las extenciones registradas en minuscula
                    carpeta_destino = os.path.join(CARPETA, categoria)#Entonces guardamos en la carpeta de destino la direccion 
                    os.makedirs(carpeta_destino, exist_ok=True)#Creamos la carpeta si existe
                    shutil.move(ruta, os.path.join(carpeta_destino, archivo))#Movemos el file desde la ruta actual a la ruta de destino
                    print(f"✅{archivo} -> {categoria}")#mostramos el archivo que ha sido movido y su categoria
                    
organizar()