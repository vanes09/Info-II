#importo la librería
import numpy as np

#matriz aleatioria de 4 dimendiones con size de 1200000
matriz = np.random.rand(20,30,40,50)

#se crea la copia seleccionando la parte que deseo quitar
copia_3d = matriz[0].copy()

print("Atributos de la matriz")
print("Forma (shape):", copia_3d.shape)        
print("Número de dimensiones (ndim):", copia_3d.ndim) 
print("Tamaño total (size):", copia_3d.size)    
print("Tipo de datos (dtype):", copia_3d.dtype)  # float64 por defecto
print("Tamaño de cada elemento (itemsize):", copia_3d.itemsize, "bytes")
print("Memoria total ocupada (nbytes):", copia_3d.nbytes, "bytes")
print("Tipo del objeto:", type(copia_3d))
