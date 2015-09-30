import pandas as pd
import numpy as np
import csv

#this does not use pandas well. figure out how to do data editing via pandas instead of dictionaries.

#imports csv
def csvimport(path):
	data = pd.DataFrame.from_csv(path, header=0)
	data = data.loc[(data["GROUP"] == "major") & (data.index <= 56),]
	return data

#makes a list of new column names
def colnames(industries, nums):
	#make list of new cols for all industries with value as their emp lvl lq in june 2014
	columns = {}
	for industry in industries:
		newcols = list()
		for num in nums:
			colname = "{0}_{1}".format(num,industry[0:2])
			newcols.append(colname) 
		columns.update({industry : newcols})
	return columns

#sorts the data into a dictionary where each state ID is a key, then each year, then has all OCC data marked by industry
def sortdata(data, industries, fips, newcols, years):
	clean = {}
	for fip in fips:
		newYear = {}
		for year in years:
			newOCC= {}
			for industry in industries:
				#double check to make sure there aren't more values per code; cursory check says no
				lq = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year), "LOC QUOTIENT"].values
				tot_emp = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year),"TOT_EMP"].values
				emp_prse = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year),"EMP_PRSE"].values
				jobs_1000 = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year),"JOBS_1000"].values
				h_median = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year),"H_MEDIAN"].values
				a_median = data.loc[(data.index == fip) & (data["OCC_CODE"] == industry) & (data["YEAR"] == year),"A_MEDIAN"].values

				try:
					lq = lq[0]
					tot_emp = tot_emp[0]
					emp_prse = emp_prse[0]
					jobs_1000 = jobs_1000[0]
					h_median = h_median[0]
					a_median = a_median[0]
				except IndexError:
					lq = lq
					tot_emp = tot_emp
					emp_prse = emp_prse
					jobs_1000 = jobs_1000
					h_median = h_median
					a_median = a_median
				newOCC.update({newcols[industry][0] : lq, newcols[industry][1] : tot_emp, newcols[industry][2] : emp_prse, 
					newcols[industry][3] : jobs_1000, newcols[industry][4] : h_median, newcols[industry][5] : a_median})
			newYear.update({year : newOCC})
		clean.update({fip : newYear})
	return clean

#makes everything into a csv with desired colnames
def csvmaker(fieldnames, filename, final, fips, years):
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for fip in fips:
			for year in years:
				row = {'state' : fip, 'year' : year}
				row.update(final[fip][year])
				writer.writerow(row)

#initialize all the things!
path = 'oes20102013.csv'
data = csvimport(path)
industries = list(np.unique(data['OCC_CODE']))
nums = ['lq', 'tot_emp', 'emp_prse', 'jobs_1000', 'h_median', 'a_median']
years = [2010, 2011, 2012, 2013]
state = list(np.unique(data.index))
fieldnames = ['state', 'year', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_11', 'tot_emp_11', 'emp_prse_11', 'jobs_1000_11', 'h_median_11', 'a_median_11', 'lq_13', 'tot_emp_13', 'emp_prse_13', 'jobs_1000_13', 'h_median_13', 'a_median_13', 'lq_15', 'tot_emp_15', 'emp_prse_15', 'jobs_1000_15', 'h_median_15', 'a_median_15', 'lq_17', 'tot_emp_17', 'emp_prse_17', 'jobs_1000_17', 'h_median_17', 'a_median_17', 'lq_19', 'tot_emp_19', 'emp_prse_19', 'jobs_1000_19', 'h_median_19', 'a_median_19', 'lq_21', 'tot_emp_21', 'emp_prse_21', 'jobs_1000_21', 'h_median_21', 'a_median_21', 'lq_23', 'tot_emp_23', 'emp_prse_23', 'jobs_1000_23', 'h_median_23', 'a_median_23', 'lq_25', 'tot_emp_25', 'emp_prse_25', 'jobs_1000_25', 'h_median_25', 'a_median_25', 'lq_27', 'tot_emp_27', 'emp_prse_27', 'jobs_1000_27', 'h_median_27', 'a_median_27', 'lq_29', 'tot_emp_29', 'emp_prse_29', 'jobs_1000_29', 'h_median_29', 'a_median_29', 'lq_31', 'tot_emp_31', 'emp_prse_31', 'jobs_1000_31', 'h_median_31', 'a_median_31', 'lq_33', 'tot_emp_33', 'emp_prse_33', 'jobs_1000_33', 'h_median_33', 'a_median_33', 'lq_35', 'tot_emp_35', 'emp_prse_35', 'jobs_1000_35', 'h_median_35', 'a_median_35', 'lq_37', 'tot_emp_37', 'emp_prse_37', 'jobs_1000_37', 'h_median_37', 'a_median_37', 'lq_39', 'tot_emp_39', 'emp_prse_39', 'jobs_1000_39', 'h_median_39', 'a_median_39', 'lq_41', 'tot_emp_41', 'emp_prse_41', 'jobs_1000_41', 'h_median_41', 'a_median_41', 'lq_43', 'tot_emp_43', 'emp_prse_43', 'jobs_1000_43', 'h_median_43', 'a_median_43', 'lq_45', 'tot_emp_45', 'emp_prse_45', 'jobs_1000_45', 'h_median_45', 'a_median_45', 'lq_47', 'tot_emp_47', 'emp_prse_47', 'jobs_1000_47', 'h_median_47', 'a_median_47', 'lq_49', 'tot_emp_49', 'emp_prse_49', 'jobs_1000_49', 'h_median_49', 'a_median_49', 'lq_51', 'tot_emp_51', 'emp_prse_51', 'jobs_1000_51', 'h_median_51', 'a_median_51', 'lq_53', 'tot_emp_53', 'emp_prse_53', 'jobs_1000_53', 'h_median_53', 'a_median_53']
filename = 'oesclean021515.csv'

#run all the functions!
newcols = colnames(industries, nums)
final = sortdata(data, industries, state, newcols, years)
csvmaker(fieldnames, filename, final, state, years)