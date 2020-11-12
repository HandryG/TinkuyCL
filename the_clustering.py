#from sklearn.cluster import OPTICS
#import pandas as pd

from data_io import get_tinkuy_coords_np, get_tinkuy_coords_list
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.silhouette import silhouette_ksearch_type, silhouette_ksearch

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


points = [[-12.05025679423635, -77.03324583436115],[-12.053308418145496, -77.03154783727447],\
    [-12.050965662079083, -77.0315933901085],[-12.052609930564596, -77.03643043749302],\
    [-12.049983623161909, -77.03460163736935],[-12.053816298287387, -77.03238549002167],\
    [-12.05252341321739, -77.03407842374864],[-12.049563010624647, -77.03447713113442],\
    [-12.054230354746393, -77.03190110407533],[-12.054834396207616, -77.03242732065735]]

#search_instance = silhouette_ksearch(points, 2, 10, algorithm=silhouette_ksearch_type.KMEDOIDS,ccore=True).process()
#amount = search_instance.get_amount()
#scores = search_instance.get_scores()

max_score = 0
amount = 2
for n_clusters in range(2,10):
    clusterer = KMeans(n_clusters=n_clusters)
    preds = clusterer.fit_predict(points)
    centers = clusterer.cluster_centers_
    score = silhouette_score(points, preds)
    if(score > max_score):
        max_score = score
        amount    = n_clusters
    #print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))

print(amount)
initial_centers = kmeans_plusplus_initializer(points, amount).initialize()
kmeans_instance = kmedoids(points, range(0,amount)).process()
clusters   = kmeans_instance.get_clusters()
medoids    = kmeans_instance.get_medoids()
#visualizer = cluster_visualizer()
#visualizer.append_clusters(clusters, points)
#visualizer.show()

medoid_points = []
for medoid in medoids:
    medoid_points.append(points[medoid])
    
print(medoid_points)

