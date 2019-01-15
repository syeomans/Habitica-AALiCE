"""
This file is largely experimental and not well-incorporated into the rest of this repository.
"""

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

def manaPotion(user):
	userStats = getStats(user)
	statsToUpdate = {}
	statsToUpdate['gp'] = userStats['gp'] - 25
	statsToUpdate['mp'] = userStats['mp'] + 15
	print(statsToUpdate)
	response = setStats(user, statsToUpdate)
	return(response)