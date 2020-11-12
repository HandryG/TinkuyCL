from sklearn.cluster import OPTICS
from data_io import get_tinkuy_coords_df 
import pandas as pd

def do_clustering():
  df = get_tinkuy_coords_df()
  df = pd.to_numeric(df[["latitud","longitud"]], downcast="float")
  df = df[["latitud","longitud"]].to_numpy()
  clust  = OPTICS(min_samples=15).fit_predict(df)
  return clust

