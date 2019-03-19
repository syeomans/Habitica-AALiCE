from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl
from Habotica.task import createChallengeTask, getChallengeTasks, habit, daily, todo, reward

def catchKeyError(response, path):
	"""
	Not meant for use outside initializing a user class

	Attempts to set a variable based on a path to the data inside a user's authenticated profile. 
	"""
	try:
		outstr = "output = response" + path
		exec(outstr)
		return(output)
	except KeyError:
		return(None)

class challenge:
	def __init__(self, credentials, challengeId=None, data=None):
		if data == None:
			data = getChallenge(credentials, challengeId)['data']

		self.credentials = credentials
		self.group = catchKeyError(data, "['group']")
		self.prize = catchKeyError(data, "['prize']")
		self.memberCount = catchKeyError(data, "['memberCount']")
		self.description = catchKeyError(data, "['description']")
		self.official = catchKeyError(data, "['official']")
		self.summary = catchKeyError(data, "['summary']")
		self.tasksOrder = catchKeyError(data, "['tasksOrder']")
		self.createdAt = catchKeyError(data, "['createdAt']")
		self.updatedAt = catchKeyError(data, "['updatedAt']")
		self.id = catchKeyError(data, "['id']")
		self.shortName = catchKeyError(data, "['shortName']")
		self._id = catchKeyError(data, "['_id']")
		self.leader = catchKeyError(data, "['leader']")
		self.categories = catchKeyError(data, "['categories']")
		self.name = catchKeyError(data, "['name']")
		self.todos = [todo(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'todos')['data']]
		self.habits = [habit(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'habits')['data']]
		self.dailys = [daily(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'dailys')['data']]
		self.rewards = [reward(self.credentials, data=i) for i in getChallengeTasks(self.credentials, self.id, 'rewards')['data']]

		def deleteChallenge(self):
			"""
			Delete a challenge
			"""
			url = "https://habitica.com/api/v3/challenges/" + self.id
			return(deleteUrl(url, self.credentials))

		def exportChallenge(self):
			"""
			Export a challenge in CSV
			"""
			url = "https://habitica.com/api/v3/challenges/" + self.id + "/export/csv"
			return(getUrl(url, self.credentials))

		def selectChallengeWinner(self, winnerId):
			"""
			Select winner for a challenge

			winnerId: The _id of the winning user. Type: UUID
			"""
			url = "https://habitica.com/api/v3/challenges/" + self.id + "/selectWinner/" + winnerId
			return(postUrl(url, self.credentials))

		def updateChallenge(self, name = "", summary = "", description = "", leader = ""):
			"""
			Update the name, description, or leader of a challenge. User must be challenge leader.

			name (optional): The new full name of the challenge. Type: String
			summary (optional): The new challenge summary. Type: String
			description (optional): The new challenge description. Type: String
			leader (optional): The UUID of the new challenge leader. Type: String
			"""
			url = "https://habitica.com/api/v3/challenges/" + self.id
			
			payload = {}
			if name != "":
				payload["name"] = name
			if summary != "":
				payload["summary"] = summary
			if description != "":
				payload["description"] = description
			if leader != "":
				payload["leader"] = leader

			return(putUrl(url, self.credentials, payload))

def createChallenge(creds, groupId, name, shortName, summary = " ", description = " ", prize = 0):
	"""
	Creates a challenge. Cannot create associated tasks with this route. See createChallengeTasks.

	Note: I'm not an admin, so I can't support creating official challenges.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	name: String containing the full name of the challenge. Type: String
	shortName: A shortened name for the challenge, to be used as a tag. Type: String
	summary (optional): A short summary advertising the main purpose of the challenge; maximum 250 characters; if not supplied, challenge.name will be used
	description (optional): A detailed description of the challenge
	prize (optional): Number of gems offered as a prize to challenge winner. Default value: 0
	official (optional): Whether or not a challenge is an official Habitica challenge (requires admin). Default value: false
	"""
	url = "https://habitica.com/api/v3/challenges"
	payload = {'group': groupId, 'name': name, 'shortName': shortName, 'summary': summary, 'description': description, 'prize': prize}
	return(postUrl(url, creds, payload))

def deleteChallenge(creds, challengeId):
	"""
	Delete a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(deleteUrl(url, creds))

def exportChallenge(creds, challengeId):
	"""
	Export a challenge in CSV

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID

	Returns a csv file. 
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/export/csv"
	return(getUrl(url, creds))

def getChallenge(creds, challengeId):
	"""
	Get a single challenge given its id.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	return(getUrl(url, creds))

def getGroupChallenges(creds, groupId):
	"""
	Get all challenges for a group

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The id of the group to which the challenge belongs. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/groups/" + groupId
	return(getUrl(url, creds))

def getChallenges(creds):
	"""
	Get challenges the user has access to. Includes public challenges, challenges belonging to the user's group, and challenges the user has already joined.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/challenges/user"
	return(getUrl(url, creds))

def joinChallenge(creds, challengeId):
	"""
	Join a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/join"
	return(postUrl(url, creds))

def leaveChallenge(creds, challengeId):
	"""
	Leave a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/leave"
	return(postUrl(url, creds))

def selectChallengeWinner(creds, challengeId, winnerId):
	"""
	Select winner for a challenge

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	winnerId: The _id of the winning user. Type: UUID
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId + "/selectWinner/" + winnerId
	return(postUrl(url, creds))

def updateChallenge(creds, challengeId, name = "", summary = "", description = "", leader = ""):
	"""
	Update the name, description, or leader of a challenge. User must be challenge leader.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	challengeId: The challenge _id. Type: UUID
	name (optional): The new full name of the challenge. Type: String
	summary (optional): The new challenge summary. Type: String
	description (optional): The new challenge description. Type: String
	leader (optional): The UUID of the new challenge leader. Type: String
	"""
	url = "https://habitica.com/api/v3/challenges/" + challengeId
	
	payload = {}
	if name != "":
		payload["name"] = name
	if summary != "":
		payload["summary"] = summary
	if description != "":
		payload["description"] = description
	if leader != "":
		payload["leader"] = leader

	return(putUrl(url, creds, payload))

