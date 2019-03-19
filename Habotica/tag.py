from Habotica.urlFunctions import getUrl, postUrl, putUrl, deleteUrl

def createTag(creds, name):
	"""
	Create a new tag.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	name: the name of the tag to be added
	"""
	url = "https://habitica.com/api/v3/tags"
	payload = {"name": name}
	return(postUrl(url, creds, payload))

def deleteTag(creds, tagId):
	"""
	Delete a user tag given its ID.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	tagId: the tag_id
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	return(deleteUrl(url, creds))

def getTag(creds, tagId):
	"""
	Get a tag given its ID.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	tagId: the tag_id
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	return(getUrl(url, creds))

def getTags(creds):
	"""
	Gets user's tags. Returns a list of dictionaries of tag names and IDs. 

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	"""
	url = "https://habitica.com/api/v3/tags/"
	return(getUrl(url, creds))

def reorderTag(creds, tagId, position):
	"""
	Reorder a tag.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	tagId: the tag_id
	position: Position the tag is moving to. Index starts at 0. (type: integer)
	"""
	url = "https://habitica.com/api/v3/reorder-tags/"
	payload = {"tagId": tagId, "to": position}
	return(postUrl(url, creds, payload))

def updateTag(creds, tagId, name):
	"""
	Update a tag.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	tagId: the tag_id
	name: the new name of the tag
	"""
	url = "https://habitica.com/api/v3/tags/" + tagId
	payload = {"name": name}
	return(putUrl(url, creds, payload))