from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

class message:
	def __init__(self, data):
		self.data = data
		self.username = [data['username'] if 'username' in data.keys() else 'system']
		self.userStyles = [data['userStyles'] if 'userStyles' in data.keys() else None]
		self.userId = data['uuid']
		self.text = data['text']
		self.flagCount = data['flagCount']
		self.backer = [data['backer'] if 'backer' in data.keys() else False]
		self.groupId = data['groupId']
		self.client = [data['client'] if 'client' in data.keys() else None]
		self.flags = data['flags']
		self.likes = data['likes']
		self.timestamp = data['timestamp']
		self.contributor = [data['contributor'] if 'contributor' in data.keys() else False]
		self._id = data['_id']
		self.chatId = data['id']
		self.user = [data['user'] if 'user' in data.keys() else self.username]

	def clearFlags(self):
		"""
		Resets the flag count on a chat message. Retains the id of the user's that have flagged the message. 
		(Only visible to moderators)

		Permission: Admin	
	  
		chatId: The chat message id
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags'
		return(postUrl(url, self.credentials))

	def deleteMessage(self, previousMsg = None):
		"""
		Deletes a chat message from a group

		chatId: The chat message id
		previousMsg: The last message's ID fetched by the client so that the whole chat will be returned 
			only if new messages have been posted in the meantime
		"""
		if previousMsg == None:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags'
		else:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/clearflags?previousMsg=' + previousMsg
		return(deleteUrl(url, self.credentials))

	def flagMessage(self):
		"""
		Chat - Flag a group chat message. 

		A message will be hidden from chat if two or more users flag a message. It will be hidden 
		immediately if a moderator flags the message. An email is sent to the moderators about every 
		flagged message.	
	  
		chatId: The chat message id
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/flag'
		return(postUrl(url, self.credentials))

	def likeMessage(self):
		"""
		Chat - Like a group chat message	
	  
		creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		chatId: The chat message id
		groupId: The group _id (or 'party'). Type: UUID
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + self.chatId + '/like'
		return(postUrl(url, self.credentials))

class chat:
	# chat(self, getChat(self.credentials)['data'])
	def __init__(self, credentials, groupId='party', data=None):
		if data == None:
			data = getChat(credentials)['data']
		self.groupId = groupId
		self.credentials = credentials

		# data = getChat(self.user.credentials, self.groupId)['data']
		self.messages = [message(i) for i in data]

	def getMessage(self, chatId):
		for i in self.messages:
			if i.chatId == chatId:
				return(i)

	def clearFlags(self, chatId):
		"""
		Resets the flag count on a chat message. Retains the id of the user's that have flagged the message. 
		(Only visible to moderators)

		Permission: Admin	
	  
		chatId: The chat message id
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags'
		return(postUrl(url, self.credentials))

	def deleteMessage(self, chatId, previousMsg = None):
		"""
		Deletes a chat message from a group

		chatId: The chat message id
		previousMsg: The last message's ID fetched by the client so that the whole chat will be returned 
			only if new messages have been posted in the meantime
		"""
		if previousMsg == None:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags'
		else:
			url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/clearflags?previousMsg=' + previousMsg
		return(deleteUrl(url, self.credentials))

	def flagMessage(self, chatId):
		"""
		Chat - Flag a group chat message. 

		A message will be hidden from chat if two or more users flag a message. It will be hidden 
		immediately if a moderator flags the message. An email is sent to the moderators about every 
		flagged message.	
	  
		chatId: The chat message id
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/flag'
		return(postUrl(url, self.credentials))

	def likeMessage(self, chatId):
		"""
		Chat - Like a group chat message	
	  
		creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		chatId: The chat message id
		groupId: The group _id (or 'party'). Type: UUID
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/' + chatId + '/like'
		return(postUrl(url, self.credentials))

	def markMessagesRead(self):
		"""
		Chat - Mark all messages as read for a group	
	  
		creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		groupId: The group _id (or 'party'). Type: UUID
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat/seen'
		return(postUrl(url, self.credentials))

	def postMessage(self, text):
		"""
		Chat - Post chat message to a group
	  
		creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
		message: The message to post
		groupId: The group _id (or 'party'). Type: UUID
		"""
		url = 'https://habitica.com/api/v3/groups/' + self.groupId + '/chat'
		payload = {"message": text}
		response = postUrl(url, self.credentials, payload)
		exec("response = " + response.replace('true', 'True').replace('false', 'False'))
		messageData = response['data']['message']
		self.messages = [message(messageData)] + self.messages
		return(response)

def clearFlags(creds, chatId, groupId = 'party'):
	"""
	Resets the flag count on a chat message. Retains the id of the user's that have flagged the message. 
	(Only visible to moderators)

	Permission: Admin	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	return(postUrl(url, creds))

def deleteMessage(creds, chatId, groupId = 'party', previousMsg = None):
	"""
	Deletes a chat message from a group

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	previousMsg: The last message's ID fetched by the client so that the whole chat will be returned only if new 
    	messages have been posted in the meantime
	"""
	if previousMsg == None:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags'
	else:
		url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/clearflags?previousMsg=' + previousMsg
	return(deleteUrl(url, creds))

def flagMessage(creds, chatId, groupId = 'party'):
	"""
	Chat - Flag a group chat message. A message will be hidden from chat if two or more users flag a message. It will be hidden immediately 
	if a moderator flags the message. An email is sent to the moderators about every flagged message.	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/flag'
	return(postUrl(url, creds))

def getChat(creds, groupId = 'party'):
	"""
	Chat - Get chat messages from a group. Fetches an array of messages from a group.	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID

	return keys: userV, notifications, data, appVersion, success
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	return(getUrl(url, creds))

def getChatData(creds, groupId = 'party'):
	"""
	Chat - Get chat messages from a group. Returns only a list of messages. 
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	return(getChat(creds, groupId)["data"])

def likeMessage(creds, chatId, groupId = 'party'):
	"""
	Chat - Like a group chat message	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	chatId: The chat message id
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/' + chatId + '/like'
	return(postUrl(url, creds))

def markMessagesRead(creds, groupId = 'party'):
	"""
	Chat - Mark all messages as read for a group	
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat/seen'
	return(postUrl(url, creds))

def postMessage(creds, message, groupId = 'party'):
	"""
	Chat - Post chat message to a group
  
	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	message: The message to post
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/chat'
	payload = {"message": message}
	return(postUrl(url, creds, payload))
