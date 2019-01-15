from urlFunctions import getUrl

class content:
	"""
	Get all contents on Habitica 

	Note: Some content is nested under the below properties and may need to be indexed to access.

	Properties:
	'specialPets', 'premiumPets', 'backgroundsFlat', 'questMounts', 'armoire', 'timeTravelStable', 
	'questPets', 'special', 'spells', 'hatchingPotions', 'officialPinnedItems', 'questEggs', 
	'bundles', 'premiumMounts', 'premiumHatchingPotions', 'userDefaults', 'itemList', 'pets',
	'questsByLevel', 'userDefaultsMobile', 'appearances', 'dropEggs', 'achievements', 'gearTypes',
	'potion', 'gear', 'food', 'eggs', 'faq', 'mystery', 'audioThemes', 'petInfo', 
	'loginIncentives', 'mountInfo', 'backgrounds', 'specialMounts', 'dropHatchingPotions',
	'userCanOwnQuestCategories', 'classes', ucardTypes', 'quests', umounts', 'subscriptionBlocks'
	"""
	def __init__(self, language=None):
		data = getContent(language=None)

		self.contentTypes = data.keys()
		for key in data.keys():
			exStr = "self." + key + " = data['" + key + "']"
			exec(exStr)

def getContent(contentType=None, language=None):
	"""
	Get all available content objects

	language: Language code used for the items' strings. If the authenticated user makes the request, 
		the content will return with the user's configured language.
		Default value: en
		Allowed values: "bg", "cs", "da", "de", "en", "en@pirate", "en_GB", "es", "es_419", "fr", "he", "hu", 
		"id", "it", "ja", "nl", "pl", "pt", "pt_BR", "ro", "ru", "sk", "sr", "sv", "uk", "zh", "zh_TW"

	contentType: Various data about the content of Habitica. The content route contains many keys, but the data 
		listed below are the recomended data to use. Type: string

		mystery: The mystery sets awarded to paying subscribers.
		gear: The gear that can be equipped.
			tree: Detailed information about the gear, organized by type.
			flat: The full key of each equipment.
		spells: The skills organized by class. Includes cards and visual buffs.
		potion: Data about the health potion.
		armoire: Data about the armoire.
		classes: The available classes.
		eggs: All available eggs.
		timeTravelStable: The animals available in the Time Traveler's stable, separated into pets and mounts.
		hatchingPotions: All the hatching potions.
		petInfo: All the pets with extra info.
		mountInfo: All the mounts with extra info.
		food: All the food.
		userCanOwnQuestCategories: The types of quests that a user can own.
		quests: Data about the quests.
		appearances: Data about the apperance properties.
			hair: Data about available hair options.
			shirt: Data about available shirt options.
			size: Data about available body size options.
			skin: Data about available skin options.
			chair: Data about available chair options.
			background: Data about available background options.
		backgrounds: Data about the background sets.
		subscriptionBlocks: Data about the various subscirption blocks. 
	"""
	# Get language. Add to URL as query parameter if specified.
	if language == None:
		url = 'https://habitica.com/api/v3/content'
	else:
		url = 'https://habitica.com/api/v3/content?language=' + language

	# Return only specified content. If none specified, return all content.
	if contentType == None:
		return(getUrl(url)['data'])
	else:
		return(getUrl(url)['data'][contentType])

