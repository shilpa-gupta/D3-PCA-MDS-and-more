
import pandas as pd
# print all the titles
def printTitle(dataFile):
	with open(dataFile,'r') as input:
		count = 0;
		for line in input:
			count += 1
			if(count == 1):
				headings = line.split(",")
				for head in headings:
					print(head + '\n')

'''
color --> remove [0]
director_name--> remove [1] 
num_critic_for_reviews --> numeric [2]
duration --> numeric [3]
director_facebook_like --> numeric [4]
actor_3_facebook_likes -- numeric [5]
actor_2_name --> remove [6]
actor_1_facebook_likes --> numeric [7]
gross --> numeric [8]
genres --> remove [9]
actor_1_name --> remove [10]
movie_title  --> unique [11]
num_voted_users --> numeric [12]
cast_total_facebook_likes --> numeric [13]
actor_3_name --> remove [14]
facenumber_in_poster --> numeric [15]
plot_keywords --> remove [16]
movie_imdb_link --> remove [17]
num_user_for_reviews --> numeric [18]
language --> remove [19]
country --> remove [20]
content_rating --> remove [21]
budget --> numeric [22]
title_year --> time [23]
actor_2_facebook_likes --> numeric [24]
imdb_score --> numeric [25]
aspect_ratio --> numeric [26]
movie_facebook_likes --> numeric [27]
'''
# Removing unnecessory columns as mentioned in comments above
def removeExtraColumns(inputFile,outputFile):
	keepingIndex = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
	count = 0
	with open(inputFile, 'r', encoding="utf8") as input:
		with open(outputFile, 'w+') as output:
			for line in input:
				newRow = []
				# if count == 0:
				# 	newRow.append("id")
				# else:
				# 	newRow.append(count)
				print(count)
				count += 1
				row = line.split(",")
				for idx,item in enumerate(row):
					if idx in keepingIndex:
						newRow.append(item)
				if len(newRow) == 17:
					output.write(','.join(str(x) for x in newRow))
					# output.write("\n")

# removeExtraColumns("data/column_removed.csv","data/Only_Numeric_cols.csv")

def norm_data(inputFile, outputFile):
	df = pd.read_csv(inputFile, encoding="ISO-8859-1")
	result = df.copy()
	result = result.set_index("movie_title")
	for feature_name in result.columns:
		max_value = df[feature_name].max()
		min_value = df[feature_name].min()
		result[feature_name] = (result[feature_name] - min_value)/(max_value - min_value)
	result.to_csv(outputFile)

norm_data("data/Only_Numeric_cols.csv","data/normalized.csv")