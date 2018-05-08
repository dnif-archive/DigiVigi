# urllib, urllib.request and Beautiful Soup are the three important libraries needed in this script
# This Script only captures data from Webiron web page only. One will have to change the URL
# After capturing, it only stores that data in a csv file for one time only
# This script does not capture data in paged table
# This script does not append data, one will have to modify the script to capture new or previously exiting data to
# to append it to existing csv file
# This code runs fine to its purpose.

import urllib
import urllib.request
from bs4 import BeautifulSoup

#this is a function which takes whatever url is pass from the code or UI
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

#Here's where you have captured the html page
soup = make_soup("http://www.webiron.com/abuse_feed/")

#Assigning null value is necessary otherwise garbage value may exist while running the program
abusedatasaved = ""

for record in soup.findAll('tr'):
    abusedata= ""
    for data in record.findAll('td'):
        temptext = '' #Using this variable to store text data in td tag
        modtext = ''  #Using this variable to remove comma in text data, as it will be further stored in a csv
        temptext += data.text
        modtext += temptext.replace(',', '/')
        abusedata = abusedata + "," + modtext
    abusedatasaved = abusedatasaved + "\n" + abusedata[1:] #The [1:] will loop through 1st column and next ones

#print(abusedatasaved)
filepath = "D:\codegen\Abusedata.csv"
file = open(filepath, 'a')
file.write(abusedatasaved)
file.close()