# THIS SCRIPT IS WRITTEN TO SUPPORT PROCESS 2 OF THIS PROJECT

import csv
import json

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
