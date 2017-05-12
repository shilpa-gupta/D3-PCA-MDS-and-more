def get_Scatter_matrix(inputFile, outputFile):
	df = pd.read_csv(inputFile, encoding="ISO-8859-1")
	df = df.set_index("movie_title")
	