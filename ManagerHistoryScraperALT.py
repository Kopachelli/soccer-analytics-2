#In: URL
#Out: CSV of Manager Information
#ON GITHUB NOW

#Print Header
print "Manager History - Data Mining Script"
print "Version 1"
print " "

print "Professor Eric Schwartz"
print "Naman Gupta"
print " "
print "-----------------------------------------------"
print "Data Sourced from WikiPedia"
print "-----------------------------------------------"
print " "

#Import Necessary Modules & Libraries
import requests
import string
import re
from bs4 import BeautifulSoup
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DataScraper:
	"Class that handles all Data Scraping Instance/Class Vars & Methods"

	def __init__(self, url):
		"Instance Variables of Data Scraper Class"
		self.url = url
		self.headerSet = []
		self.managerSet = []


	def runScraper(self):
		"Will Run Data Scraping"

		res = requests.get(self.url)
		soup = BeautifulSoup(res.content, "html.parser")

		#Handling for the possiblity that the first table might not be the manager...
		#If there are at least 12 rows in the table, we can assume that we are now talking about managerial history
		if len(soup.find_all(class_="wikitable")[0].find_all("tr")) > 12:
			managerTable = soup.find_all(class_="wikitable")[0]
		else:
			managerTable = soup.find_all(class_="wikitable")[1]

		#Iterate through headers of the table, storing the text in the <th> tags.
		for th in managerTable.find_all("th"):
			self.headerSet.append(th.find(text=True).encode('utf-8'))

		self.headerSet = tuple(self.headerSet)

		#Scraping Individual Manager Data Rows
		for tr in managerTable.find_all("tr"): #iterate through each row in table element
			dataElementSet = tr.findAll("td") #gives set of table data for each table row
			managerInfo = [] #Initialize List which will capture each manager's data
			for dataElement in dataElementSet: #for each <td> tag for manager..
				# managerInfo.append(dataElement.findAll(text=True))
				Data = dataElement.findAll(text=True)
				for data in Data:
					if ('000' in data) or ('nb 1' in data):
						Data.remove(data)
				managerInfo.append(Data)

			if len(managerInfo) > 0:
				self.managerSet.append(managerInfo)

		#Testing
		print self.headerSet

		for manager in self.managerSet:
			print manager


	def writeData (self):
		"Writes Data into .csv"

		print "\nType Desired Outfile Name (include .csv): "
		outfile_name = "chelseamanagersALT.csv" #make a raw-input
		print "Outfile Name: " + outfile_name + '\n'
		outfile = open(outfile_name, "w")

		#Make it so that the number of %s is variable, depending on length of tuple.
		#Maybe avoid string interpolation altogether?

		try:
			outfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s\n' % self.headerSet)
			print "Successfully Wrote Header Information"
		except Exception:
			print "Error in Writing Headers"

		for manager in self.managerSet:
			try:
				outfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s\n' % manager)
				print "Successfully Wrote Manager Information for " + manager[0]
			except Exception:
				print "Error in Writing Manager Information for " + manager[0]

		#Closing
		outfile.close()
		print "\n" + "Script Complete!"


#----------
#EXECUTION
#----------
url_input = "https://en.wikipedia.org/wiki/List_of_Manchester_City_F.C._managers" #will be raw-inputted

Chelsea = DataScraper(url=url_input) #Chelsea is new instance of Data Scraper Class (Instantiation)
Chelsea.runScraper()
#Chelsea.writeData()
