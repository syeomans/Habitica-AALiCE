from urlFunctions import getUrl, postUrl, putUrl, deleteUrl

class group:
	def __init__(self, credentials, groupId=None, data=None):
		if data == None:
			data = getGroup(credentials, groupId)['data']
		self.credentials = credentials
		self.leaderOnly = data["leaderOnly"]
		self.managers = data["managers"]
		self.purchased = data["purchased"]
		self.privacy = data["privacy"]
		self.memberCount = data["memberCount"]
		self.description = data["description"]
		self.summary = data["summary"]
		self.challengeCount = data["challengeCount"]
		self._id = data["_id"]
		self.quest = data["quest"]
		self.tasksOrder = data["tasksOrder"]
		self.chat = data["chat"]
		self.groupId = data["id"]
		self.balance = data["balance"]
		self.type = data["type"]
		self.leader = data["leader"]
		self.categories = data["categories"]
		self.name = data["name"]

	# def __init__(self, data):
	# 	self.leaderOnly = data["leaderOnly"]
	# 	self.managers = data["managers"]
	# 	self.purchased = data["purchased"]
	# 	self.privacy = data["privacy"]
	# 	self.memberCount = data["memberCount"]
	# 	self.description = data["description"]
	# 	self.summary = data["summary"]
	# 	self.challengeCount = data["challengeCount"]
	# 	self._id = data["_id"]
	# 	self.quest = data["quest"]
	# 	self.tasksOrder = data["tasksOrder"]
	# 	self.chat = data["chat"]
	# 	self.groupId = data["id"]
	# 	self.balance = data["balance"]
	# 	self.type = data["type"]
	# 	self.leader = data["leader"]
	# 	self.categories = data["categories"]
	# 	self.name = data["name"]

	def invite(self, credentials, emails=None, uuids=None):
		"""
		Group - Invite users to a group

		You can provide both emails and uuids, or just one. You must provide at least one.

		credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		emails: An array of dictionaries, each representing one email address to invite
			email: The email address of the user being invited.
			name(optional): The name of the user being invited.
			ex: [{'email': 'user1email@example.com'}, {'email': 'user2@email.com', 'name': 'user2'}]
		uuids: An array of uuids to invite
			ex: ["user-id-of-existing-user", "user-id-of-another-existing-user"]

		TODO: This function doesn't work. 
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/invite'
		if emails != None and uuids != None:
			payload = {'emails': emails, 'uuids': uuids}
		elif emails != None:
			payload = {'emails': emails}
		elif uuids != None:
			payload = {'uuids': uuids}
		else:
			return(postUrl(url, credentials))
		# print(payload)
		return(postUrl(url, credentials, payload))

	def removeManager(self, credentials):
		"""
		Group - Remove a manager from a group

		credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/remove-manager'
		return(postUrl(url, credentials))

	def removeMember(self, credentials, memberId):
		"""
		Group - Remove a member from a group

		Permission: GroupLeader, Admin

		credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
		memberId: The _id of the member to remove
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/removeMember/' + memberId
		return(postUrl(url, credentials))

	def updateGroup(self, credentials):
		"""
		Group - Remove a member from a group

		Permission: GroupLeader, Admin

		TODO: There's something missing from the online documentation. I have a feeling like there
			should be a body parameter containing all the changes to make. 
			Online documentation: https://habitica.com/apidoc/#api-Group-UpdateGroup

		credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId
		return(putUrl(url, credentials))

def addManager(credentials, groupId):
	"""
	Add a manager to a group

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/add-manager'
	return(postUrl(url, credentials))

def createGroupPlan(credentials):
	"""
	Create a Group and then redirect to the correct payment

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = 'https://habitica.com/api/v3/groups/create-plan'
	return(postUrl(url, credentials))

def createGroup(credentials, name, groupType, privacy):
	"""
	Create a Group and then redirect to the correct payment

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	name: The name of the group
	groupType: Type of group (guild or party)
		Allowed values: "guild", "party"
	privacy: Privacy of group (party MUST be private)
		Allowed values: "private", "public"
	"""
	url = 'https://habitica.com/api/v3/groups'
	payload = {'name': name, 'type': groupType, 'privacy': privacy}
	return(postUrl(url, credentials, payload))

def getGroupPlans(credentials):
	"""
	Group - Get group plans for a user

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = 'https://habitica.com/api/v3/group-plans'
	return(getUrl(url, credentials))

def getGroup(credentials, groupId):
	"""
	Group - Get group

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId
	return(getUrl(url, credentials))

def getGroups(credentials, groupType, paginate, page):
	"""
	Group - Get groups for a user

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupType: The type of groups to retrieve. Must be a query string representing a list of values like 'tavern,party'. 
		Possible values are party, guilds, privateGuilds, publicGuilds, tavern
	paginate: Public guilds support pagination. When true guilds are returned in groups of 30
		Allowed values: "true", "false"
	page: When pagination is enabled for public guilds this parameter can be used to specify the page number 
		(the initial page is number 0 and not required)
	"""
	url = 'https://habitica.com/api/v3/groups/'
	return(getUrl(url, credentials))

def invite(credentials, groupId, emails=None, uuids=None):
	"""
	Group - Invite users to a group

	You can provide both emails and uuids, or just one. You must provide at least one.

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	emails: An array of dictionaries, each representing one email address to invite
		email: The email address of the user being invited.
		name(optional): The name of the user being invited.
		ex: [{'email': 'user1email@example.com'}, {'email': 'user2@email.com', 'name': 'user2'}]
	uuids: An array of uuids to invite
		ex: ["user-id-of-existing-user", "user-id-of-another-existing-user"]

	TODO: This function doesn't work. 
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/invite'
	if emails != None and uuids != None:
		payload = {'emails': emails, 'uuids': uuids}
	elif emails != None:
		payload = {'emails': emails}
	elif uuids != None:
		payload = {'uuids': uuids}
	else:
		return(postUrl(url, credentials))
	# print(payload)
	return(postUrl(url, credentials, payload))

def joinGroup(credentials, groupId):
	"""
	Group - Join a group

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/join'
	return(postUrl(url, credentials))

def leaveGroup(credentials, groupId, keep=None):
	"""
	Group - Leave a group

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	keep: Whether or not to keep challenge tasks belonging to the group being left.
		Default value: keep-all
		Allowed values: "remove-all", "keep-all"
	"""
	if keep == None:
		url = 'https://habitica.com/api/v3/groups/:groupId/leave'
	else:
		url = 'https://habitica.com/api/v3/groups/:groupId/leave?keep=' + keep
	return(postUrl(url, credentials))

def rejectInvite(credentials, groupId):
	"""
	Group - Reject a group invitation

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/reject-invite'
	return(postUrl(url, credentials))

def removeManager(credentials, groupId):
	"""
	Group - Remove a manager from a group

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/remove-manager'
	return(postUrl(url, credentials))

def removeMember(credentials, groupId, memberId):
	"""
	Group - Remove a member from a group

	Permission: GroupLeader, Admin

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	memberId: The _id of the member to remove
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/removeMember/' + memberId
	return(postUrl(url, credentials))

def updateGroup(credentials, groupId):
	"""
	Group - Remove a member from a group

	Permission: GroupLeader, Admin

	TODO: There's something missing from the online documentation. I have a feeling like there
		should be a body parameter containing all the changes to make. 
		Online documentation: https://habitica.com/apidoc/#api-Group-UpdateGroup

	credentials: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id ('party' for the user party and 'habitrpg' for tavern are accepted)
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId
	return(putUrl(url, credentials))