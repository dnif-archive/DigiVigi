import urllib2
import requests
import json
import csv

url = "http://haveibeenpwned.com/api/v2/breaches"
urlForPostJsonData = "http://192.168.0.29:9234/json/receive"

r = requests.get(url,verify = False) 

json_data = r.content # Content of response

headers = {'content-type':'application/json'}

json_parsed = json.loads(json_data)
csvout = csv.writer(open("mydata.csv", "wb+"))

csvout.writerow(("Title", "Name","Domain","BreachDate","AddedDate","ModifiedDate","PwnCount","Description","IsVerified","IsFabricated","IsSensitive","IsActive","IsRetired","IsSpamList","LogoType",
                "DataClasses"))

for i in range(len(json_parsed)):
	strTitle = json_parsed[i]['Title'].encode('ascii', 'ignore').decode('ascii')
	strName = json_parsed[i]['Name'].encode('ascii', 'ignore').decode('ascii')
	strDomain = json_parsed[i]['Domain'].encode('ascii', 'ignore').decode('ascii')
	strBreachDate = json_parsed[i]['BreachDate'].encode('ascii', 'ignore').decode('ascii')
	strAddedDate = json_parsed[i]['AddedDate'].encode('ascii', 'ignore').decode('ascii')
	strModifiedDate = json_parsed[i]['ModifiedDate'].encode('ascii', 'ignore').decode('ascii')
	strPwnCount = json_parsed[i]['PwnCount']
	strDescription = json_parsed[i]['Description'].encode('ascii', 'ignore').decode('ascii')
	IsVerified = json_parsed[i]['IsVerified']
	IsFabricated = json_parsed[i]['IsFabricated']
	IsSensitive = json_parsed[i]['IsSensitive']
	IsActive = json_parsed[i]['IsActive']
	IsRetired = json_parsed[i]['IsRetired']
	IsSpamList = json_parsed[i]['IsSpamList']
	LogoType = json_parsed[i]['LogoType'].encode('ascii', 'ignore').decode('ascii')
	strDataAccess = json_parsed[i]['DataClasses']
	#print(json_parsed[i]['IsVerified'])

	csvout.writerow((strTitle, strName,strDomain,strBreachDate,strAddedDate,strModifiedDate,strPwnCount,strDescription,IsVerified,IsFabricated,IsSensitive,IsActive,IsRetired,IsSpamList,LogoType,strDataAccess))

r1 = requests.post(urlForPostJsonData,json.dumps(json_data),header)

response = r1.content

print(response)

