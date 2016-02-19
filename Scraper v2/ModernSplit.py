#Splits Table by Modern-Era

import csv
import string
import re
import glob
import sys
import pandas as pd
from datetime import datetime

def Split():

	#Define File References
	df = pd.read_csv("FinalData.csv")

	for date in df["From"]:

		print type(date)

		try:
			date = datetime.strptime(date, "%y-%b-%d")

		except Exception:
			pass

		print type(date)


Split()