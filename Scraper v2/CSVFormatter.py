##THIS SCRIPT CLEANS UP / MAKES CSV FORMATTING CONSISTENT ACROSS ALL EPL MANAGER TABLES.

##TUTORIAL: http://stackoverflow.com/questions/31715033/loop-through-multiple-csv-files-copying-only-certain-columns-to-new-files

import csv
import string
import re
import glob
import sys
import pandas as pd


#Iterate through teams
for csvFile in glob.glob('CSV/*csv'): #within the path of this folder, the csvs are stored in the /CSV folder.
	#iterate through each CSV file (mirroring each club in dataset)
	df = pd.read_csv(csvFile)

	keep_cols = []

	header = df.columns.values.tolist()

	if "Name" in header:
		keep_cols.append("Name")
	if "Manager" in header:
		keep_cols.append("Manager")
 	if "From" in header:
		keep_cols.append("From")
	if "To" in header:
		keep_cols.append("To")
 	if "M" in header:
		keep_cols.append("M")
	if "Matches" in header:
		keep_cols.append("Matches")
	if "Played" in header:
		keep_cols.append("Played")
	if "P" in header:
		keep_cols.append("P")
	if "W" in header:
		keep_cols.append("W")
	if "Won" in header:
		keep_cols.append("Won")
	if "D" in header:
		keep_cols.append("D")
	if "Drawn" in header:
		keep_cols.append("Drawn")
	if "L" in header:
		keep_cols.append("L")
	if "Lost" in header:
		keep_cols.append("Lost")
	if "F" in header:
		keep_cols.append("F")
	if "GF" in header:
		keep_cols.append("GF")
	if "A" in header:
		keep_cols.append("A")
	if "GA" in header:
		keep_cols.append("GA")

	new_df = df[keep_cols]

	new_df.to_csv(csvFile, index=False)
	


