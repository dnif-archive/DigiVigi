# ------------------------------------- Initial Comments --------------------------------------------

# THIS SCRIPT IS WRITTEN TO SUPPORT PROCESS 2 OF THIS PROJECT
# urllib, urllib.request and Beautiful Soup are the three important libraries needed in this script
# This Script only captures data from Webiron web page only. For different URL data,
# one will have to change the URL passed in make_soup() and make slight changes to code
# This script captures data with respect to current date and appends it to an exiting csv
# This code runs fine to its purpose.
# Every thing in this script executes in a procedural way

# ------------------------------------------ Imports -------------------------------------------------

import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
from dateutil import parser
import csv
import json
import requests


# ------------------------------------- Daily Data Fetch ---------------------------------------------

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

def WriteToFile():
    header = "Log_Entry_Type,Log_Time,Attacker_IP,Entry_Emails,Log_Message,Deliverable,Days_Unresolved,Incident_Reported"
    filepath = "/home/sawant/AbuseDataFeed.csv"
    file = open(filepath, "wb")
    file.write(bytes(header, encoding="ascii", errors='ignore')) #ensures data is written in bytes, and then encoded
    file.write(bytes(abusedatasaved, encoding="ascii", errors='ignore'))
    file.close()

#calling the file writing function now
WriteToFile()

# ----------------------------------------- CSV to JSON ----------------------------------------------

# object to read csv file data
csvfile = open('/home/sawant/AbuseDataFeed.csv', 'r')

# object to write data to json file
jsonfile = open('/home/sawant/AbuseFeed.json', 'w')

# Fieldnames are not needed if your csv file already has field names defined
# fieldnames = ("$Entry_Type", "$Log_Time", "$Attacker_Ip", "$Entry_Emails", "$Log_Message", "$Deliverable",
              #"$Days_Unresolved", "$Incidents_Reported", "$LogEvent", "$EvtLen")

def WriteToJsonFile():
    reader = csv.DictReader(csvfile)
    # json.dumps is a function from library that already has for loop logic written for returning row for row
    out = json.dumps([row for row in reader])
    #print(out) For testing purpose
    jsonfile.write(out)

# function call
WriteToJsonFile()

# ----------------------------------------- POST to API ----------------------------------------------

def PostJsonAbuse():
    # Writing this code in Try Catch, so that any network or code discrepancy is handled
    try:
        with open('/home/sawant/AbuseFeed.json') as json_file:
            # Important to set your variable with proper null value. Or else it might already have garbage data in it
            data = ""
            # No json.dumps here. It will encode double times if done so. So we're just gonna load from the file
            # Json.dumps is already done when converting csv to json
            # If one does json.dumps again, it will not throw an error, but data might not reach the API or the API might
            # discard it. The API will log in following in its log - Unicode object does not support item assignment
            # This is not a fact. But one or more can test it out just to be sure and this comments could be updated.
            data = json.load(json_file)

            # headers = {'content-type': 'application/json', 'Accept': 'text/plain'}
            url ="http://yourIP:9234/json/receive"

            # r = requests.post(url, data=None, json={'json_payload': json_data}, verify=False)
            # Request library takes care of the rest of the POST format (i.e headers and all)
            r = requests.post(url, data=None, json=data)

            # Just to be sure. Expected Response Code: 200 OK
            print(r.status_code)
            # print(data)

# Exceptions written to capture discrepancies
    except requests.exceptions.Timeout as ct:
        print(ct)
    except requests.exceptions.TooManyRedirects as tmr:
        print(tmr)
    except requests.exceptions.RequestException as e:
        print(e)

# function call
PostJsonAbuse()

#END OF File
