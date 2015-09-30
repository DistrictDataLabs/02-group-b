from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen


#define the years you want. QCEW uses 4-digit, OES uses 2-digit years in their file names.
#years = ['2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
#yearsoes = ['09','10','11','12','13']

def getData(years):
	for year in years:
		#to download OES data, use the the link below
		#urlPath = 'http://www.bls.gov/oes/special.requests/oesm[YEAR]st.zip'
		
		#to download QCEW data, use the link below
		#urlPath = 'http://www.bls.gov/cew/data/files/[YEAR]/csv/[YEAR]_qtrly_singlefile.zip'
		
		urlPath = urlPath.replace('[YEAR]',year)
		url = urlopen(urlPath)
		zipfile = ZipFile(StringIO(url.read()))
		
		#this extracts each zip to a file sorted by year. this is necessary because BLS uses the same file name for the metadata over multiple years.
		filepath = 'FILE PATH/{0}'.format(year)
		zipfile.extractall(filepath)

getData(yearsoes)
	