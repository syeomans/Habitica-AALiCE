import habotica

# Users
aalice = {'x-api-user': "964a2bfe-35d2-4f8d-92bc-7cbb7e90dcc8", 'x-api-key': "1d8c9062-f5aa-40d4-85ee-32e7f58171b7"}
sam = {'x-api-user': "7c7122d1-17d0-4585-b3b8-31fcb713682e", 'x-api-key': "97f83d3f-a5b7-4903-8a64-03c9f19752e9"}
lauren = {'x-api-user': "b9cd2456-61be-487c-8ec7-918a9ae87a78", 'x-api-key': "64493f4e-0c2d-4e54-9f03-c2183f25acfa"}
party = [aalice, sam, lauren]

#habitDict = habotica.getTaskDict(aalice, "habits", "text", "id")
#habotica.score(aalice, habitDict["Productive Work"], "up")

def checkMessages():
	messages = habotica.getChatData(aalice,50)
	idFile = open("readMessages.txt", "a+")
	idList = []
	for line in idFile:
		idList.append(line[:-1])
	for message in messages:
		if 'aalice' in message['text'].lower() and message['id'] not in idList:
			if 'say' in message['text'].lower():
				index = message['text'].find('say') + len('say') + 1
				phrase = message['text'][index:]
				print('Saying "' + phrase + '"')
				habotica.postChat(aalice, phrase) 
				idFile.write(message['id'] + "\n")
	idFile.close()

# Run Cron
habotica.login("aalise.samuelyeomans@gmail.com", "Habitica513")
habotica.cron(aalice)

partyStats = []
for member in party:
	partyStats.append(habotica.getStats(member))

# If any party member is below 30 health, immediately cast blessing (healAll) until above 30 if aalice has enough mana
for i in range(0,len(partyStats)):
	while partyStats[i]['hp'] <= 30 and partyStats[0]['mp'] >= 25:
		habotica.cast(aalice, 'healAll')
		partyStats[i] = habotica.getStats(party[i])
		partyStats[0] = habotica.getStats(party[0])

# If any party member is below 40 health, cast blessing if above 50% mana
for i in range(0,len(partyStats)):
	while partyStats[i]['hp'] <= 40 and partyStats[0]['mp'] >= (partyStats[0]['maxMP']*0.5):
		habotica.cast(aalice, 'healAll')
		partyStats[i] = habotica.getStats(party[i])
		partyStats[0] = habotica.getStats(party[0])

# If mana is above 80%, cast protective aura (protectAura)
while partyStats[0]['mp'] >= (partyStats[0]['maxMP']*0.8):
	habotica.cast(aalice,'protectAura')
	partyStats[0] = habotica.getStats(party[0])

# Check off healing daily unless it's already marked as completed
healDailyId = '63b1c445-f499-48fa-9e15-b414286d038a'
if not habotica.getTask(aalice, healDailyId)['completed']:
	habotica.score(aalice, healDailyId, 'up')

checkMessages()