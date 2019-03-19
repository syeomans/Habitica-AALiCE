from urlFunctions import getUrl
from user import user
import json
import csv
import urllib2
import requests

# sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")

def exportDataXML(credentials):
	"""
	Data Export - Export user data in XML format

	username: The new username
	"""
	url = "https://habitica.com/export/history.csv"
	return(getUrl(url, credentials))

def getAuthenticatedProfile(credentials, userFields = None):
	"""
	User - Get the authenticated user's profile
	
	The user profile contains data related to the authenticated user including (but not limited to); 
		Achievements
		Authentications (including types and timestamps) 
		Challenges 
		Flags (including armoire, tutorial, tour etc...) 
		Guilds History (including timestamps and values) 
		Inbox 
		Invitations (to parties/guilds) 
		Items (character's full inventory)
		New Messages (flags for groups/guilds that have new messages) 
		Notifications 
		Party (includes current quest information) 
		Preferences (user selected prefs) 
		Profile (name, photo url, blurb) 
		Purchased (includes purchase history, gem purchased items, plans) 
		PushDevices (identifiers for mobile devices authorized) 
		Stats (standard RPG stats, class, buffs, xp, etc..) 
		Tags 
		TasksOrder (list of all ids for dailys, habits, rewards and todos)
	
	
	userFields: A list of comma separated user fields to be returned instead of the entire document. 
		Notifications are always returned.
		Example usage: "achievements,items.mounts"
	"""
	if userFields == None:
		url = "https://habitica.com/api/v3/user"
		return(getUrl(url, credentials))
	else:
		url = "https://habitica.com/api/v3/user?userFields=" + userFields
		return(getUrl(url, credentials))


samCredentials = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}


# url = 'https://habitica.com/export/history.csv'
# request = urllib2.Request(url, headers = samCredentials)
# response = urllib2.urlopen(request)
# cr = csv.reader(response)

# [Task Name, Task ID, Task Type, Date, Value]

# outfile = open('output.csv', 'w')
# for row in cr:
# 	outstr = ""
# 	for column in row:
# 		outstr = (outstr + column + ', ')
# 	outstr = outstr[:-2]
# 	outstr = outstr + '\n'
# 	outfile.write(outstr)
# outfile.close()



CSV_URL = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)


