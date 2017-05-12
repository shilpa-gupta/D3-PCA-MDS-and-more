import pandas as pd
from sklearn import decomposition
import numpy as np
from numpy import linalg as LA

def FindingPCA(inputFile, outputFile):
	with open(outputFile,'w') as output:
		df = pd.read_csv(inputFile,encoding="ISO-8859-1")
		df = df.set_index("movie_title")
		pca = decomposition.PCA()
		pca.fit(df.values)
		i=np.identity(df.shape[1])
		coef = pca.transform(i)
		corrDf = pd.DataFrame(coef, columns=['PC-1','PC-2','PC-3','PC-4','PC-5','PC-6','PC-7','PC-8','PC-9','PC-10','PC-11','PC-12','PC-13','PC-14','PC-15','PC-16'], index=df.columns)
		corrDf.to_csv(outputFile)
# FindingPCA("data/random_sampled.csv","data/PCA_random_sample.csv")


def Calculate_sq_sum_Loadings(inputFile,outputFile):
	with open(outputFile, 'w') as output:
		df = pd.read_csv(inputFile, index_col=0)
		df['sque_sum_loadings'] = np.square(df).sum(axis=1)
		df.to_csv(outputFile)

# Calculate_sq_sum_Loadings("data/PCA_random_sample.csv", "data/PCA_random_sample_sq_loadings.csv")

def get_2D_Transform(inputFile, outputFile):
	df = pd.read_csv(inputFile, encoding="ISO-8859-1")
	movie_list = df["movie_title"]
	df.pop("movie_title")
	dataArray = df.values
	pca = decomposition.PCA(n_components =2)
	pca.fit(df.values)
	arr_2d = pca.transform(df.values)
	df_2d = pd.DataFrame(arr_2d, columns=['PC-1','PC-2'])
	df_2d["movie_title"] = movie_list
	df_2d = df_2d.set_index("movie_title")
	df_2d.to_csv(outputFile)

get_2D_Transform("data/random_sampled.csv","data/random_sample_2D.csv")

def finding_intrinsic_dimen_randomsample(inputFile, outputFile):
	with open(outputFile, 'w') as output:
		df = pd.read_csv(inputFile,encoding="ISO-8859-1")
		df = df.set_index("movie_title")
		cov_mat = np.cov(df.values.T)
		eig_vals, eig_vecs = np.linalg.eig(cov_mat)
		for val in eig_vals:
			print(val)

# finding_intrinsic_dimen_randomsample("data/strat_sample.csv", "data/eigan_values_strat_sample.csv")