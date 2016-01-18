#In: URL
#Out: CSV of Manager Information

#Print Header
print "Manager History - Data Mining Script"
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


#Defining Date-Difference Function, To Be Called Later

def __datetime(dateStr):
	try:
		return datetime.strptime(dateStr, '%d %B %Y')
	except Exception:
		pass

#Function
def scraper(url):
	"Will Run Data Scraping"

	res = requests.get(url)
	res_content = res.content
	soup = BeautifulSoup(res_content, "html.parser")
	managerTable = soup.find_all(class_="wikitable")[0]


	#Finding Set of Headers, Storing Them for Later Use in Tuple
	headerSet = []

	for th in managerTable.find_all("th"): #iterate through headers of table, storing text in <th> tags
		if "Name" in th:
			nameHeader = th.find(text=True).encode('utf-8')
			headerSet.append(nameHeader)
		if "From" in th:
			fromHeader = th.find(text=True).encode('utf-8')
			headerSet.append(fromHeader)
		if "To" in th:
			toHeader = th.find(text=True).encode('utf-8')
			headerSet.append(toHeader)
		if ("M" in th) or ("Matches") in th:
			matchesHeader = th.find(text=True).encode('utf-8')
			headerSet.append(matchesHeader)
		if ("W" in th) or ("Won" in th) or ("Wins" in th) or ("Wins" in th):
			winsHeader = th.find(text=True).encode('utf-8')
			headerSet.append(winsHeader)
		if ("D" in th) or ("Drawn" in th) or ("Draws" in th) or ("Draw" in th):
			drawsHeader = th.find(text=True).encode('utf-8')
			headerSet.append(drawsHeader)
		if ("L" in th) or ("Loss" in th) or ("Lost" in th) or ("Losses" in th):
			lossesHeader = th.find(text=True).encode('utf-8')
			headerSet.append(lossesHeader)
		if ("F" in th) or ("GF" in th):
			goalsForHeader = th.find(text=True).encode('utf-8')
			headerSet.append(goalsForHeader)
		if ("A" in th) or ("GA" in th):
			goalsAgainstHeader = th.find(text=True).encode('utf-8')
			headerSet.append(goalsAgainstHeader)

	headerSet = tuple(headerSet)

	#Scraping Individual Manager Data Tuples, Storing Tuples in List
	managerSet = []

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
			
			#in the future, we can subtract start and end using this format below..
			managerStart = __datetime(managerStart)
			managerEnd = __datetime(managerEnd)
			#delta = managerStart - managerEnd

			#appending individual manager info to set (list)
			managerSet.append(managerInfo)


	print headerSet

	print managerSet

	#Writing Data
	print "Type Desired Outfile Name (include .csv): "
	outfile_name = "chelseamanagers.csv" #make a raw-input
	print "Outfile Name: " + outfile_name + '\n'
	outfile = open(outfile_name, "w")

	try:
		outfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s\n' % headerSet)
		print "Successfully Wrote Header Information"
	except Exception:
		print "Error in Writing Headers"

	for manager in managerSet:
		try:
			outfile.write('%s, %s, %s, %s, %s, %s, %s, %s, %s\n' % manager)
			print "Successfully Wrote Manager Information for " + manager[0]
		except Exception:
			print "Error in Writing Manager Information"

	#Closing
	outfile.close()
	print "\n" + "Script Complete!"


#----------
#EXECUTION
#----------
url_input = "https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._managers" #will be raw-inputted
scraper(url = url_input)
