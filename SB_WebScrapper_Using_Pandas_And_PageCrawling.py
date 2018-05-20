import requests
from bs4 import BeautifulSoup
import csv
import json
import pandas

#Get the first page to extract page numbers
r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

#We are trying to get the last tag with "class"="Page"
page_nr=soup.find_all("a",{"class":"Page"})[-1].text
print(page_nr,"number of pages were found")

#We are taking an empty list first
l=[]
#The end part of the url specifies the page no.
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
#Go to first three- four pages and see how this number at the end part of the url changes and try to figure out the pattern. Below there is 
#iteration over the page numbers. This logic is according the pattern found for this website.
for page in range(0,int(page_nr)*10,10):
    print( )
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    #c=r.json()["list"]
    #We are extracting the data according to the class tags. We are adding them as dictionary elements.
    soup=BeautifulSoup(c,"html.parser")
    #In the html code the details of each property starts with a "class"="PropertyRow". In that there are different classes for each item.
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class","propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class","propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        d["Price"]=item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Beds"]=item.find("span",{"class","infoBed"}).find("b").text
        except:
            d["Beds"]=None
    
        try:
            d["Area"]=item.find("span",{"class","infoSqFt"}).find("b").text
        except:
            d["Area"]=None
    
        try:
            d["Full Baths"]=item.find("span",{"class","infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class","infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None
        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text
        l.append(d)

# Here we iterate over the all the "Class"="PropertyRow"s which are there for each property.In one iteration one dictionary is generated 
#with all the details of one property.For each propery one dictionary is generated. We get a list of dictionaries.

#We save the list in Pandas dataframe.
df=pandas.DataFrame(l)

#Then we import the elements of the pandas dataframe in a csv file.
df.to_csv("Output.csv")

#-------------------Code to convert csv to json---------------------------------------------------------------------------------------
csvfile = open('Output.csv', 'r')
jsonfile = open('Output.json', 'w')
fieldnames = ("Sl_No","Adress","Area","Beds","Full_Baths","Half_Baths","Locality","Lot_Size","Price","LogEvent","EvtLen")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)