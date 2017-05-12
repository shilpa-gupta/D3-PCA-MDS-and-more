import pandas as pd
from sklearn import manifold
import numpy as np
from sklearn import metrics

def get_MDS_Cordinates(inputFile, outputFile):
	df = pd.read_csv(inputFile, encoding="ISO-8859-1")
	movie_list = df["movie_title"]
	df.pop("movie_title")
	dataArray = df.values
	dis_mat = metrics.pairwise.pairwise_distances(dataArray, metric="euclidean")
	mds = manifold.MDS(n_components=2)
	arr_2d = mds.fit_transform(dis_mat)
	df_2d = pd.DataFrame(arr_2d, columns=['MDS-1','MDS-2'])
	df_2d["movie_title"] = movie_list
	df_2d = df_2d.set_index("movie_title")
	df_2d.to_csv(outputFile)
get_MDS_Cordinates("data/random_sample_2D.csv","data/random_sample_2D_MDS_euclidean_new.csv")