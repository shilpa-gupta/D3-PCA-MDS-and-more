import pandas as pd
import numpy as np
import sklearn
from sklearn.cluster import KMeans
"""
For K = 2
1083174158.4
For K = 3
480358174.144
For K = 4
267506583.249
For K = 5
171947965.477
for K = 6
120322438.342
for k = 7
88301381.3105
for k = 8
67003233.6413
for k = 9
52762696.9044
for k = 10
43215423.0233
for k = 11
35802826.759
for k = 12
29805569.9939
for k = 13
25295517.2723
for k = 14
21910613.1733
for k = 15
19280654.3805
"""

# Final K = 3
def strat_sampling(inputFile, outFile):
	with open(outFile,"w+") as output:
		df = pd.read_csv(inputFile,encoding="ISO-8859-1")
		indexs = df["movie_title"]
		df.pop("movie_title")
		df["index"] = df.index
		# print(df)
		dataArray = df.values
		# print(np.argwhere(np.isnan(dataArray)))
		# print(np.all(np.isfinite(dataArray)))
		kmeans = KMeans(n_clusters=3)
		kmeans.fit(dataArray)
		centroids = kmeans.cluster_centers_
		labels = kmeans.labels_
		# print(kmeans.inertia_)
		cluster1 = np.where(labels == 0)[0]
		cluster2 = np.where(labels == 1)[0]
		cluster3 = np.where(labels == 2)[0]
		"""
		cluster size 
		(1221,)
		(1246,)
		(1245,)
		"""
		np.random.shuffle(cluster1)
		strata1 = cluster1[:500]
		np.random.shuffle(cluster2)
		strata2 = cluster2[:500]
		np.random.shuffle(cluster3)
		strata3 = cluster3[:500]
		combinedArray = np.concatenate((dataArray[strata1],dataArray[strata2]), axis=0)
		combinedArray = np.concatenate((combinedArray,dataArray[strata3]),axis=0)
		finaldf = pd.DataFrame(combinedArray, columns=df.columns)
		finaldf["movie_title"] = indexs[finaldf["index"]]
		# print(finaldf)
		movie_list = []
		for index in finaldf["index"]:
			movie_list.append(indexs[index])
		# print(movie_list)
		# for index in finaldf["index"]:
		# 	print(index)
		# 	print(indexs[index])
		# print(int(finaldf["index"]))
		finaldf["movie_title"] = movie_list
		finaldf.pop("index")
		finaldf = finaldf.set_index("movie_title")
		finaldf.to_csv(outFile)

strat_sampling("data/normalized.csv","data/strat_sample.csv")