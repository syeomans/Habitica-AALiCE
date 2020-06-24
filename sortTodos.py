import habotica
aalice = {'x-api-user': "964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", 'x-api-key': "1d8c9062-f5aa-40d4-85ee-32e7f58171b7"}
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}

# Configs
sortTags = ["Today", "Work", "Priority 1", "Priority 2", "Priority 3", "Priority 4", "Priority 5"]

# Gets from Habitica
tasks = habotica.getTasks(sam)
tagList = habotica.getTags(sam,"name")

# Convert list of tag names to sort by into tag ids
for i in range(0, len(sortTags)):
	sortTags[i] = tagList[sortTags[i]]

# Get current (pre-sorted) state of tasks
habiticaTasks = tasks

# Sort tasks locally before pushing to Habitica
sortTags.reverse() # Lower priority tags should be sorted first so they filter to the back throughout the loop
for tag in sortTags:
	hits = [] # front of the list
	misses = [] # back of the list
	for task in tasks:
		# For each task, find its tags. If the tag we're sorting by is in its tag list, move it to the front of the list. 
		thisTag = task["tags"]
		if tag in thisTag:
			hits.append(task)
		else:
			misses.append(task)
	tasks = hits + misses

# Move tasks that are not already in the correct position. 
for i in range(0, len(tasks)):
	if tasks[i]['id'] != habiticaTasks[i]['id']:
		# Move task locally
		habiticaTasks.insert(i, habiticaTasks.pop(habiticaTasks.index(tasks[i])))
		# Move task on Habitica
		print("Moving task " + habiticaTasks[i]['text'])
		habotica.moveTask(sam, habiticaTasks[i]['id'], i)

habitId = '7b811ed9-bb94-4f35-84ec-6e3ad205b9bb'
print("Scoring habit")
print(habotica.score(aalice, habitId, 'up'))
