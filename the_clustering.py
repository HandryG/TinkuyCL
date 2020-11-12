#from sklearn.cluster import OPTICS
#import pandas as pd

from data_io import get_tinkuy_coords_np, get_tinkuy_coords_list
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.silhouette import silhouette_ksearch_type, silhouette_ksearch
import sys

def do_clustering(min_medoids,max_medoids):
  points = get_tinkuy_coords_list()
  sys.setrecursionlimit(4500)
  search_instance = silhouette_ksearch(points, 2, 10, algorithm=silhouette_ksearch_type.KMEDOIDS).process()
  amount = search_instance.get_amount()
  scores = search_instance.get_scores()
  k = max(scores, key=scores.get)
  initial_centers = kmeans_plusplus_initializer(points, amount).initialize()
  kmeans_instance = kmedoids(points, range(0,amount)).process()
  clusters   = kmeans_instance.get_clusters()
  medoids    = kmeans_instance.get_medoids()
  visualizer = cluster_visualizer()
  visualizer.append_clusters(clusters, points)
  #visualizer.show()

  medoid_points = []
  for medoid in medoids:
      medoid_points.append(points[medoid])
  
  return medoid_points

