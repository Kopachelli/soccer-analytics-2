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
		managerTable = soup.find_all(class_="wikitable")[0]

		for th in managerTable.find_all("th"): #iterate through headers of table, storing text in <th> tags
			if "Name" in th:
				nameHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(nameHeader)
			if "From" in th:
				fromHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(fromHeader)
			if "To" in th:
				toHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(toHeader)
			if ("M" in th) or ("Matches") in th:
				matchesHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(matchesHeader)
			if ("W" in th) or ("Won" in th) or ("Wins" in th) or ("Wins" in th):
				winsHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(winsHeader)
			if ("D" in th) or ("Drawn" in th) or ("Draws" in th) or ("Draw" in th):
				drawsHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(drawsHeader)
			if ("L" in th) or ("Loss" in th) or ("Lost" in th) or ("Losses" in th):
				lossesHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(lossesHeader)
			if ("F" in th) or ("GF" in th):
				goalsForHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(goalsForHeader)
			if ("A" in th) or ("GA" in th):
				goalsAgainstHeader = th.find(text=True).encode('utf-8')
				self.headerSet.append(goalsAgainstHeader)

		#Convert to Tuple-Type; Makes String Interpolation Easier
		self.headerSet = tuple(self.headerSet)

		#Scraping Individual Manager Data Tuples, Storing Tuples in List
		for tr in managerTable.find_all("tr"): #iterate through each row in table element
			dataElement = tr.findAll("td") #for each row(manager), store all <td> tags in a dataElement var
			if len(dataElement) > 0: #ignore rows with no data, obviously
				#pick out specific <td> tags using indexing, store content as variables
				managerName = dataElement[1].find(string=True).encode('utf-8')
				managerStart = dataElement[3].find(string=True).encode('utf-8')
				managerEnd = dataElement[4].find(string=True).encode('utf-8')
				managerMatches = dataElement[5].find(string=True).encode('utf-8')
				managerWins = dataElement[6].find(string=True).encode('utf-8')
				managerDraws = dataElement[7].find(string=True).encode('utf-8')
				managerLosses= dataElement[8].find(string=True).encode('utf-8')
				managerGoalsFor = dataElement[9].find(string=True).encode('utf-8')
				managerGoalsAgainst = dataElement[10].find(string=True).encode('utf-8')

				#storing all manager information in tuple
				managerInfo = (managerName, managerStart, managerEnd, managerMatches, managerWins, managerDraws, managerLosses, managerGoalsFor, managerGoalsAgainst)
				
				#appending individual manager info to set (list)
				self.managerSet.append(managerInfo)

		print self.headerSet

		print self.managerSet


	def writeData (self):
		"Writes Data into .csv"

		print "\nType Desired Outfile Name (include .csv): "
		outfile_name = "chelseamanagers.csv" #make a raw-input
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
url_input = "https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._managers" #will be raw-inputted

Chelsea = DataScraper(url=url_input) #Chelsea is new instance of Data Scraper Class (Instantiation)
Chelsea.runScraper()
Chelsea.writeData()
