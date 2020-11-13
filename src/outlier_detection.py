from sklearn.cluster import DBSCAN
import numpy as np

#Se recibe una lista de listas ([longitud,latitud])
#Se devuelven los labels de los puntos (los que tengan -1 son outliers)
def eliminate_outliers(points):
    array = np.array(points)
    clustering = DBSCAN(eps=0.001, min_samples=5).fit(array)
    return clustering.labels_
