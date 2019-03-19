import csv
import urllib2
from datetime import datetime, timedelta
from user import user

def calculateAverageGold(user, startDate, endDate=None):
	# Inits
	totalGold = 0.0
	startDate = datetime.strptime(startDate, '%Y-%m-%d')
	endDate = datetime.today() if endDate == None else datetime.strptime(endDate, '%Y-%m-%d')

	# If user's tasks haven't been initialized, init them
	if user.todos == None:
		user.initTasks()

	# Get user's csv data
	url = 'https://habitica.com/export/history.csv'
	request = urllib2.Request(url, headers = user.credentials)
	response = urllib2.urlopen(request)
	data = csv.reader(response) # [Task Name, Task ID, Task Type, Date, Value]

	# Calculate the gold earned from every habit and daily in user's CSV
	for row in data:
		# Skip header row
		if row == ['Task Name', 'Task ID', 'Task Type', 'Date', 'Value']:
			continue

		streak = user.achievements['streak']

		# get this task's difficulty
		if row[2] == "habit":
			for habit in user.habits:
				if habit != None and habit.id == row[1]:
					difficulty = habit.priority
		elif row[2] == "daily":
			for daily in user.dailys:
				if daily != None and daily.id == row[1]:
					difficulty = daily.priority

		# See if this entry was entered between start and end dates
		targetDate = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
		if startDate < targetDate and targetDate < endDate:

			# Make sure task value is between -47.27 and 21.27
			if float(row[4]) < -47.27:
				taskValue = -47.27
			elif float(row[4]) > 21.27:
				taskValue = 21.27
			else:
				taskValue = float(row[4])

			# Calculate the expectation of gold the user earned for this entry (on average, considering crits)
			baseGold = (0.9747**taskValue) * difficulty * (1+user.per*0.02) * (1+streak/100)
			critBonus = 1.5 + ((4.0 * user.str) / (user.str + 200.0))
			critChance = 0.03 * (1 + user.str/100.0)
			gold = baseGold + critBonus * critChance
			totalGold += gold

	# Look through user's completed todos and calculate the gold earned by any between start and end dates
	for completedTodo in user.completedTodos:
		targetDate = completedTodo.dateCompleted[0:10] # Grab only the YY-MM-DD text
		targetDate = datetime.strptime(targetDate, '%Y-%m-%d')
		
		# See if this entry was entered between start and end dates
		if startDate < targetDate and targetDate < endDate:

			# Make sure task value is between -47.27 and 21.27
			if completedTodo.value < -47.27:
				taskValue = -47.27
			elif completedTodo.value > 21.27:
				taskValue = 21.27
			else:
				taskValue = float(completedTodo.value)

			# Calculate the expectation of gold the user earned for this entry (on average, considering crits)
			baseGold = (0.9747**taskValue) * completedTodo.priority * (1+user.per*0.02) * (1+streak/100)
			critBonus = 1.5 + ((4.0 * user.str) / (user.str + 200.0))
			critChance = 0.03 * (1 + user.str/100.0)
			gold = baseGold + critBonus * critChance
			totalGold += gold

	return(totalGold)



samCredentials = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")
# sam.initTasks()

monthGold = calculateAverageGold(sam, "2019-01-08")
print("Gold earned this month: " + str(monthGold))
print("Average gold per day (over last month): " + str(monthGold/31))

