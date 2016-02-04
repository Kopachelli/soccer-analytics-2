#Merges Data Tables


import csv
import string
import re
import glob
import sys
import pandas as pd

def Merge():

	frames = []

	#Iterate through teams
	for csvFile in glob.glob('CSV/*csv'): #within the path of this folder, the csvs are stored in the /CSV folder.
		#iterate through each CSV file (mirroring each club in dataset)
		df = pd.read_csv(csvFile)
		
		frames.append(df)

	result = pd.concat(frames, axis=0, ignore_index=True)

	try:
		result.to_csv("finaltable.csv")
		print "Success"

	except Exception:
		print "Failed"


def Format():

	df = pd.read_csv("finaltable.csv")

	df["Won"] = df["W"].fillna('').map(str) + df["Won"].fillna('').map(str)
	df["Drawn"] = df["D"].fillna('').map(str) + df["Drawn"].fillna('').map(str)
	df["Lost"] = df["Lost"].fillna('').map(str) + df["L"].fillna('').map(str)
	df["Matches"] = df["Matches"].fillna('').map(str) + df["M"].fillna('').map(str)
	df["Played"] = df["Played"].fillna('').map(str) + df["P"].fillna('').map(str)
	df["GF"] = df["GF"].fillna('').map(str) + df["F"].fillna('').map(str)
	df["GA"] = df["GA"].fillna('').map(str) + df["A"].fillna('').map(str)

	df["Matches"] = df["Matches"].fillna('').map(str) + df["Played"].fillna('').map(str)

	df.to_csv("finaltable2.csv")


Format()