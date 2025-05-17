#importo la librería
import numpy as np
import pandas as pd
from scipy.io import loadmat
import os 

#matriz aleatioria de 4 dimendiones con size de 1200000
matriz = np.random.rand(20,30,40,50)

#se crea la copia seleccionando la parte que deseo quitar
copia_3d = matriz[0].copy()

#Atributos de la matriz
print("Atributos de la matriz")
print("Forma (shape):", copia_3d.shape)        
print("Número de dimensiones (ndim):", copia_3d.ndim) 
print("Tamaño total (size):", copia_3d.size)    
print("Tipo de datos (dtype):", copia_3d.dtype)  
print("Tamaño de cada elemento (itemsize):", copia_3d.itemsize, "bytes")
print("Memoria total ocupada (nbytes):", copia_3d.nbytes, "bytes")
print("Tipo del objeto:", type(copia_3d))

#Se modifica la matriz y se pasa a 2D
copia_2D = copia_3d.reshape(1200,50)

#función para convertir matriz 2D a data frame
def data_frame(arreglo):
    DF = pd.DataFrame(arreglo)
    return DF

#llamado a la función
DF_copia2D = data_frame(copia_2D)

def cargar_archivo(ruta):
    extension = os.path.splitext(ruta)[1].lower() #divide el nombre en dos y [1] es la extension ya sea .csv o .mat

    if extension == '.csv':
        df = pd.read_csv(ruta) #devuelve un archivo listo para ser usado en pandas, algo así como tabla
        print("El archivo csv fue cargado correctamente")
        return df
    
        
    elif extension == '.mat':
        data = loadmat(ruta) #devuelve un diccionario
        print("Archivo mat fue cargado correctamente.")
        return data
    
    else:
        raise ValueError("Formato no soportado. Solo se aceptan archivos .csv y .mat")

def suma(array, eje=None):
    return np.sum(array, axis=eje) 
    
def restar(array1, array2):
    return np.subtract(array1, array2)

def multiplicar(array, eje=None):
    return np.prod(array, axis=eje)

def dividir(array1, array2):
    return np.divide(array1, array2)

def logaritmo(array, base=np.e):
    if base == np.e:
        return np.log(array)
    else:
        return np.log(array) / np.log(base)

def promedio(array, eje=None):
    return np.mean(array, axis=eje)

def desviacion_estandar(array, eje=None):
    return np.std(array, axis=eje)


