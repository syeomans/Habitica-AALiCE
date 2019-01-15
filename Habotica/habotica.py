# TODO add description of this script

# Imports
import urllib
import urllib2
import json
import ast
#import challenge

def getUrl(user, url):
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

def postUrl(user, url, payload = {}):
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

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)

def putUrl(user, url, payload = {}):
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

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)

def deleteUrl(user, url, payload = {}):
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

	# check. Substitute with appropriate HTTP code.
	if connection.code == 200:
	    data = connection.read()
	else:
	    # handle the error case. connection.read() will still contain data
	    # if any was returned, but it probably won't be of any use
	    #print("Something's wrong!!!!!!!!!!!!")
	    data = connection.read()
	    print(data)

def getChat(user, num_messages = 200):
	"""
	Get the last num_messages number of chats. Returns a list of strings containing chat messages.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	num_messages: the number of newest messages to retrieve 
		default value returns all reachable messages
	"""
	url = "https://habitica.com/api/v3/groups/party/chat"
	print("Getting last " + str(num_messages) + " messages.")
	contents = getUrl(user, url)
	outList = []
	for i in range(0,num_messages):
		outList.append(contents['data'][i]['text'])
	return(outList)

def getChatData(user, num_messages = 200):
	"""
	Get the data from the last 200 chats. Returns a list of dictionaries containing chat info.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	num_messages: the number of newest messages to retrieve 
		default value returns all reachable messages
	returned dictionary has these keys: ['uuid', 'timestamp', 'flagCount', 'flags', 'likes', 'text', 'id']
	"""
	url = "https://habitica.com/api/v3/groups/party/chat"
	print("Getting last " + str(num_messages) + " messages.")
	contents = getUrl(user, url)
	
	# If user wants a specific number of messages, put them in a list and return
	if num_messages != 200:
		outList = []
		for i in range(0,num_messages):
			outList.append(contents['data'][i])
	# Else, return all data
	else:
		outList = contents['data']
	return(outList)

def postChat(user, message):
	"""
	Post a message to the party chat. Returns a response code from Habitica's servers. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	message: a string containing the message to post
	"""
	url = "https://habitica.com/api/v3/groups/party/chat"
	payload = {'message': message}
	return(postUrl(user, url, payload))

def getStatus():
	"""Gets the status of Habitica's API."""
	url = "https://habitica.com/api/v3/status"
	return(getUrl({}, url))

def getAPIUp():
	"""Returns True if API is up. False otherwise."""
	contents = getStatus()
	if(contents['data']['status']) == "up":
		return(True)
	else:
		return(False)

def getTask(user, taskId):
	"""
	Get a task given the taskId. Returns a dictionary containing the task's data.
	
	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	taskId: a string containing a task id (obtainable from any function that returns a task dictionary)
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	print("Getting task")
	return(getUrl(user, url)['data'])

def getAllTasks(user):
	"""Get all tasks from user. 

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}

	Returns a list of dictionaries containing information on all the user's tasks.
	The list is structured from oldest to newest.
	The returned dictionaries' structure depends on the type of task. Keys defined below:

	todos keys: attribute, checklist, group, collapseChecklist, tags, text, challenge, userId, value, 
		id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	
	dailys keys: streak, startDate, isDue, attribute, userId, frequency, updatedAt, id, createdAt, 
		daysOfMonth, group, collapseChecklist, priority, text, type, repeat, tags, checklist, completed, 
		nextDue, weeksOfMonth, yesterDaily, challenge, reminders, everyX, value, _id, notes, history
	
	habits keys: attribute, counterUp, group, tags, down, text, challenge, counterDown, userId, up, 
		value, id, priority, frequency, notes, updatedAt, _id, type, reminders, createdAt, history
	
	rewards keys: attribute, group, tags, text, challenge, userId, value, id, priority, notes, updatedAt, 
		_id, type, reminders, createdAt
	
	completedTodos keys: attribute, dateCompleted, checklist, group, collapseChecklist, tags, text, 
		challenge, userId, value, id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	"""
	url = "https://habitica.com/api/v3/tasks/user"
	print("Getting all tasks")
	return(getUrl(user, url)['data'])

def getTasks(user, task_type='todos'):
	"""
	Get all tasks of a given type. Returns a list of dictionaries containing all task info. Defaults to todos.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	task_type: one of ['habits', 'dailys', 'todos', 'rewards', 'completedTodos']

	The returned dictionaries' structure depends on the type of task. Keys defined below:

	todos keys: attribute, checklist, group, collapseChecklist, tags, text, challenge, userId, value, 
		id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	
	dailys keys: streak, startDate, isDue, attribute, userId, frequency, updatedAt, id, createdAt, 
		daysOfMonth, group, collapseChecklist, priority, text, type, repeat, tags, checklist, completed, 
		nextDue, weeksOfMonth, yesterDaily, challenge, reminders, everyX, value, _id, notes, history
	
	habits keys: attribute, counterUp, group, tags, down, text, challenge, counterDown, userId, up, 
		value, id, priority, frequency, notes, updatedAt, _id, type, reminders, createdAt, history
	
	rewards keys: attribute, group, tags, text, challenge, userId, value, id, priority, notes, updatedAt, 
		_id, type, reminders, createdAt
	
	completedTodos keys: attribute, dateCompleted, checklist, group, collapseChecklist, tags, text, 
		challenge, userId, value, id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	"""
	url = "https://habitica.com/api/v3/tasks/user?type=" + task_type
	print("Getting " + task_type)
	return(getUrl(user, url)['data'])

def getTaskDict(user, task_type, term, defn):
	"""
	Returns a dictionary of tasks and attributes of the user's choice. Possible terms and definitions listed below.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	task_type: one of ['habits', 'dailys', 'todos', 'rewards', 'completedTodos']
	term: one of ['text', 'id']. Terms for the returned dictionary.
	defn: one of ['attribute', 'checklist', 'group', 'collapseChecklist', 'tags', 
		'text', 'challenge', 'userId', 'value', 'id', 'priority', 'completed', 'notes', 'updatedAt', 
		'date', '_id', 'type', 'reminders', 'createdAt']
	"""

	# List all valid inputs
	task_type_list = ['habits', 'dailys', 'todos', 'rewards', 'completedTodos']
	term_list = ['text', 'id']
	defn_list = ['attribute', 'checklist', 'group', 'collapseChecklist', 'tags', 'text', 'challenge', 'userId', 'value', 'id', 'priority', 'completed', 'notes', 'updatedAt', 'date', '_id', 'type', 'reminders', 'createdAt']
	
	# Input validation
	if task_type not in task_type_list:
		return(str(task_type) + " is not a valid task type.")
	if term not in term_list:
		return(str(term) + " is not a valid term.")
	if defn not in defn_list:
		return(str(defn) + " is not a valid definition.")

	# Get task list and make dictionary
	contents = getTasks(user, task_type)
	outDict = {}	
	for i in contents:
		outDict[i[term]] = i[defn]
	return(outDict)

def getTags(user, term):
	"""
	Returns a dictionary of the user's tags. Terms are either tag names or ids. Definitions are the other.

	By choosing 'both' for term, this function will return a list of dictionaries containing both names 
		and ids for all the user's tags.
	'user' takes a dictionary formatted as: {'name': 'your_user_id', 'pwd': 'your_api_key'}
	Valid inputs for term: ['name', 'id', 'both']
	"""

	# Get tags. "Contents" will contain a list of dictionaries of all user's tags' data
	url = "https://habitica.com/api/v3/tags"
	print("Getting tag dictionary")
	contents = getUrl(user, url)['data']

	# Whether the user wants names or ids to be terms, choose the other as the definitions.
	if term == 'name':
		defn = 'id'
	elif term == 'id':
		defn = 'name'
	# If user selects both, return the raw output from the Get call	
	elif term == 'both':
		return(contents)

	# Make and return dictionary
	outDict = {}
	for i in contents:
		outDict[i[term]] = i[defn]
	return(outDict)

def getTaskList(user, task_type='todos'):
	"""
	Returns an ordered list of task names.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	task_type: one of ['habits', 'dailies', 'todos', 'rewards', 'completedTodos']
	"""
	contents = getTasks(user, task_type)
	outList = []	
	for i in contents:
		outList.append(i['text']) 
	return(outList)

def getTaskIdList(user, task_type='todos'):
	"""
	Returns an ordered list of task ids.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	task_type: one of ['habits', 'dailies', 'todos', 'rewards', 'completedTodos']
	"""
	contents = getTasks(user, task_type)
	outList = []	
	for i in contents:
		outList.append(i['_id']) 
	return(outList)

# TODO: test this function 
def acceptQuest(user):
	"""
	Accepts a quest invitation.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	"""
	url = "https://habitica.com/api/v3/groups/party/quests/accept"
	# # payload = {'message': message}
	# response = requests.post(url, headers = credentials)
	return(postUrl(user,url))

def moveTask(user, taskId, position):
	"""
	Moves a task to the desired position.

	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/move/to/" + str(position)
	return(postUrl(user,url))

def cron(user):
	"""
	Run user's cron. This will 'check in' the user.
	
	user: a dictionary formatted as: {'x-api-user': 'your_user_id_here', 'x-api-key': 'your_api_key_here'}
	"""
	url = "https://habitica.com/api/v3/cron"
	return(postUrl(user,url))

def sortTasks(user, task_type, sort_type):
	"""
	Sort tasks by any valid task key. Returns a response code from Habitica's servers. 

	task_type: one of ['habits', 'dailies', 'todos', 'rewards', 'completedTodos']
	sort_type: any valid task key. Some keys are more useful than others. Some keys outright fail.
		sort_type "tagalpha" will sort alphabetically by tag for any task_type
		(sorting by tag alone is useless and often fails)

	todos keys: attribute, checklist, group, collapseChecklist, tags, text, challenge, userId, value, 
		id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	
	dailys keys: streak, startDate, isDue, attribute, userId, frequency, updatedAt, id, createdAt, 
		daysOfMonth, group, collapseChecklist, priority, text, type, repeat, tags, checklist, completed, 
		nextDue, weeksOfMonth, yesterDaily, challenge, reminders, everyX, value, _id, notes, history
	
	habits keys: attribute, counterUp, group, tags, down, text, challenge, counterDown, userId, up, 
		value, id, priority, frequency, notes, updatedAt, _id, type, reminders, createdAt, history
	
	rewards keys: attribute, group, tags, text, challenge, userId, value, id, priority, notes, updatedAt, 
		_id, type, reminders, createdAt
	
	completedTodos keys: attribute, dateCompleted, checklist, group, collapseChecklist, tags, text, 
		challenge, userId, value, id, priority, completed, notes, updatedAt, _id, type, reminders, createdAt
	"""
	tasks = getTasks(user, task_type)

	# if sort_type is "taskalpha", sort by tags alphabetically
	if sort_type == "tagalpha":
		# Get a dictionary of tag ids as terms and ids as defs
		tagDict = getTags(user, 'id')

		# Set alpha, a new key which holds a single string to sort by
		for i in tasks:
			# If there are no tags, tag by setting alpha to "~"
			if i['tags'] == []:
				alpha = "~"
			# Else, set alpha to the first tag alphabetically
			else:
				# Turn list of tag ids into tag names
				tagList = i['tags']
				for j in range(0, len(tagList)):
					tagList[j] = tagDict[tagList[j]]
				# alpha is the first of the list if it were sorted alphabetically
				alpha = min(tagList)
			# Assign alpha key to task dictionary
			i['tagalpha'] = str(alpha)

	# Sort tasks by chosen key
	print("Sorting tasks")
	sortedlist = sorted(tasks, key=lambda k: k[sort_type])
	for i in range(0, len(tasks)):
		print("Moving task " + sortedlist[i]['text'])
		response = moveTask(user, sortedlist[i]["id"], i)
		# Return status code if not successful
		response = json.loads(response)
		if response['success'] != True:
			return(response)

def cast(user, spellId, targetId = 'none'):
	"""
	Cast a skill (spell) on a target

	spellId: the skill to cast. Takes a string of characters.
	targetId: Query parameter, necessary if the spell is cast on a party member or task. 
		Not used if the spell is cast on the user or the user's current party.
		Takes a string containing a UUID.

	spellId to name mapping: 
	Mage
		fireball: "Burst of Flames" (target: task ID)
		mpheal: "Ethereal Surge" (target: none)
		earth: "Earthquake" (target: none)
		frost: "Chilling Frost" (target: none)
	Warrior 
		smash: "Brutal Smash" (target: taskId)
		defensiveStance: "Defensive Stance" (target: none)
		valorousPresence: "Valorous Presence" (target: none)
		intimidate: "Intimidating Gaze" (target: none)
	Rogue 
		pickPocket: "Pickpocket" (target: taskId)
		backStab: "Backstab" (target: taskId)
		toolsOfTrade: "Tools of the Trade" (target: none)
		stealth: "Stealth" (target: none)
	Healer 
		heal: "Healing Light" (target: none)
		protectAura: "Protective Aura" (target: none)
		brightness: "Searing Brightness" (target: none)
		healAll: "Blessing" (target: none)
	"""
	if targetId == 'none':
		url = 'https://habitica.com/api/v3/user/class/cast/' + spellId
	else:
		url = 'https://habitica.com/api/v3/user/class/cast/' + spellId + '?' + targetId
	print("Casting " + spellId)
	response = postUrl(user, url)
	return(response)

def score(user, taskId, direction):
	"""
	Score a task. i.e., check a todo, daily, or habit.

	Returns a dictionary containing data on the user's character. 
	Namely, gold, level, HP, MP, etc. along with the gold gained
	from this score (called 'delta') and info on any drops received.

	Parameters: 
	Field		Type	Description
	taskId		String	The task _id or alias
	direction	String	The direction for scoring the task
						Allowed values: "up", "down"
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/score/" + direction
	response = postUrl(user, url)
	
	# The content of the response is returned as a string that like a Python dictionary,
	# except "true" and "false" aren't capitalized. Capitalize and convert 
	# to a dictionary.
	response = response.replace('true', 'True')
	response = response.replace('false', 'False')
	returnDict = ast.literal_eval(response)
	return(returnDict['data'])

def getUserProfile(user):
	"""
	Get the authenticated user's profile

	The user profile contains data related to the authenticated user including (but not limited to): 
	Achievements Authentications (including types and timestamps) Challenges Flags (including armoire, 
	tutorial, tour etc...) Guilds History (including timestamps and values) Inbox (includes message history) 
	Invitations (to parties/guilds) Items (character's full inventory) New Messages (flags for groups/guilds 
	that have new messages) Notifications Party (includes current quest information) Preferences (user selected prefs) 
	Profile (name, photo url, blurb) Purchased (includes purchase history, gem purchased items, plans) 
	PushDevices (identifiers for mobile devices authorized) Stats (standard RPG stats, class, buffs, xp, etc..) 
	Tags TasksOrder (list of all ids for dailys, habits, rewards and todos)
	"""
	url = 'https://habitica.com/api/v3/user'
	content = getUrl(user, url)
	print("Getting user data")
	return(content['data'])

def getAnonymizedData(user):
	"""
	Get anonymized user data

	Returns the user's data without: Authentication information 
	NewMessages/Invitations/Inbox Profile Purchased information Contributor information Special items Webhooks
	"""
	url = 'https://habitica.com/api/v3/user/anonymized'
	content = getUrl(user, url)
	print("Getting user data")
	return(content['data'])

def getStats(user):
	"""
	Get the user's stats. i.e., health, gold, exp, etc.

	Returns a dictionary containing data on the user's stats. The keys are listed below:
	['training', 'exp', 'buffs', 'int', 'hp', 'gp', 'maxMP', 'maxHealth', 'per', 'toNextLevel', 
	'points', 'mp', 'str', 'lvl', 'class', 'con']
	"""
	content = getUserProfile(user)
	return(content['stats'])

def updateUser(user, updates):
	url = 'https://habitica.com/api/v3/user'
	response = putUrl(user, url, updates)
	return(response)

def setStats(user, statsToSetDict):
	payloadDict = {}
	for stat in statsToSetDict:
		payloadDict['stats.'+stat] = statsToSetDict[stat]
	response = updateUser(user, payloadDict)
	return(response)

def manaPotion(user):
	userStats = getStats(user)
	statsToUpdate = {}
	statsToUpdate['gp'] = userStats['gp'] - 25
	statsToUpdate['mp'] = userStats['mp'] + 15
	print(statsToUpdate)
	response = setStats(user, statsToUpdate)
	return(response)

def login(username, password):
	url = 'https://habitica.com/api/v3/user/auth/local/login'
	payload = {'username': username, 'password': password}
	user = {}
	response = postUrl(user, url, payload)
	return(response)

def addTag(user, taskId, tagId):
	url = 'https://habitica.com/api/v3/tasks/' + taskId + '/tags/' + tagId
	response = postUrl(user, url)
	return(response)
