# TODO add description of this script

# Imports
import json
import urllib3
import certifi
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())


def getUrl(url, user = {}):
	"""
	Make an api call with a GET method, given a user id and api key to put in the header. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	Returns a loaded json object from Habitica's servers. 
	"""
	request = http.request('GET', url, headers=user)
	data = json.loads(request.data)
	return(data)

def deleteUrl(url, user = {}):
	"""
	Make an api call with a DELETE method, given a user id and api key to put in the header. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	Returns a loaded json object from Habitica's servers. 
	"""
	request = http.request('DELETE', url, headers=user)
	data = json.loads(request.data)
	return(data)

def postUrl(url, user = {}, payload = {}):
	"""
	Make an api call with a POST method, given a user id and api key to put in the header. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	Returns a loaded json object from Habitica's servers. 
	"""
	user['Content-Type'] = 'application/json'
	encoded_data = json.dumps(payload)
	request = http.request('POST', url, headers=user, body=encoded_data)
	data = json.loads(request.data)
	return(data)

def putUrl(url, user = {}, payload = {}):
	"""
	Make an api call with a PUT method, given a user id and api key to put in the header. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	Returns a loaded json object from Habitica's servers. 
	"""
	user['Content-Type'] = 'application/json'
	encoded_data = json.dumps(payload)
	request = http.request('PUT', url, headers=user, body=encoded_data)
	data = json.loads(request.data)
	return(data)