import psycopg2

#function to import csv to sql
def process_file(conn, table_name, file_object):
	sql_stmt = """
	COPY %s FROM STDIN WITH
		CSV
		HEADER
		DELIMITER AS ','
	"""
	cursor = conn.cursor()
	cursor.copy_expert(sql=sql_stmt % table_name, file=file_object)
	conn.commit()
	cursor.close()


def create_table(table_name):
	sql_stmt = """
	CREATE TABLE {0} (area_fips varchar, own_code varchar, industry_code varchar, agglvl_code varchar, size_code varchar, year varchar, qtr varchar, disclosure_code varchar, qtrly_estabs_count numeric, month1_emplvl numeric, month2_emplvl numeric, month3_emplvl numeric, total_qtrly_wages numeric, taxable_qtrly_wages numeric, qtrly_contributions numeric, avg_wkly_wage numeric, lq_disclosure_code varchar, lq_qtrly_estabs_count numeric, lq_month1_emplvl numeric, lq_month2_emplvl numeric, lq_month3_emplvl numeric, lq_total_qtrly_wages numeric, lq_taxable_qtrly_wages numeric, lq_qtrly_contributions numeric, lq_avg_wkly_wage numeric);
	""".format(table_name)
	cursor = conn.cursor()
	cursor.execute(sql_stmt, (table_name,))
	conn.commit()
	cursor.close()

#the years we want as strings
years = ['2010','2011','2012','2013','2014']

#open database connection
conn = psycopg2.connect("dbname=dewtrunc user=admin")

try:
	for year in years:
		table = 'qcew{0}'.format(year)
		create_table(table)
		if year == '2014':
			filename = "data/[YEAR].q1-q2.singlefile.csv"
			filename = filename.replace('[YEAR]',year)
			bls_data = open(filename)
			process_file(conn, table, bls_data)
		else:
			filename = "data/[YEAR].q1-q4.singlefile.csv"
			filename = filename.replace('[YEAR]',year)
			bls_data = open(filename)
			process_file(conn, table, bls_data)
finally:
	conn.close()