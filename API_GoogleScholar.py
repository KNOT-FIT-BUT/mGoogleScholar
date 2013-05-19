#!/usr/bin/python

'''
API Modul pre sluzbu GoogleScholar
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2
import re
import time

'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraza
@return: asociativne_pole
'''
def basicSearch(keyword):
	
	result_dic=dict()
	author_parse=""
	title_parse=""
	date_parse=""
	vol_parse=""
	issn_parse=""
	abstract_url_parse=""
	pdf_url_parse=""
	language_parse=""
	keywords_parse=""
	isbn_parse=""
	insert_key=0
	html_file=""
	parsed_list=[]
	soup=""
	base_url=""
	response=""
	base_url=sendUrlGoogle_BASIC(keyword)
	#time.sleep(15)
	try:
		response = urllib2.urlopen(urllib2.Request(base_url, headers={"User-Agent":"Mozilla/5.0 Cheater/1.0"})) 
	except Exception: pass
		
	soup=BeautifulSoup(response)
	print soup	
	
	
	#print soup
	#print odkazys
	return result_dic



'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby GoogleScholar


@return:asociativne_pole
@return: asociativne_pole
'''	
def extendedSearch(AllWords,WithCorrectPhrase,LeastOneWord,WithoutWords,Occurence,Author,Venue,StartYear,EndYear):
	
	
	base_url=""
	base_url=sendGoogle_EXTENDED(AllWords,WithCorrectPhrase,LeastOneWord,WithoutWords,Occurence,Author,Venue,StartYear,EndYear)
	time.sleep(15)
	try:
		response = urllib2.urlopen(urllib2.Request(base_url, headers={"User-Agent":"Mozilla/5.0 Cheater/1.0"})) 
	except Exception:raise
	soup=""
	soup=BeautifulSoup(soup)
	
	
	
def sendGoogle_EXTENDED(AllWords,WithCorrectPhrase,LeastOneWord,WithoutWords,Occurence,Author,Venue,StartYear,EndYear):
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
		pass
	
	return http_req



def sendUrlGoogle_BASIC(keywordsPhrase):
	http_req=""
	response=""
	try:
		keywordsPhrase=keywordsPhrase.strip()
		keywordsPhrase=keywordsPhrase.replace(" ","+")
		http_req="http://scholar.google.cz/scholar?hl=cs&q="+ keywordsPhrase+"&btnG="
	except Exception:raise

	
	return http_req


ahoj = basicSearch("moje")
sys.exit(0)




#if __name__ == "__main__":
#    main()
