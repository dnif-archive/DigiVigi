import urllib2
import requests
import json
import csv
import json_utils

urlForGetJsonData = "http://54.190.62.177:3011/getAccessLog" ##it is the access log URL where we get the access log in JSON format
urlForPostJsonData = "http://192.168.0.29:9234/json/receive" ## it is the service used to post data on dnif platform

headers = {'content-type':'application/json'}

r1 = requests.get(urlForGetJsonData,verify = False) 

json_data = r1.content # Content of response

#json_parsed = [{"res":{"statusCode":200},"req":{"url":"/login","headers":{"accept":"application/json","content-type":"application/json","host":"54.190.62.177:3011","content-length":"69","connection":"close"},"method":"POST","httpVersion":"1.1","originalUrl":"/login","query":{},"body":{"userType":"admin","userName":"admin","password":"admin","email":""}},"responseTime":1,"level":"info","message":"POST /login 200 1ms","timestamp":"2018-06-02T01:58:56.470Z"},{"res":{"statusCode":200},"req":{"url":"/login","headers":{"accept":"application/json","content-type":"application/json","host":"54.190.62.177:3011","content-length":"69","connection":"close"},"method":"POST","httpVersion":"1.1","originalUrl":"/login","query":{},"body":{"userType":"admin","userName":"admin","password":"admin","email":""}},"responseTime":1,"level":"info","message":"POST /login 200 1ms","timestamp":"2018-06-02T07:34:12.751Z"},{"res":{"statusCode":200},"req":{"url":"/getEmployees","headers":{"host":"54.190.62.177:3011","connection":"keep-alive","content-length":"6","accept":"*/*","origin":"http://54.190.62.177:3010","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"http://54.190.62.177:3010/employees","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"},"method":"POST","httpVersion":"1.1","originalUrl":"/getEmployees","query":{},"body":{"page":"1"}},"responseTime":1,"level":"info","message":"POST /getEmployees 200 1ms","timestamp":"2018-06-02T07:34:33.691Z"},{"res":{"statusCode":404},"req":{"url":"/images/Employees/1527086290908-Photo0584.jpg","headers":{"host":"54.190.62.177:3011","connection":"keep-alive","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","accept":"image/webp,image/apng,image/*,*/*;q=0.8","referer":"http://54.190.62.177:3010/employees","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8","cookie":"session=Jh7LlBxiuag4_RcerQKD1g.q864o-K_t0WWSOTgIPstvWGMLAKCaOnLfnBZNkq2MB3dHEuudM09TNunJBWv_mkY33myqDgV-aDjv25-zhhegheRWNasuhcapOTQRvfBH4aKQ7xm5cxAUcXsgVzW6kaTfGLp4M8bZODymOawPo0sPKJlhvUH7H-xDjSitZtzZr8.1527924852750.1800000.BEEAgRVLJ5LZRswCvzm_IsflkFLPUN0ZmGpjWSF69yY"},"method":"GET","httpVersion":"1.1","originalUrl":"/images/Employees/1527086290908-Photo0584.jpg","query":{}},"responseTime":1,"level":"info","message":"GET /images/Employees/1527086290908-Photo0584.jpg 404 1ms","timestamp":"2018-06-02T07:36:53.165Z"},{"res":{"statusCode":200},"req":{"url":"/getRequestedLeaves","headers":{"host":"54.190.62.177:3011","connection":"keep-alive","content-length":"6","accept":"*/*","origin":"http://54.190.62.177:3010","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36","content-type":"application/x-www-form-urlencoded; charset=UTF-8","referer":"http://54.190.62.177:3010/leaves","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"},"method":"POST","httpVersion":"1.1","originalUrl":"/getRequestedLeaves","query":{},"body":{"page":"1"}},"responseTime":1,"level":"info","message":"POST /getRequestedLeaves 200 1ms","timestamp":"2018-06-02T07:37:00.012Z"}]
json_parsed = json.loads(json_data)

print(str(json_parsed))

data = {}
postArray = []

for x in range(len(json_parsed)):
	if 'statusCode' in json_parsed[x]['res']:	
		#print("statusCode is there: ")
		#print("statusCode \n\n",json_parsed[x]['res']['statusCode'])
		data['statusCode'] = json_parsed[x]['res']['statusCode']

	if 'url' in json_parsed[x]['req']:	
		#print("url is there: ")
		#print("url \n\n",json_parsed[x]['req']['url'])
		data['url'] = json_parsed[x]['req']['url']

	if 'accept' in json_parsed[x]['req']['headers']:
		#print("accept is there:")
		#print("accept \n\n",str(json_parsed[x]['req']['headers']['accept']))
		data['accept'] = json_parsed[x]['req']['headers']['accept']

	if 'content-type' in json_parsed[x]['req']['headers']:
		#print("content-type is there: ")
		#print("content-type \n\n",str(json_parsed[x]['req']['headers']['content-type']))
		data['content-type'] = json_parsed[x]['req']['headers']['content-type']

	if 'host' in json_parsed[x]['req']['headers']:
		#print("host is there: ")
		#print("host \n\n",json_parsed[x]['req']['headers']['host'])
		data['host'] = json_parsed[x]['req']['headers']['host']

	if 'content-length' in json_parsed[x]['req']['headers']:
		#print("content-type is there: ")
		#print("content-length \n\n",str(json_parsed[x]['req']['headers']))
		data['content-length'] = json_parsed[x]['req']['headers']['content-length']

	if 'connection' in json_parsed[x]['req']['headers']:
		#print("connection is there: ")
		#print("connection \n\n",str(json_parsed[x]['req']['headers']['connection']))
		data['connection'] = json_parsed[x]['req']['headers']['connection']

	if 'method' in json_parsed[x]['req']:		
		#print("method is there: ")
		#print("method \n\n",json_parsed[x]['req']['method'])
		data['method'] = json_parsed[x]['req']['method']

	if 'httpVersion' in json_parsed[x]['req']:
		#print("httpVersion is there: ")
		#print("httpVersion \n\n",json_parsed[x]['req']['httpVersion'])
		data['httpVersion'] = json_parsed[x]['req']['httpVersion']

	if 'originalUrl' in json_parsed[x]['req']:
		#print("originalUrl is there: ")
		#print("originalUrl \n\n",json_parsed[x]['req']['originalUrl'])
		data['originalUrl'] = json_parsed[x]['req']['originalUrl']

	if 'query' in json_parsed[x]['req']['headers']:
		#print("query is there: ")
		#print("query \n\n",str(json_parsed[x]['req']['query']))	
		data['query'] = json_parsed[x]['req']['query']

	if 'body' in json_parsed[x]['req']:
		#print("body is there:")
		#print("body \n\n",str(json_parsed[x]['req']['body']))
		data['body'] = json_parsed[x]['req']['body']

	if 'responseTime' in json_parsed[x]:
		#print("responseTime is there:")
	 	#print("responseTime",json_parsed[x]['responseTime'])
	 	data['responseTime'] = json_parsed[x]['responseTime']

	if 'level' in json_parsed[x]:
		#print("level is there: ")
		#print("level \n\n",json_parsed[x]['level'].encode('ascii', 'ignore').decode('ascii'))
		data['level'] = json_parsed[x]['level']

	if 'message' in json_parsed[x]:
		print("message is there: \n")
		#print("message \n\n",json_parsed[x]['message'].encode('ascii', 'ignore').decode('ascii'))
		data['message'] = json_parsed[x]['message']

	if 'timestamp' in json_parsed[x]:
		#print("timestamp is there:")
		#print("timestamp \n\n",json_parsed[x]['timestamp'].encode('ascii', 'ignore').decode('ascii'))
		data['timestamp'] = json_parsed[x]['timestamp']

	if 'referer' in json_parsed[x]['req']['headers']:
		#print("referer is there: ")
		#print("referer \n\n",str(json_parsed[x]['req']['headers']['referer']))
		data['referer'] = json_parsed[x]['req']['headers']['referer']

	if 'accept-encoding' in json_parsed[x]['req']['headers']:
		#print("accept-encoding is there: ")
		#print("accept-encoding \n\n",str(json_parsed[x]['req']['headers']['accept-encoding']))
		data['accept-encoding'] = json_parsed[x]['req']['headers']['accept-encoding']

	if 'accept-language' in json_parsed[x]['req']['headers']:
		#print("accept-language is there: ")
		#print("accept-language \n\n",str(json_parsed[x]['req']['headers']['accept-language']))
		data['accept-language'] = json_parsed[x]['req']['headers']['accept-language']

	if 'cookie' in json_parsed[x]['req']['headers']:
		#print("cookie is there: ")
		#print("cookie \n\n",str(json_parsed[x]['req']['headers']['cookie']))
		data['cookie'] = json_parsed[x]['req']['headers']['cookie']

	json_data_for_post = json.dumps(data)

	print(json_data_for_post)

	postArray.append(json_data_for_post)

postString1 = str(postArray).replace("\\","");

postString2 = postString1.replace("[\"","[")

postString3 = postString2.replace("\"]","]")

postString4 = postString3.replace("'{","{")

postString5 = postString4.replace("\'","")


print(postString5)

#r2 = requests.post(urlForPostJsonData, postString5 = json.dumps(postString5), headers = headers)

#response = r2.content

#print(response)

	