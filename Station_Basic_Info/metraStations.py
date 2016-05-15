'''
Retriving Rail Station Basic Information Data From RTAMS 
Input : http://www.rtams.org/rtams/metraStations.jsp
Output : metraStations_withID.csv
Author :Qili Sui, Xiaochen Chen

May 15th 2016
Version 1.0
'''
#importing libraries and packages
import csv
import urllib
import re
from bs4 import BeautifulSoup
import pandas as pd
import re
import string

def get_table(url = "http://www.rtams.org/rtams/metraStations.jsp"):
	#retriving the whole website
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html,"lxml")

	#retriving the table we want which has a class called
	#outline({'class':'outline'}).
	outline = soup.find('table',{'class':'outline'})
	#retriving the body of the table
	trs = outline.find('tbody').findAll('tr')

	#save data in the table
	data = []

	#iterate through each row
	for tr in trs:

		#In each row, iterate through each cell
		tds = tr.findAll('td')
		#save each cell in each row, append id to the beigining
		data.append([tds[0].text.strip(string.whitespace).replace(u'\xa0', u''),tds[1].text.strip(string.whitespace).replace(u'\xa0', u''),tds[2].text.strip(string.whitespace).replace(u'\xa0', u''),tds[3].text.strip(string.whitespace).replace(u'\xa0', u''),tds[4].text.strip(string.whitespace).replace(u'\xa0', u''),tds[5].text.strip(string.whitespace).replace(u'\xa0', u'')])
	return data


def write_table(data):
	#create the header of the csv table
	columns = 'Station Name, Address, Branches,Farezone,Milepost,Parking Capacity'.split(',')

	#writing the data to metraStations_withID.csv
	with open('metraStations.csv','w') as myfile:
		writer = csv.writer(myfile)
		writer.writerow(columns)
		#for each list(row = data of each row) in data[],iteratively write them into csv
		for row in data:
			writer.writerow(row)


write_table(get_table())


