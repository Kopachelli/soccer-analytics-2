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
import csv

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
		if len(soup.find(class_="wikitable").find_all("tr")) > 12:
			managerTable = soup.find(class_="wikitable")
		else:
			managerTable = soup.find_all(class_="wikitable")[1]

		#Iterate through headers of the table, storing the text in the <th> tags.
		for th in managerTable.find_all("th"):
			self.headerSet.append(str(th.find(text=True)))

		self.headerSet = tuple(self.headerSet)

		#Scraping Individual Manager Data Rows
		for tr in managerTable.find_all("tr"): #iterate through each row in table element
			dataElementSet = tr.findAll("td") #gives set of table data for each table row
			managerInfo = [] #Initialize List which will capture each manager's data
			for dataElement in dataElementSet: #for each <td> tag for manager..
				Data = dataElement.findAll(text=True) #find all text in the tag
				for data in Data:
					if ('000' in data) or ('nb 1' in data): #keep the text that looks like English..
						Data.remove(data)

					data = data.encode('utf-8')

				managerInfo.append(Data)

			if len(managerInfo) > 0:
				self.managerSet.append(tuple(managerInfo))


	def writeData (self):
		"Writes Data into .csv"

		outfile_name = teamName + "managers.csv"
		print "Outfile Name: " + outfile_name
		outfile = open(outfile_name, "wb")

		mywriter = csv.writer(outfile)

		try:
			mywriter.writerow(self.headerSet)
			#print "Successfully Wrote Header Information"
		except Exception:
			pass

		for manager in self.managerSet:
			try:
				mywriter.writerow(manager)
				#print "Successfully Wrote Manager Information for "
			except Exception:
				pass
				#print "Error in Writing Manager Information for "

		#Closing
		outfile.close()
		print "Script Complete for " + teamName + "\n"


#----------
#EXECUTION
#----------

url_set = {"Arsenal":"https://en.wikipedia.org/wiki/List_of_Arsenal_F.C._managers",
			"AstonVilla":"https://en.wikipedia.org/wiki/List_of_Aston_Villa_F.C._managers",
			"Bournemouth":"https://en.wikipedia.org/w/index.php?title=List_of_A.F.C._Bournemouth_managers&action=edit&redlink=1",
			"Chelsea":"https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._managers",
			"CrystalPalace":"https://en.wikipedia.org/wiki/List_of_Crystal_Palace_F.C._managers",
			"LeicesterCity":"https://en.wikipedia.org/wiki/List_of_Leicester_City_F.C._managers",
			"Liverpool":"https://en.wikipedia.org/wiki/List_of_Liverpool_F.C._managers",
			"ManchesterCity":"https://en.wikipedia.org/wiki/List_of_Manchester_City_F.C._managers",
			"ManchesterUnited":"https://en.wikipedia.org/wiki/List_of_Manchester_United_F.C._managers",
			"NewcastleUnited":"https://en.wikipedia.org/wiki/List_of_Newcastle_United_F.C._managers",
			"NorwichCity":"https://en.wikipedia.org/wiki/List_of_Norwich_City_F.C._managers",
			"Southampton":"https://en.wikipedia.org/wiki/List_of_Southampton_F.C._managers",
			"StokeCity":"https://en.wikipedia.org/wiki/List_of_Stoke_City_F.C._managers",
			"Sunderland":"https://en.wikipedia.org/wiki/List_of_Sunderland_A.F.C._managers",
			"SwanseaCity":"https://en.wikipedia.org/wiki/List_of_Swansea_City_A.F.C._managers",
			"Tottenham":"https://en.wikipedia.org/wiki/List_of_Tottenham_Hotspur_F.C._managers",
			"Watford":"https://en.wikipedia.org/wiki/List_of_Watford_F.C._managers",
			"WestBrom":"https://en.wikipedia.org/wiki/List_of_West_Bromwich_Albion_F.C._managers",
			"WestHam":"https://en.wikipedia.org/wiki/West_Ham_United_F.C._managers"}


for team in url_set.keys():

	try:
		teamName = str(team)
		team = DataScraper(url_set[team])
		team.runScraper()
		team.writeData()
		
	except Exception:
		print "Failed for Team: " + teamName + "\n"