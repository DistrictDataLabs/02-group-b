from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen


years = ['2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
def getData(years):
	for year in years:
		urlPath = 'http://www.bls.gov/cew/data/files/[YEAR]/csv/[YEAR]_qtrly_singlefile.zip'
		urlPath = urlPath.replace('[YEAR]',year)
		url = urlopen(urlPath)
		zipfile = ZipFile(StringIO(url.read()))
		zipfile.extractall('data')

getData(years)
	