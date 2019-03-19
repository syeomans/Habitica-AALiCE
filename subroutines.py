# Dependencies: 
# Habotica 
# pip install python-dateutil   <-- this didn't work for me, but the next one did
# sudo apt-get install python3-dateutil

from Habotica import user
import Habotica as habotica
from datetime import date
from datetime import datetime
from dateutil.parser import parse

def isDate(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False 

def datedTags(usr):
	# Get user's tags
	tagDict = usr.tagNameToIdDict

	# Create tags if they aren't already there
	if "Today" not in tagDict.keys():
		print("Creating tag 'Today'")
		habotica.createTag(usr.credentials, "Today")
		newTags = habotica.getTags(usr.credentials)['data']
		tagDict = {i['name']:i['id'] for i in newTags}
	if "Tomorrow" not in tagDict.keys():
		print("Creating tag 'Tomorrow'")
		habotica.createTag(usr.credentials, "Tomorrow")
		newTags = habotica.getTags(usr.credentials)['data']
		tagDict = {i['name']:i['id'] for i in newTags}
	if "This week" not in tagDict.keys():
		print("Creating tag 'This week'")
		habotica.createTag(usr.credentials, "This week")
		newTags = habotica.getTags(usr.credentials)['data']
		tagDict = {i['name']:i['id'] for i in newTags}
	if "This month" not in tagDict.keys():
		print("Creating tag 'This month'")
		habotica.createTag(usr.credentials, "This month")
		newTags = habotica.getTags(usr.credentials)['data']
		tagDict = {i['name']:i['id'] for i in newTags}
	if "This year" not in tagDict.keys():
		print("Creating tag 'This year'")
		habotica.createTag(usr.credentials, "This year")
		newTags = habotica.getTags(usr.credentials)['data']
		tagDict = {i['name']:i['id'] for i in newTags}

	# Initialize user's tasks if they aren't already
	if usr.todos == None:
		usr.initTasks()

	# Look through user's task list. Tag all tasks with due dates.
	addTagDict = {"Today": False, "Tomorrow": False, "This week": False, "This month": False, "This year": False, }
	for todo in usr.todos:

		# Clear out addTagDict from last iteration
		addTagDict = {key: False for key in addTagDict.keys()}

		# Check due date
		if 'date' in todo.data.keys() and todo.data['date'] != None:
			dueDate = todo.data['date'][:10]
		else:
			dueDate = None
		if dueDate != None and dueDate != '':
			today = date.today()
			inList = dueDate.split("-")
			targetDate = date(int(inList[0]), int(inList[1]), int(inList[2]))
			daysAway = (targetDate - today).days 
			if daysAway <= 1:
				addTagDict["Today"] = True
			elif daysAway == 2:
				addTagDict["Tomorrow"] = True
			elif daysAway <= 7:
				addTagDict["This week"] = True
			elif daysAway <= 30:
				addTagDict["This month"] = True
			elif daysAway <= 365:
				addTagDict["This year"] = True

		# Check task text
		if "{" in todo.text and "}" in todo.text:
			# Grab the date between "{" and "}"
			index1 = todo.text.index("{") + 1 # +1 because 0 indexing
			index2 = todo.text.index("}")
			targetText = todo.text[index1 : index2]
			# Check if the text between curly braces is a valid date
			if (isDate(targetText)):
				# Convert text to datetime object
				targetDate = parse(targetText) 
				# Calculate days between target date and today's date
				daysAway = (targetDate - datetime.now()).days + 1
				# Assign a tag to apply based on the number of days from now
				if daysAway <= 0:
					addTagDict["Today"] = True
				elif daysAway == 1:
					addTagDict["Tomorrow"] = True
				elif daysAway <= 7:
					addTagDict["This week"] = True
				elif daysAway <= 30:
					addTagDict["This month"] = True
				elif daysAway <= 365:
					addTagDict["This year"] = True

		# Check task notes
		if todo.notes != None: # Sometimes there aren't any notes.
			if "{" in todo.notes and "}" in todo.notes:
				# Grab the date between "{" and "}"
				index1 = todo.notes.index("{") + 1 # +1 because 0 indexing
				index2 = todo.notes.index("}")
				targetText = todo.notes[index1 : index2]
				# Check if the text between curly braces is a valid date
				if (isDate(targetText)):
					# Convert text to datetime object
					targetDate = parse(targetText) 
					# Calculate days between target date and today's date
					daysAway = (targetDate - datetime.now()).days + 1
					# Assign a tag to apply based on the number of days from now
					if daysAway <= 0:
						addTagDict["Today"] = True
					elif daysAway == 1:
						addTagDict["Tomorrow"] = True
					elif daysAway <= 7:
						addTagDict["This week"] = True
					elif daysAway <= 30:
						addTagDict["This month"] = True
					elif daysAway <= 365:
						addTagDict["This year"] = True

		# Check checklist (list of dictionaries or blank list if none)
		if todo.checklist != []: # If the checklist is not blank
			for item in todo.checklist:
				if item['completed'] == False:
					if "{" in item['text'] and "}" in item['text']:
						# Grab the date between "{" and "}"
						index1 = item['text'].index("{") + 1 # +1 because 0 indexing
						index2 = item['text'].index("}")
						targetText = item['text'][index1 : index2]
						# Check if the text between curly braces is a valid date
						if (isDate(targetText)):
							# Convert text to datetime object
							targetDate = parse(targetText) 
							# Calculate days between target date and today's date
							daysAway = (targetDate - datetime.now()).days + 1
							# Assign a tag to apply based on the number of days from now
							if daysAway <= 0:
								addTagDict["Today"] = True
							elif daysAway == 1:
								addTagDict["Tomorrow"] = True
							elif daysAway <= 7:
								addTagDict["This week"] = True
							elif daysAway <= 30:
								addTagDict["This month"] = True
							elif daysAway <= 365:
								addTagDict["This year"] = True

		# Remove any tags that shouldn't be on this task
		for key in addTagDict.keys():
			if tagDict[key] in todo.tags and addTagDict[key] == False:
				print('Removing tag "' + key + '" from task "' + todo.text + '"')
				todo.removeTag(tagDict[key])

		# Add all tags that should be on this task
		for key in addTagDict.keys():
			if tagDict[key] not in todo.tags and addTagDict[key] == True:
				print('Adding tag "' + key + '" to task "' + todo.text + '"')
				todo.addTag(tagDict[key])

		



