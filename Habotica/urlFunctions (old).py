# TODO add description of this script

# Imports
import urllib
import urllib2
import json
import ast

def getUrl(url, user = {}):
	"""
	Make an api call with a get method, given a user id and api key to put in the header. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	Returns a response code from Habitica's servers. 
	"""
	request = urllib2.Request(url, headers = user)
	contents = json.load(urllib2.urlopen(request))
	return(contents)

def postUrl(url, user = {}, payload = {}):
	"""
	Make an api call with a post method, given a payload to put in the data, a user id, and api key to put in the headers.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	payload: a dictionary of data to send to the server. By default, it's blank.
	Returns a response code from Habitica's servers. 
	"""
	
	# make a string with the request type in it:
	method = "POST"
	# create a handler. you can specify different handlers here (file uploads etc)
	# but we go for the default
	handler = urllib2.HTTPHandler()
	# create an opener director instance
	opener = urllib2.build_opener(handler)
	# build a request
	data = urllib.urlencode(payload)
	request = urllib2.Request(url, data=data, headers = user)
	# overload the get method function with a small anonymous function...
	request.get_method = lambda: method
	# try it; don't forget to catch the result
	try:
	    connection = opener.open(request)
	    return(connection.read())
	except urllib2.HTTPError,e:
	    connection = e
	    return(connection.read())

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)

def putUrl(url, user = {}, payload = {}):
	"""
	Make an api call with a put method, given a payload to put in the data, a user id, and api key to put in the headers.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	payload: a dictionary of data to send to the server. By default, it's blank.
	Returns a response code from Habitica's servers. 
	"""
	#response = requests.put(url, headers = user, data = payload)
	# response = urllib2.urlopen(url, headers = user, data=payload).read()
	# return(response)
		# make a string with the request type in it:
	method = "PUT"
	# create a handler. you can specify different handlers here (file uploads etc)
	# but we go for the default
	handler = urllib2.HTTPHandler()
	# create an opener director instance
	opener = urllib2.build_opener(handler)
	# build a request
	data = urllib.urlencode(payload)
	request = urllib2.Request(url, data=data, headers = user)
	# overload the get method function with a small anonymous function...
	request.get_method = lambda: method
	# try it; don't forget to catch the result
	try:
	    connection = opener.open(request)
	    return(connection.read())
	except urllib2.HTTPError,e:
	    connection = e
	    return(connection.read())

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)

def deleteUrl(url, user = {}, payload = {}):
	"""
	Make an api call with a put method, given a payload to put in the data, a user id, and api key to put in the headers.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
		user can be an empty dictionary if no headers are necessary
	url: any valid url
	payload: a dictionary of data to send to the server. By default, it's blank.
	Returns a response code from Habitica's servers. 
	"""
	#response = requests.put(url, headers = user, data = payload)
	# response = urllib2.urlopen(url, headers = user, data=payload).read()
	# return(response)
		# make a string with the request type in it:
	method = "DELETE"
	# create a handler. you can specify different handlers here (file uploads etc)
	# but we go for the default
	handler = urllib2.HTTPHandler()
	# create an opener director instance
	opener = urllib2.build_opener(handler)
	# build a request
	data = urllib.urlencode(payload)
	request = urllib2.Request(url, data=data, headers = user)
	# overload the get method function with a small anonymous function...
	request.get_method = lambda: method
	# try it; don't forget to catch the result
	try:
	    connection = opener.open(request)
	    return(connection.read())
	except urllib2.HTTPError,e:
	    connection = e
	    return(connection.read())

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)