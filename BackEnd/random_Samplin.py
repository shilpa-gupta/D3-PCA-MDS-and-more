import pandas as pd
#Random Sampling of cleaned data
def randomSample(inputFile):
	df = pd.read_csv(inputFile, encoding="ISO-8859-1")
	print(df.head())
	random_sampled_df = df.sample(n=1500)
	print(random_sampled_df.head())
	print(len(random_sampled_df))
	random_sampled_df.to_csv("data/random_sampled.csv",index=False)

randomSample("data/normalized.csv")