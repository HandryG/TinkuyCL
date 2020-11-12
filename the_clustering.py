from sklearn.cluster import OPTICS
from data_io import get_tinkuy_coords_np 
import pandas as pd

def do_clustering():
  df = get_tinkuy_coords_np()
  #df = pd.to_numeric(df["latitud"], downcast="float")
  #df = pd.to_numeric(df["longitud"], downcast="float")
  #df = df[["latitud","longitud"]].to_numpy()
  clust  = OPTICS(min_samples=15).fit_predict(df)
  return clust

