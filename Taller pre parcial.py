#importo la librería
import numpy as np
import pandas as pd

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


