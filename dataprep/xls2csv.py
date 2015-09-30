import pandas as pd

#oes data is in xls, this will convert them to csvs.

def xls2csv(years, filename):
	for year in years:
		#function to convert the xls to csv and write to one file
		filepath = '/PATH/TO/DATA/oes/[YEAR]/state_M20[YEAR]_dl.xls'
		filepath = filepath.replace('[YEAR]',year)
		xls = pd.ExcelFile(filepath)
		df = xls.parse(thousands=',',na_values=['*','**'])
		df['YEAR'] = "20{0}".format(year)
		if year == '10':
			df.to_csv(filename, index=0)
		else:
			df.to_csv(filename, mode='a', header=False, index=0)


yearsoes = ['10','11','12','13']
xls2csv(yearsoes, 'oes20102013.csv')