from urlFunctions import postUrl

def abortQuest(creds, groupId = 'party'):
	"""
	Abort a quest. Must be a group leader or quest leader.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/abort'
	return(postUrl(url, creds))

def acceptQuest(creds, groupId = 'party'):
	"""
	Accept a quest

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/accept'
	return(postUrl(url, creds))

def cancelQuest(creds, groupId = 'party'):
	"""
	Cancel a quest. Must be a group leader or quest leader.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/cancel'
	return(postUrl(url, creds))

def forceStartQuest(creds, groupId = 'party'):
	"""
	Force a quest to start. Must be a group leader or quest leader.

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/force-start'
	return(postUrl(url, creds))

def inviteToQuest(creds, questKey, groupId = 'party'):
	"""
	Invite users to a quest

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	questKey: The shorthand name of the quest. ex: 'atom1' is the questKey of "Attack of the Mundane, part 1."
		To see all current quest keys, use the content library: getContent('quests').keys() 
		Keys as of Apr. 14, 2018:
		['armadillo', 'atom1', 'atom2', 'atom3', 'axolotl', 'badger', 'basilist', 'beetle', 'bewilder', 'bunny',
		'burnout', 'butterfly', 'cheetah', 'cow', 'dilatory', 'dilatoryDistress1', 'dilatoryDistress2',
		'dilatoryDistress3', 'dilatory_derby', 'dustbunnies', 'dysheartener', 'egg', 'evilsanta', 'evilsanta2',
		'falcon', 'ferret', 'frog', 'ghost_stag', 'goldenknight1', 'goldenknight2', 'goldenknight3', 'gryphon',
		'guineapig', 'harpy', 'hedgehog', 'hippo', 'horse', 'kraken', 'lostMasterclasser1', 'lostMasterclasser2',
		'lostMasterclasser3', 'lostMasterclasser4', 'mayhemMistiflying1', 'mayhemMistiflying2', 'mayhemMistiflying3',
		'monkey', 'moon1', 'moon2', 'moon3', 'moonstone1', 'moonstone2', 'moonstone3', 'nudibranch', 'octopus', 'owl',
		'peacock', 'penguin', 'pterodactyl', 'rat', 'rock', 'rooster', 'sabretooth', 'sheep', 'slime', 'sloth',
		'snail', 'snake', 'spider', 'squirrel', 'stoikalmCalamity1', 'stoikalmCalamity2', 'stoikalmCalamity3',
		'stressbeast', 'taskwoodsTerror1', 'taskwoodsTerror2', 'taskwoodsTerror3', 'treeling', 'trex', 'trex_undead', 
		'triceratops', 'turtle', 'unicorn', 'vice1', 'vice2', 'vice3', 'whale', 'yarn']
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/invite/' + questKey
	return(postUrl(url, creds))

def leaveQuest(creds, groupId = 'party'):
	"""
	Leave a quest

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/leave'
	return(postUrl(url, creds))


def rejectQuest(creds, groupId = 'party'):
	"""
	Reject a quest

	creds: a dictionary of user credentials formatted as: {'x-api-user': 'your_user_id', 'x-api-key': 'your_api_key'}
	groupId: The group _id (or 'party'). Type: UUID
	"""
	url = 'https://habitica.com/api/v3/groups/' + groupId + '/quests/reject'
	return(postUrl(url, creds))