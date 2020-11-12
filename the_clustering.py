from sklearn.cluster import OPTICS
from data_io import get_tinkuy_coords_df 

def do_clustering():
  df = get_tinkuy_coords_df()
  df = df[["latitud","longitud"]].to_numpy()
  clust  = OPTICS(min_samples=15).fit_predict(df)
  return clust

