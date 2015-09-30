
##this will take a csv of county fips in csv format and convert to a string with each code separated by a common, suitable for a massive sql query
import csv

fips = open('PATH TO CSV', 'r')
allfips = list()
final = ''

reader = csv.reader(fips, delimiter=',')

for row in reader:
	string = str(row).strip('[]')
	allfips.append("{0},".format(string))

for line in allfips:
	final += str(line)

with open("allthefips.txt","w") as f:
	f.write(final)
