# urllib, urllib.request and Beautiful Soup are the three important libraries needed in this script
# This Script only captures data from Webiron web page only. For different URL data,
# one will have to change the URL passed in make_soup() and make slight changes to code
# This script captures data with respect to current date and appends it to an exiting csv
# This code runs fine to its purpose.
# Every thing in this script executes in a procedural way

import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from dateutil import parser

# This is a function which takes whatever url is passed from the code or UI
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

# Here's where we capture the html page
soup = make_soup("http://www.webiron.com/abuse_feed/")

def foo():
    # Assigning null value is necessary otherwise garbage value may exist while running the program
    global abusedatasaved
    abusedatasaved = ""
    for record in soup.findAll('tr'):
        abusedata = ""
        for data in record.findAll('td'):
            for dateComparer in record.findAll('td')[1:2]: # Here we're catching hold of date field in loop
                if datetime.datetime.now().date() == parser.parse(dateComparer.text).date():
                    temptext = ''  # To store text data inside the td tag
                    modtext = ''   # To remove comma in text data, as it will be further stored in a csv
                    temptext += data.text
                    modtext += temptext.replace(',', '/')
                    abusedata = abusedata + "," + modtext.strip() # Stripping two ends whitespace; if present
                else:
                    return
                    #print("Hey, there's no new data out there :P")
        abusedatasaved =abusedatasaved + "\n" + abusedata[1:] #The [1:] will loop through 1st column and next ones

# Calling the function foo()
foo()

#print(abusedatasaved)

def WriteToFile():
    header = "Log_Entry_Type, Log_Time, Attacker_IP, Entry_Emails, Log_Message, Deliverable, Days_Unresolved, Incident_Reported"
    filepath = "/home/sawant/AbuseDataFeed.csv"
    file = open(filepath, "wb")
    file.write(bytes(header, encoding="ascii", errors='ignore')) #ensures data is written in bytes, and then encoded
    file.write(bytes(abusedatasaved, encoding="ascii", errors='ignore'))
    file.close()

#calling the file writing function now
WriteToFile()


