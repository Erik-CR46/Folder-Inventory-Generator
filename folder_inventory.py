import os #Importaciones necesarias
import pandas as pd
from datetime import datetime

#Ruta de la carpeta que queremos analizar
ruta_base = r"C:\Users\tu_usuario\Downloads"

#Lista donde se va a guardar todos los datos
data = []

#Funcion para obtener la fecha y nombre del fichero mas reciente de cada carpeta
def obtener_archivo_reciente(ruta):
    archivo_reciente = None #Inicializamos estas variables pa poder ir comparando con la actual
    fecha_reciente = None

    try:

        #En este caso NO usamos walk porque iria bajando por subcarpetas y tardaria muchisimo
        #Solo miramos los ficheros directamente dentro de la carpeta

        for file in os.listdir(ruta): #Recorremos todo lo que hay en la carpeta
            filepath = os.path.join(ruta, file) #Unimos la ruta con el elemento

            if os.path.isfile(filepath):  #Comprobamos que sea fichero (no carpeta)
                try:
                    fecha = os.path.getmtime(filepath) #Sacamos la fecha del fichero

                    if fecha_reciente is None or fecha > fecha_reciente: #Nos quedamos con el mas reciente
                        fecha_reciente = fecha
                        archivo_reciente = file #Guardamos solo el nombre del fichero

                except:
                    continue

    except:
        return "", ""

    #Devolvemos nombre + fecha
    if archivo_reciente:
        return archivo_reciente, datetime.fromtimestamp(fecha_reciente)
    else:
        return "", ""


#Empieza el main haciendo un for con listdir de la ruta enviada
for lvl1 in os.listdir(ruta_base):

    path_lvl1 = os.path.join(ruta_base, lvl1) #Unimos la ruta con la carpeta donde estemos en el for

    if not os.path.isdir(path_lvl1): #En caso de que la iteraccion no sea una carpeta ignoramos
        continue

    print("Nivel 1:", lvl1)

    #Intentamos sacar subcarpetas de nivel 2
    try:
        subfolders_lvl2 = []

        for f in os.listdir(path_lvl1):
            ruta = os.path.join(path_lvl1, f)

            if os.path.isdir(ruta):
                subfolders_lvl2.append(f)

    except:
        print("❌ Error en nivel 1:", path_lvl1)
        continue


    #Caso: no tiene subcarpetas nivel 2
    if not subfolders_lvl2:

        archivo, fecha = obtener_archivo_reciente(path_lvl1)

        data.append({
            "Nivel 1": lvl1,
            "Nivel 2": "",
            "Nivel 3": "",
            "Fichero más reciente": archivo,
            "Antigüedad": fecha,
        })


    else:
        for lvl2 in subfolders_lvl2:

            path_lvl2 = os.path.join(path_lvl1, lvl2)

            print("   Nivel 2:", lvl2)

            try:
                subfolders_lvl3 = []

                for f in os.listdir(path_lvl2):
                    ruta = os.path.join(path_lvl2, f)

                    if os.path.isdir(ruta):
                        subfolders_lvl3.append(f)

            except:
                print("❌ Error en nivel 2:", path_lvl2)
                continue


            #Caso: no hay nivel 3
            if not subfolders_lvl3:

                archivo, fecha = obtener_archivo_reciente(path_lvl2)

                data.append({
                    "Nivel 1": lvl1,
                    "Nivel 2": lvl2,
                    "Nivel 3": "",
                    "Fichero más reciente": archivo,
                    "Antigüedad": fecha,
                })


            else:
                for lvl3 in subfolders_lvl3:

                    path_lvl3 = os.path.join(path_lvl2, lvl3)

                    print("      Nivel 3:", lvl3)

                    archivo, fecha = obtener_archivo_reciente(path_lvl3)

                    data.append({
                        "Nivel 1": lvl1,
                        "Nivel 2": lvl2,
                        "Nivel 3": lvl3,
                        "Fichero más reciente": archivo,
                        "Antigüedad": fecha,
                    })


# exportar Excel
df = pd.DataFrame(data)
df.to_excel("inventario_carpetas_rapido.xlsx", index=False)

print("✅ Excel generado correctamente")