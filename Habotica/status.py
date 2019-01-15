from urlFunctions import getUrl

def getAPIStatus():
	"""
	Get Habitica's API status.

	Returns -- 
		status: string. 'up' if everything is ok.
	"""
	url = "https://habitica.com/api/v3/status"
	return(getUrl(url))