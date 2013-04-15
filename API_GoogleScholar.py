#!/usr/bin/python

'''
API Modul pre sluzbu GoogleScholar
Implementuje zakladne vyhladavanie pomocou tejto sluzby
Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
'''

from bs4 import BeautifulSoup
import sys
import urllib2


'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX
@param:keyword - vyhladavacia fraza
@return: asociativne_pole
'''
def basicSearch(keyword):
	html_file=""
	html_file = sendUrlGooGle_BASIC(keyword)
	
'''
Funkcia, ktora splna zakladne vyhladavanie pomocou sluzby CiteSeerX


@return:asociativne_pole
@return: asociativne_pole
'''	
def extendedSearch(KeywordOpt,keyword,WithoutWords,WithoutWordsArg,Article,PublicPlace,Year,YearArg):
	article_arg=0
	publicplace_arg=0
	year=0
	
	if (Article !=0):
		article_arg=1
	elif (PublicPlace != 0):
		publicplace_arg=0
	
	
def sendGoogle_EXTENDED(keywordsPhrase,Citation,Sort):
	http_req=""

def sendUrlGoogle_BASIC(keywordsPhrase):
	http_req=""
	response=""
	keywordsPhrase=keywordsPhrase.replace(" ","+")
	http_req="http://scholar.google.cz/scholar?hl=cs&q="+ keywordsPhrase+"&btnG="
	req=""
	the_page=""
	req = urllib2.Request(http_request)
	response = urllib2.urlopen(req)
	the_page = response.read()	
	
	return the_page


		

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc)

print(soup.prettify())


	
