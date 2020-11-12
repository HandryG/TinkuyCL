from sklearn.cluster import OPTICS
from data_io import get_tinkuy_coords_np 
import pandas as pd

def do_clustering():
  df = get_tinkuy_coords_np()
  clust  = OPTICS(min_samples=15).fit_predict(df)
  print('Cluster model done')
  return clust

