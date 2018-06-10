from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

#launch url
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

# create a new Firefox session
Chromedriver='C:/Users/Sharbani/Downloads/chromedriver.exe'
driver = webdriver.Chrome(Chromedriver)
driver.implicitly_wait(30)
driver.get(url)

#After opening the url above, Selenium clicks the specific agency link
python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click() #click fhsu link

#Selenium hands the page source to Beautiful Soup
soup_level1=BeautifulSoup(driver.page_source, 'lxml')

datalist = [] #empty list
x = 0 #counter

#Beautiful Soup finds all Job Title links on the agency page and the loop begins
for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
    #Selenium visits each Job Title page
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() #click link
    
    #Selenium hands of the source of the specific job page to Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'lxml')

    #Beautiful Soup grabs the HTML table on the page
    table = soup_level2.find_all('table')[0]
    
    #Giving the HTML table to pandas to put in a dataframe object
    df = pd.read_html(str(table),header=0)
    
    #Store the dataframe in a list
    datalist.append(df[0])
    
    #Ask Selenium to click the back button
    driver.execute_script("window.history.go(-1)") 
    
    #increment the counter variable before starting the loop over
    x += 1
    
    #end loop block
    
#loop has completed

#end the Selenium browser session
driver.quit()

#combine all pandas dataframes in the list into one big dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

#convert the pandas dataframe to JSON
json_records = result.to_json(orient='records')

#get current working directory
path = os.getcwd()

#open, write, and close the file
f = open(path + "\\fhsu_payroll_data.json","w") #FHSU
f.write(json_records)
f.close()

# ----------------------------------------- POST to API ----------------------------------------------

def PostJsonFhsu():
    # Writing this code in Try Catch, so that any network or code discrepancy is handled
    try:
        with open('C:Users/Sharbani/Desktop/fhsu_payroll_data.json') as json_file:
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
PostJsonFhsu()

#END OF File