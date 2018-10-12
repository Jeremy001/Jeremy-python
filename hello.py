
# coding: utf-8

import csv

csv_file = open('/Users/yunshan/Documents/Jeremy-python/test_sh.csv', 
	'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['sid', 'sname'])

sid = 1001
sname = 'yunshan'

csv_writer.writerow([sid, sname])

csv_file.close()