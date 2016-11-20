# Story
# what if a program could talk to you through symbols instead of language?
# like the Golden Compass spoke to Lyra in His Dark Materials
# or Rory's Story Cubes
# later, sounds can be attached to symbols and emotion to form the auditoy part of this language
# it will be similar to what R2D2 is doing, but not so much whistling

import xml.etree.ElementTree
import random

import CommonMethods as cm


basicLanguagePath  = "./basicLanguage.xml"
basicKnowledgePath = "./basicKnowledge.xml" 

basicLanguageSymbols = []
basicPatterns        = []
basicStories         = []

# Methods
def loadBasicLanguage():
	e = xml.etree.ElementTree.parse(basicLanguagePath).getroot()
	for s in e.findall("Symbol"):
		symbol = cm.Symbol(s.get("name"), s.get("categ"))
		basicLanguageSymbols.append(symbol)
	print("basic language loaded")

def loadBasicKnowledge():
	e = xml.etree.ElementTree.parse(basicKnowledgePath).getroot()
	for p in e.findall("Patterns")[0].findall("Pattern"):
		basicPatterns.append(p.get("content"))
	for s in e.findall("Stories")[0].findall("Story"):
		story = cm.Story(s.get("content"), s.get("valid"))
		basicStories.append(story)
	print("basic knowledge loaded")

def getRandomSymbolName(categ):
	categSymbolNames = []
	for s in basicLanguageSymbols:
		if s.categ == categ:
			categSymbolNames.append(s.name)
	return categSymbolNames[random.randint(0,(len(categSymbolNames)-1))]

def understand(story):
	print("story:   " + story)
	# get the symbols
	symbols = story.split(',')
	print("symbols: " + str(symbols))
	# if you don't know a symbol, stop (ask about it later)
	# if you know all symbols, find the pattern (if you don't know it, ask for it later)
	storyPatternElements = []
	for s in symbols:
		if not cm.isSymbolPartOfLanguage(s,basicLanguageSymbols):
			print(s + " is not a known symbol. Stopping story.")
			return
		storyPatternElements.append(cm.getCategOfSymbolName(s,basicLanguageSymbols))
	storyPattern = ",".join(storyPatternElements)
	if storyPattern in basicPatterns:
		print("pattern: " + storyPattern)
	else:
		print(storyPattern + " is not a known pattern. Stopping story.")
		return
	# if the story you heard is false, stop (...? later)
	for s in basicStories:
		if s.content == story:
			if s.valid == "false":
				print("Story not true. Stopping story.")
				return
			elif s.valid == "true":
				print("True story")

	# tell me a story based on this pattern - not necesarily true
	myStory = []
	isMyStoryTrue = False

	# todo: get rid of all the translations you have to do - just keep all in symbols
	while not isMyStoryTrue:
		myStory = []
		for elem in storyPatternElements:
			myStory.append(getRandomSymbolName(elem))
		s = ",".join(myStory)
		for k in basicStories:
			if k.content == s:
				isMyStoryTrue = (k.valid == "true")
				break

	print("Story > " + ",".join(myStory))


# Warmup
loadBasicLanguage()
loadBasicKnowledge()

# Unleash the creativity
#while(true):
# todo: make all possible connections and for each one ask me for yes or no - 
# that's how you learn - I don't have to give you anything more than the words

# current models rely heavily on math to make 2 args become 1 arg = the result
# but we don't use math in our heads, then what do we use to come to one result?
# I can read a cat and pet a book.

# for s in basicLanguageSymbols:
# 	print(s.name)
# for p in basicPatterns:
# 	print(p)
# for s in basicStories:
# 	print(s.content + " " + s.valid)

print("Tell Story a story and she will tell you one in return.")

while(True):
	user_says = raw_input("you > ")

	# understand the input by comparing it with everything you know:
	# are all symbols known?
	# is the pattern known?
	# is this story true?
	understand(user_says)
	


