#In: URL
#Out: CSV of Manager Information

#Print Header
print "Manager History - Data Mining Script"
print " "

print "Professor Eric Schwartz"
print "Naman Gupta"
print " "
print "-----------------------------------------------"
print "Data Sourced from MyFootballFacts"
print "-----------------------------------------------"
print " "

#Import Necessary Modules & Libraries
import requests
import string
import re
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from datetime import datetime

def scraper(url):

	res = requests.get(url)
	res_content = res.content
	soup = BeautifulSoup(res_content, "html.parser")
	managerTableData = soup.find("table").findAll("tr")


	managers = []

	for tr in managerTableData:
		data = tr.findAll("td")
		if len(data) > 3:
			if data[1]:
				managerName = data[1].text
			if data[2]:
				managerNationality = data[3].text
			if data[3]:
				managerClub = data[4].text
			if data[4]:
				managerFrom = data[5].text
			if data[5]:
				managerUntil = data[6].text

		managerTup = (managerName.encode('utf-8').replace("\r\n","").replace("\xc2\xa0","").replace("  ", " "), 
			managerNationality.encode('utf-8').replace("\r\n","").replace("\xc2\xa0","").replace("  ", " "), 
			managerClub.encode('utf-8').replace("\r\n","").replace("\xc2\xa0","").replace("  ", " "), 
			managerFrom.encode('utf-8').replace("\r\n","").replace("\xc2\xa0","").replace("  ", " "), 
			managerUntil.encode('utf-8').replace("\r\n","").replace("\xc2\xa0","").replace("  ", " "))

		managers.append(managerTup)

	print managers[4:-2]

	#Writing Data
	print "Type Desired Outfile Name (include .csv): "
	outfile_name = "eplmanagerduration.csv" #make a raw-input
	print "Outfile Name: " + outfile_name + '\n'
	outfile = open(outfile_name, "w")

	for manager in managers[4:-2]:
		try:
			outfile.write('%s, %s, %s, %s, %s\n' % manager)
			print "Successfully Wrote Manager Information for " + manager[0]
		except Exception:
			print "Error in Writing Manager Information"

	#Closing
	outfile.close()
	print "\n" + "Script Complete!"

scraper(url = "http://www.myfootballfacts.com/MANAGERS_20.12.15.htm")