import Habotica as habotica
from Habotica import user

# Users
print("Getting party")
aalice = user("964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", "1d8c9062-f5aa-40d4-85ee-32e7f58171b7")
sam = user("7c7122d1-17d0-4585-b3b8-31fcb713682e", "97f83d3f-a5b7-4903-8a64-03c9f19752e9")
lauren = user("b9cd2456-61be-487c-8ec7-918a9ae87a78", "64493f4e-0c2d-4e54-9f03-c2183f25acfa")
party = [aalice, sam, lauren]

#habitDict = habotica.getTaskDict(aalice, "habits", "text", "id")
#habotica.score(aalice, habitDict["Productive Work"], "up")

# def checkMessages():
# 	aalice.initMessages()
# 	messages = habotica.getChatData(aalice,50)
# 	idFile = open("readMessages.txt", "a+")
# 	idList = []
# 	for line in idFile:
# 		idList.append(line[:-1])
# 	for message in messages:
# 		if 'aalice' in message['text'].lower() and message['id'] not in idList:
# 			if 'say' in message['text'].lower():
# 				index = message['text'].find('say') + len('say') + 1
# 				phrase = message['text'][index:]
# 				print('Saying "' + phrase + '"')
# 				habotica.postChat(aalice, phrase) 
# 				idFile.write(message['id'] + "\n")
# 	idFile.close()

# Run Cron
print("Running cron")
aalice.cron()


# If any party member is below 30 health, immediately cast blessing (healAll) until above 30 if aalice has enough mana
for member in party:
	while member.hp <= 30 and aalice.mp >= 25:
		print("Casting Blessing")
		aalice.cast('healAll')
		# Update party member's hp
		healing = (aalice.con + aalice.int + 5) * 0.075
		for member in party:
			member.hp = [member.hp + healing if member.hp+healing <= 50 else 50]

# If any party member is below 43 health, cast blessing if above 50% mana
for member in party:
	while member.hp <= 43 and aalice.mp >= aalice.maxMP*0.5:
		print("Casting Blessing")
		aalice.cast('healAll')
		# Update party member's hp
		healing = (aalice.con + aalice.int + 5) * 0.075
		for member in party:
			member.hp = [member.hp + healing if member.hp+healing <= 50 else 50]

# If mana is above 80%, cast protective aura (protectAura)
while aalice.mp >= aalice.maxMP*0.8:
	print("Casting Protective Aura")
	aalice.cast('protectAura')

# Check off healing daily unless it's already marked as completed
print("Initializing tasks")
aalice.initTasks()
healDailyId = '63b1c445-f499-48fa-9e15-b414286d038a'
healDailyIndex = aalice.dailyOrder.index(healDailyId)
healDaily = aalice.dailys[healDailyIndex]

# if not habotica.getTask(aalice.credentials, healDailyId)['completed']:
# 	habotica.score(aalice.credentials, healDailyId, 'up')
if not healDaily.completed == 'completed':
	print("Scoring task")
	healDaily.scoreTask('up')
# checkMessages()