import requests
import json

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