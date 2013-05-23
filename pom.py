"""
    @param AllWords: Vyhladania podla vsetkych slov
    @param WithCorrectPhrase: Vyhladavanie podla fraze 
	@param LeastOneWord: Vyhladavanie podla aspon jedneho slova 
    @param WithoutWods: Nezahrnutie slov do vysledkov vyhladavania
    @param Occurence: 0-1 Vyskyt v clanku alebo v nazve diela
    @param Author: Meno autora podla ktoreho sa ma vyhladavat
    @param Venue: Vyhladavanie podla zanra diela
    @param Startyear: Zaciatny rok podla ktoreho sa ma vyhladavat
	@param Endyear: Koncovy rok podla ktoreho sa maju diela vyhladavat
	@return: Spravny vyparsovane url 
"""

def __sendGoogle_EXTENDED(AllWords,WithCorrectPhrase,LeastOneWord,WithoutWords,Occurence,Author,Venue,StartYear,EndYear):
	http_req=""
	try:
		AllWords=AllWords.strip()
		AllWords=AllWords.replace(" ","+")
		WithCorrectPhrase=WithCorrectPhrase.strip()
		WithCorrectPhrase=WithCorrectPhrase.replace(" ","+") 
		LeastOneWord=LeastOneWord.strip()
		LeastOneWord=LeastOneWord.replace(" ","+")
		WithoutWords=WithoutWords.strip()
		WithoutWords=WithoutWords.replace(" ","+")
		if (Occurence == 1):
			Occurence="any"
		if (Occurence == 2):
			Occurence="title"
		Author=Author.strip()
		Author=Author.replace(" ","+")
		Venue=Venue.strip()
		Venue=Venue.replace(" ","+") 
		StartYear=StartYear.strip()
		StartYear=StartYear.replace(" ","+")
		EndYear=EndYear.strip()
		EndYear=EndYear.replace(" ","+")
		http_req= "http://scholar.google.cz/scholar?as_q="+ AllWords+"&as_epq="+ WithCorrectPhrase+"&as_oq="+LeastOneWord+"&as_eq="+ WithoutWords+"&as_occt="+Occurence+"&as_sauthors="+Author+"&as_publication="+Venue+"&as_ylo="+StartYear+"&as_yhi="+EndYear+"&btnG=&hl=cs&as_sdt=0%2C5"
	except IOError:
		raise ValueError("Uncorrect value")
	
	return http_req


"""
    @param keywordsPhrase: Vyhladavacia fraza
	@return: Spravny vyparsovane url 
"""
def __sendUrlGoogle_BASIC(keywordsPhrase):
	http_req=""
	response=""
	try:
		keywordsPhrase=keywordsPhrase.strip()
		keywordsPhrase=keywordsPhrase.replace(" ","+")
		http_req="http://scholar.google.cz/scholar?hl=cs&q="+ keywordsPhrase+"&btnG="
	except Exception:raise

	
	return http_req



ahoj=basicSearch("nieco")
sys.exit(0)
