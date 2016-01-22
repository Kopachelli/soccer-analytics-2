##THIS SCRIPT CLEANS UP / MAKES CSV FORMATTING CONSISTENT ACROSS ALL EPL MANAGER TABLES.

##TUTORIAL: http://stackoverflow.com/questions/31715033/loop-through-multiple-csv-files-copying-only-certain-columns-to-new-files

import csv
import string
import re
import glob

#Iterate through teams
for csvFile in glob.glob('CSV/*csv'): #within the path of this folder, the csvs are stored in the /CSV folder.
	f = open(csvFile)
	csv_f = csv.reader(f)

	print "---------"
	print csvFile
	print "---------"

