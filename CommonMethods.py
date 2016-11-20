# Common Story Methods

class Symbol:
	def __init__(self, name, categ):
		self.name  = name
		self.categ = categ

class Story:
	def __init__(self, content, valid):
		self.content = content
		self.valid   = valid

def getCategOfSymbolName(symbolName, basicLanguageSymbols):
	for s in basicLanguageSymbols:
		if s.name == symbolName:
			return s.categ	

def isSymbolPartOfLanguage(symbolName, basicLanguageSymbols):
	for s in basicLanguageSymbols:
		if s.name == symbolName:
			return True
	return False