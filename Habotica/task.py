from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

class task:
	def __init__(self, credentials, taskId=None, data=None):
		"""
		Parent class for habit, daily, todo, reward, and completed todo.

		user: A reference to a user object that this task belongs to. All tasks must belong to a user.
		data: task data returned from an API call
		"""
		if data == None:
			data = getTask(credentials, taskId)['data']
		self.data = data
		self.group = data['group']
		self.tags = data['tags']
		self.text = data['text']
		self.challenge = data['challenge']
		self.userId = [data['userId'] if 'userId' in data.keys() else None]
		self.value = data['value']
		self.id = data['id']
		self.priority = data['priority']
		self.notes = data['notes']
		self.updatedAt = data['updatedAt']
		self._id = data['_id']
		self.type = data['type']
		self.reminders = data['reminders']
		self.createdAt = data['createdAt']
		self.credentials = credentials

	def addTag(self, tagId):
		"""
		Task - Add a tag to a task

		tagId: The tag id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/tags/" + tagId
		payload = {"taskId": self.id, "tagId": tagId}
		response = postUrl(url, self.credentials, payload)
		self.tags.append(tagId)
		return(response)

	def createChecklist(self, text):
		"""
		Task - Add an item to the task's checklist

		TODO: move to children classes that use this

		text: The text of the checklist item
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""
		Task - Delete a checklist item from a task

		TODO: move to children classes that use this

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def removeTag(self, tagId):
		"""
		Task - Delete a tag from a task

		tagId: The tag id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/tags/" + tagId
		response = deleteUrl(url, self.credentials)
		self.tags.remove(tagId)
		return(response)

	def deleteTask(self):
		"""
		Task - Delete a task given its id

		TODO: test

		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id
		return(deleteUrl(url, self.credentials))

	def scoreChecklist(self, itemId):
		"""
		Task - Score a checklist item

		TODO: test
		TODO: move to children classes that use this

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def scoreTask(self, direction):
		"""
		Task - Score a task

		TODO: test
		TODO: move to children classes that use this

		direction: The direction for scoring the task. Allowed values: "up", "down"
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/score/" + direction
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""
		Task - Unassign a user from a task
		Unassigns a user to from a group task

		TODO: test
		TODO: move to children classes that use this

		itemId: The checklist item _id
		text: The text that will replace the current checkitem text.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

	def updateTask(self, text = None, attribute = None, collapseChecklist = None, notes = None,
				date = None, priority = None, reminders = None, frequency = None, repeat = True,
				everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
		"""
		Task - Update a task

		TODO: test

		text: String (optional). The text to be displayed for the task
		attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
			Allowed values: "str", "int", "per", "con"
		collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
			Default value: false
		notes (optional): String. Extra notes
		date (optional): String. Due date to be shown in task list. Only valid for type "todo."
		priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
			Default value: 1
			Allowed values: "0.1", "1", "1.5", "2"
		reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time.
			For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
		frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days".
			Only valid for type "daily".
			Default value: weekly
			Allowed values: "weekly", "daily"
		repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon.
			Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s.
			Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
			Default value: true
		everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is
			available again.
			Default value: 1
		streak (optional): Number. Number of days that the task has consecutively been checked off.
			Only valid for type "daily"
			Default value: 0
		startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
		up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for
			"Good habits."
			Default value: true
		down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for
			"Bad habits."
			Default value: true
		value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
			Default value: 0
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id
		payload = {}
		if text != None:
			payload["text"] = text
			self.text = text
		if attribute != None:
			payload["attribute"] = attribute
			self.attribute = attribute
		if collapseChecklist != None:
			payload["collapseChecklist"] = collapseChecklist
			self.collapseChecklist = collapseChecklist
		if notes != None:
			payload["notes"] = notes
			self.notes = notes
		if date != None:
			payload["date"] = date
			self.date = date
		if priority != None:
			payload["priority"] = priority
			self.priority = priority
		if reminders != None:
			payload["reminders"] = reminders
		if frequency != None:
			payload["frequency"] = frequency
			self.frequency = frequency
		if repeat != True:
			payload["repeat"] = repeat
			self.repeat = repeat
		if everyX != 1:
			payload["everyX"] = everyX
			self.everyX = everyX
		if streak != 0:
			payload["streak"] = streak
			self.streak = streak
		if startDate != None:
			payload["startDate"] = startDate
			self.startDate = startDate
		if up != True:
			payload["up"] = up
			self.up = up
		if down != True:
			payload["down"] = down
			self.down = down
		if value != 0:
			payload["value"] = value
			self.value = value
		return(putUrl(url, self.credentials, payload))

class habit(task):
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.frequency = data['frequency']
		self.history = data['history']
		self.counterUp = data['counterUp']
		self.down = data['down']
		self.counterDown = data['counterDown']
		self.up = data['up']

	def scoreTask(self, direction):
		"""
		Task - Score a task

		TODO: test

		direction: The direction for scoring the task. Allowed values: "up", "down"
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/score/" + direction
		return(postUrl(url, self.credentials))

class daily(task):
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.attribute = data['attribute']
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']
		self.startDate = data['startDate']
		self.isDue = data['isDue']
		self.frequency = data['frequency']
		self.daysOfMonth = data['daysOfMonth']
		self.repeat = data['repeat']
		self.nextDue = data['nextDue']
		self.weeksOfMonth = data['weeksOfMonth']
		self.yesterDaily = data['yesterDaily']
		self.everyX = data['everyX']

	def createChecklist(self, text):
		"""
		Task - Add an item to the task's checklist

		text: The text of the checklist item
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""
		Task - Delete a checklist item from a task

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def scoreChecklist(self, itemId):
		"""
		Task - Score a checklist item

		TODO: test

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""
		Task - Unassign a user from a task
		Unassigns a user to from a group task

		TODO: test

		itemId: The checklist item _id
		text: The text that will replace the current checkitem text.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

class todo(task):
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']

	def createChecklist(self, text):
		"""
		Task - Add an item to the task's checklist

		text: The text of the checklist item
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist"
		payload = {"text": text}
		response = postUrl(url, self.credentials, payload)
		self.checklist.append(text)
		return(response)

	def deleteChecklist(self, itemId):
		"""
		Task - Delete a checklist item from a task

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		response = deleteUrl(url, self.credentials)
		self.checklist.remove(itemId)
		return(response)

	def scoreChecklist(self, itemId):
		"""
		Task - Score a checklist item

		TODO: test

		itemId: The checklist item _id
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId + "/score"
		return(postUrl(url, self.credentials))

	def updateChecklist(self, itemId, text):
		"""
		Task - Unassign a user from a task
		Unassigns a user to from a group task

		TODO: test

		itemId: The checklist item _id
		text: The text that will replace the current checkitem text.
		"""
		url = "https://habitica.com/api/v3/tasks/" + self.id + "/checklist/" + itemId
		payload = {"text": text}
		return(putUrl(url, self.credentials, payload))

class reward(task):
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)

class completedTodo(task):
	def __init__(self, credentials, taskId=None, data=None):
		task.__init__(self, credentials, taskId, data)
		self.checklist = data['checklist']
		self.collapseChecklist = data['collapseChecklist']
		self.completed = data['completed']
		self.dateCompleted = data['dateCompleted']



#Functions######################################################################################


def getTaskList(credentials, taskType):
	"""
	Get a list of task objects

	user: a reference to an existing user object
	taskType: one of ['habits', 'dailys', 'todos', 'rewards', 'completedTodos']
	"""
	data = getTasks(credentials, taskType)['data']
	if taskType == 'habits':
		return([habit(credentials, data=i) for i in data])
	if taskType == 'dailys':
		return([daily(credentials, data=i) for i in data])
	if taskType == 'todos':
		return([todo(credentials, data=i) for i in data])
	if taskType == 'rewards':
		return([reward(credentials, data=i) for i in data])
	if taskType == 'completedTodos':
		return([completedTodo(credentials, data=i) for i in data])


def addTag(creds, taskId, tagId):
	"""
	Task - Add a tag to a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	tagId: The tag id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	payload = {"taskId": taskId, "tagId": tagId}
	return(postUrl(url, creds, payload))

def createChecklist(creds, taskId, text):
	"""
	Task - Add an item to the task's checklist

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	text: The text of the checklist item
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist"
	payload = {"text": text}
	return(postUrl(url, creds, payload))

def approveTask(creds, taskId, userId):
	"""
	Task - Approves a user assigned to a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	userId: The id of the user that will be approved
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/approve/" + userId
	return(postUrl(url, creds))

def assignTask(creds, taskId, assignedUserId):
	"""
	Task - Assigns a user to a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	assignedUserId: The id of the user that will be assigned to the task
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/assign/" + assignedUserId
	return(postUrl(url, creds))

def createChallengeTask(creds, challengeId, text, taskType, alias = None, attribute = None, collapseChecklist = False,
						notes = None, date = None, priority = 1, reminders = None, frequency = "weekly",
						repeat = True, everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
	"""
	Task - Create a new task belonging to a challenge
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	text: String. The text to be displayed for the task
	taskType: String. Task type, options are: "habit", "daily", "todo", "reward".
		Allowed values: "habit", "daily", "todo", "reward"
	alias (optional): String. Alias to assign to task
	attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
		Allowed values: "str", "int", "per", "con"
	collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
		Default value: false
	notes (optional): String. Extra notes
	date (optional): String. Due date to be shown in task list. Only valid for type "todo."
	priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
		Default value: 1
		Allowed values: "0.1", "1", "1.5", "2"
	reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time.
		For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
	frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days".
		Only valid for type "daily".
		Default value: weekly
		Allowed values: "weekly", "daily"
	repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon.
		Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s.
		Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
		Default value: true
	everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is
		available again.
		Default value: 1
	streak (optional): Number. Number of days that the task has consecutively been checked off.
		Only valid for type "daily"
		Default value: 0
	startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
	up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for
		"Good habits."
		Default value: true
	down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for
		"Bad habits."
		Default value: true
	value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
		Default value: 0
	"""
	url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId
	payload = {"text": text, "type": taskType}
	if alias != None:
		payload["alias"] = alias
	if attribute != None:
		payload["attribute"] = attribute
	if collapseChecklist != False:
		payload["collapseChecklist"] = collapseChecklist
	if notes != None:
		payload["notes"] = notes
	if date != None:
		payload["date"] = date
	if priority != 1:
		payload["priority"] = priority
	if reminders != None:
		payload["reminders"] = reminders
	if frequency != "weekly":
		payload["frequency"] = frequency
	if repeat != True:
		payload["repeat"] = repeat
	if everyX != 1:
		payload["everyX"] = everyX
	if streak != 0:
		payload["streak"] = streak
	if startDate != None:
		payload["startDate"] = startDate
	if up != True:
		payload["up"] = up
	if down != True:
		payload["down"] = down
	if value != 0:
		payload["value"] = value
	return(postUrl(url, creds, payload))

def getTasks(creds, taskType = None):
	"""
	Task - Get a user's tasks

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskType: one of ['habits', 'dailys', 'todos', 'rewards', 'completedTodos'] (optional)

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
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/user"
	else:
		url = "https://habitica.com/api/v3/tasks/user?type=" + taskType
	return(getUrl(url, creds))

def createGroupTask(creds, groupId):
	"""
	Task - Create a new task belonging to a group
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group the new task(s) will belong to
	"""
	url = "https://habitica.com/api/v3/tasks/group/" + groupId
	payload = {"groupId": groupId}
	return(postUrl(url, creds, payload))

def createTask(creds, text, taskType, tags = None, alias = None, attribute = None, collapseChecklist = False,
				notes = None, date = None, priority = 1, reminders = None, frequency = "weekly", repeat = True,
				everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
	"""
	Task - Create a new task belonging to the user
	Can be passed an object to create a single task or an array of objects to create multiple tasks.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	text: String. The text to be displayed for the task
	taskType: String. Task type, options are: "habit", "daily", "todo", "reward".
		Allowed values: "habit", "daily", "todo", "reward"
	tags (optional): String[]. Array of UUIDs of tags
	alias (optional): String. Alias to assign to task
	attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
		Allowed values: "str", "int", "per", "con"
	collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
		Default value: false
	notes (optional): String. Extra notes
	date (optional): String. Due date to be shown in task list. Only valid for type "todo."
	priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
		Default value: 1
		Allowed values: "0.1", "1", "1.5", "2"
	reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time.
		For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
	frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days".
		Only valid for type "daily".
		Default value: weekly
		Allowed values: "weekly", "daily"
	repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon.
		Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s.
		Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
		Default value: true
	everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is
		available again.
		Default value: 1
	streak (optional): Number. Number of days that the task has consecutively been checked off.
		Only valid for type "daily"
		Default value: 0
	startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
	up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for
		"Good habits."
		Default value: true
	down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for
		"Bad habits."
		Default value: true
	value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
		Default value: 0
	"""
	url = "https://habitica.com/api/v3/tasks/user"
	payload = {"text": text, "type": taskType}
	if tags != None:
		payload["tags"] = tags
	if alias != None:
		payload["alias"] = alias
	if attribute != None:
		payload["attribute"] = attribute
	if collapseChecklist != False:
		payload["collapseChecklist"] = collapseChecklist
	if notes != None:
		payload["notes"] = notes
	if date != None:
		payload["date"] = date
	if priority != 1:
		payload["priority"] = priority
	if reminders != None:
		payload["reminders"] = reminders
	if frequency != "weekly":
		payload["frequency"] = frequency
	if repeat != True:
		payload["repeat"] = repeat
	if everyX != 1:
		payload["everyX"] = everyX
	if streak != 0:
		payload["streak"] = streak
	if startDate != None:
		payload["startDate"] = startDate
	if up != True:
		payload["up"] = up
	if down != True:
		payload["down"] = down
	if value != 0:
		payload["value"] = value
	return(postUrl(url, creds, payload))

def deleteChecklist(creds, taskId, itemId):
	"""
	Task - Delete a checklist item from a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	itemId: The checklist item _id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId
	return(deleteUrl(url, creds))

def removeTag(creds, taskId, tagId):
	"""
	Task - Delete a tag from a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	tagId: The tag id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/tags/" + tagId
	return(deleteUrl(url, creds))

def deleteTask(creds, taskId):
	"""
	Task - Delete a task given its id

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	return(deleteUrl(url, creds))

def clearCompletedTodos(creds):
	"""
	Task - Delete user's completed todos

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/tasks/clearCompletedTodos"
	return(postUrl(url, creds))

def getChallengeTasks(creds, challengeId, taskType = None):
	"""
	Task - Get a challenge's tasks

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The id of the challenge from which to retrieve the tasks
	taskType (optional)	Query parameter to return just a type of tasks
		Allowed values: "habits", "dailys", "todos", "rewards"
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId
	else:
		url = "https://habitica.com/api/v3/tasks/challenge/" + challengeId + "?type=" + taskType
	return(getUrl(url, creds))

def getGroupApprovals(creds, groupId):
	"""
	Task - Get a group's approvals

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group from which to retrieve the approvals
	"""
	url = "https://habitica.com/api/v3/approvals/group/" + groupId
	return(getUrl(url, creds))

def getGroupTasks(creds, groupId, taskType = None):
	"""
	Task - Get a group's tasks

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group from which to retrieve the approvals
	taskType(optional): Query parameter to return just a type of tasks
		Allowed values: "habits", "dailys", "todos", "rewards"
	"""
	if taskType == None:
		url = "https://habitica.com/api/v3/tasks/group/" + groupId
	else:
		url = "https://habitica.com/api/v3/tasks/group/" + groupId + "?type=" + taskType
	return(getUrl(url, creds))

def getTask(creds, taskId):
	"""
	Task - Get a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	return(getUrl(url, creds))

def needsWork(creds, taskId, userId):
	"""
	Task - Group task needs more work
	Mark an assigned group task as needeing more work before it can be approved

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	userId: The id of the assigned user
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/needs-work/" + userId
	return(postUrl(url, creds))

def moveGroupTask(creds, groupId, taskId, position):
	"""
	Task - Move a group task to a specified position
	Moves a group task to a specified position

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group from which to retrieve the approvals
	taskId: The task _id or alias
	position: Where to move the task (-1 means push to bottom). First position is 0
	"""
	url = "https://habitica.com/api/v3/group/" + groupId + "/tasks/" + taskId + "/move/to/" + str(position)
	return(postUrl(url, creds))

def moveTask(creds, taskId, position):
	"""
	Task - Move a task to a new position
	Note: completed To-Dos are not sortable, do not appear in user.tasksOrder.todos, and are ordered by date of
	completion.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	position: Where to move the task (-1 means push to bottom). First position is 0
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/move/to/" + str(position)
	return(postUrl(url, creds))

def scoreChecklist(creds, taskId, itemId):
	"""
	Task - Score a checklist item

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	itemId: The checklist item _id
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId + "/score"
	return(postUrl(url, creds))

def scoreTask(creds, taskId, direction):
	"""
	Task - Score a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	direction: The direction for scoring the task. Allowed values: "up", "down"
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/score/" + direction
	return(postUrl(url, creds))

def unassignTask(creds, taskId, assignedUserId):
	"""
	Task - Unassign a user from a task
	Unassigns a user to from a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	assignedUserId: The id of the user that will be unassigned from the task
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/unassign/" + assignedUserId
	return(postUrl(url, creds))

def unlinkTask(creds, taskId, keep):
	"""
	Task - Unlink a challenge task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	keep: Specifies if the task should be kept(keep) or removed(remove)
		Allowed values: 'keep', 'remove'
	"""
	url = "https://habitica.com/api/v3/tasks/unlink-one/" + taskId + "?keep=" + keep
	return(postUrl(url, creds))

def unlinkTasks(creds, challengeId, keep=None):
	"""
	Task - Unlink a challenge task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id
	keep (optional): Specifies if tasks should be kept(keep-all) or removed(remove-all) after the unlink
		Allowed values: 'keep-all', 'remove-all'
	"""
	if keep == None:
		url = "https://habitica.com/api/v3/tasks/unlink-all/" + challengeId
	else:
		url = "https://habitica.com/api/v3/tasks/unlink-all/" + challengeId + "?keep=" + keep
	return(postUrl(url, creds))

def updateChecklist(creds, taskId, itemId, text):
	"""
	Task - Unassign a user from a task
	Unassigns a user to from a group task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	itemId: The checklist item _id
	text: The text that will replace the current checkitem text.
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId + "/checklist/" + itemId
	payload = {"text": text}
	return(putUrl(url, creds, payload))

def updateTask(creds, taskId, text = None, attribute = None, collapseChecklist = False, notes = None,
				date = None, priority = 1, reminders = None, frequency = "weekly", repeat = True,
				everyX = 1, streak = 0, startDate = None, up = True, down = True, value = 0):
	"""
	Task - Update a task

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	taskId: The task _id or alias
	text: String (optional). The text to be displayed for the task
	attribute (optional): String. User's attribute to use, options are: "str", "int", "per", "con"
		Allowed values: "str", "int", "per", "con"
	collapseChecklist (optional): Boolean. Determines if a checklist will be displayed
		Default value: false
	notes (optional): String. Extra notes
	date (optional): String. Due date to be shown in task list. Only valid for type "todo."
	priority (optional): Number. Difficulty, options are 0.1, 1, 1.5, 2; eqivalent of Trivial, Easy, Medium, Hard.
		Default value: 1
		Allowed values: "0.1", "1", "1.5", "2"
	reminders (optional): String[]. Array of reminders, each an object that must include: a UUID, startDate and time.
		For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3","startDate":"1/16/17","time":"1/16/17" }
	frequency (optional): String. Value "weekly" enables "On days of the week", value "daily" enables "EveryX Days".
		Only valid for type "daily".
		Default value: weekly
		Allowed values: "weekly", "daily"
	repeat (optional): String. List of objects for days of the week, Days that are true will be repeated upon.
		Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s.
		Value of frequency must be "weekly". For example, to skip repeats on Mon & Fri: "repeat":{"f":false,"m":false}
		Default value: true
	everyX (optional): Number. Value of frequency must be "daily", the number of days until this daily task is
		available again.
		Default value: 1
	streak (optional): Number. Number of days that the task has consecutively been checked off.
		Only valid for type "daily"
		Default value: 0
	startDate (optional): Date. Date when the task will first become available. Only valid for type "daily"
	up (optional): Boolean. Only valid for type "habit." If true, enables the "+" under "Directions/Action" for
		"Good habits."
		Default value: true
	down (optional): Boolean. Only valid for type "habit." If true, enables the "-" under "Directions/Action" for
		"Bad habits."
		Default value: true
	value (optional): Number. Only valid for type "reward." The cost in gold of the reward.
		Default value: 0
	"""
	url = "https://habitica.com/api/v3/tasks/" + taskId
	payload = {}
	if text != None:
		payload["text"] = text
	if attribute != None:
		payload["attribute"] = attribute
	if collapseChecklist != False:
		payload["collapseChecklist"] = collapseChecklist
	if notes != None:
		payload["notes"] = notes
	if date != None:
		payload["date"] = date
	if priority != 1:
		payload["priority"] = priority
	if reminders != None:
		payload["reminders"] = reminders
	if frequency != "weekly":
		payload["frequency"] = frequency
	if repeat != True:
		payload["repeat"] = repeat
	if everyX != 1:
		payload["everyX"] = everyX
	if streak != 0:
		payload["streak"] = streak
	if startDate != None:
		payload["startDate"] = startDate
	if up != True:
		payload["up"] = up
	if down != True:
		payload["down"] = down
	if value != 0:
		payload["value"] = value
	return(putUrl(url, creds, payload))
