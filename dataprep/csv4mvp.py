import pandas as pd
import numpy as np
import csv

#imports csv
def csvimport(path):
	data = pd.DataFrame.from_csv(path, header=0)
	return data

#makes a list of new column names
def colnames(industries):
	#make list of new cols for all industries with value as their emp lvl lq in june 2014
	newcols = list()
	for industry in industries:
		colname = "lq_{0}".format(industry)
		newcols.append(colname) 
	return newcols

#sorts the data into a dictionary where each fips is a key, and it has all 17 industries linked to lq
def sortdata(data, industries, fips, newcols):
	clean = {}
	for fip in fips:
		lqs = {}
		for col in newcols:
			#since there are multiple values per industry for some areas, we're taking the mean until we figure out what's up
			lq = data["lq_month3_emplvl"].loc[(data.index == fip) & (data["industry_code"] == industries[newcols.index(col)])].mean()
			lqs.update({col : lq})
		clean.update({fip : lqs})
	return clean

#makes everything into a csv with desired colnames
def csvmaker(fieldnames, filename, final, fips):
	with open(filename, 'w') as csvfile:
    	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    	writer.writeheader()
    	for fip in fips:
    		row = {'fips': fip}
    		row.update(final[fip])
    		writer.writerow(row)

#initialize all the things!
path = 'mvp020715.csv'
data = csvimport(path)
industries = list(np.unique(data['industry_code']))
fips = list(np.unique(data.index))
fieldnames = ['fips', 'lq_10', 'lq_11', 'lq_21', 'lq_22', 'lq_23', 'lq_42', 'lq_51', 'lq_52', 'lq_53', 'lq_54', 'lq_55', 'lq_56', 'lq_61', 'lq_62', 'lq_71', 'lq_72', 'lq_81', 'lq_92', 'lq_99']
filename = 'mvpclean020715.csv'

#run all the functions!
newcols = colnames(industries)
final = sortdata(data, industries, fips, newcols)
csvmaker(fieldnames, filename, final, fips)
