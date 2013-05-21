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
	except Exception:
		raise ValueError("Chyba v pripojeni")
	
		
	soup=BeautifulSoup(response)
	vysledok=""
	vysledok=soup.find('div',attrs={'class':'gs_ri'})
	nazov=""
	vysledok=str(vysledok)
	vysledok=BeautifulSoup(vysledok)
	
	
	#nazov titulu
	nazov=vysledok.find('a')
	#print nazov.contents
	#parsovanie dalsieho parametru
	nazov=vysledok.find('div',attrs={'class':'gs_a'})
	#print nazov.contents
	#parsovnie dalsieho parametru
	nazov=vysledok.find('div',attrs={'class':'gs_rs'})
	#print nazov.contents
	#pocet citacii na clanok
	nazov=vysledok.find('div',attrs={'class':'gs_fl'})
	nazov=str(nazov)
	nazov=BeautifulSoup(nazov)
	nazov=nazov.find('a')
	nazov=str(nazov.contents)
	print nazov[47:50]
	
	
	
	sys.exit(0)
	number_of_cycles=0
	
	
	
	
	
	puvenue=""
	pubyear=""
	snippet=""
	citations=""
	pubabstract=""
	results=""
	list_authors=[]
	pom_list=[]
	pom_string=""
	name_of_pub=""
	pom_string=unicode(pom_string)
	while (True):
		list_authors=[]
		results= soup.findAll('div', attrs={'class' : 'result'})
		
		for i in range(0,len(results)):
			number_of_cycles=number_of_cycles+1
		
		
		for i in range(0,number_of_cycles):
			moje=BeautifulSoup(str(results[i]))
			
			#parsovanie nazvu knihy
			 #a class="remove doc_details"
			name_of_pub= moje.find('a', attrs={'class' : 'doc_details'})
			
			if (not name_of_pub):
				list_authors.append("0")
			else:
				
				
				pom_list.append(name_of_pub.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""

			#parsovanie autora
			authors= moje.find('span', attrs={'class' : 'authors'})
			if (not authors):
				list_authors.append("0")
			else:
				
				
				pom_list.append(authors.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie nazvu publikacie
			pubvenue=moje.find('span', attrs={'class' : 'pubvenue'})
			if (not pubvenue):
				list_authors.append("0")
			else:
				pom_list.append(pubvenue.contents)
				
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
	
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie roku publikacie
			
			
			pubyear= moje.find('span', attrs={'class' : 'pubyear'})
			if (not pubyear):
				list_authors.append("0")
			else:
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#parsovanie snippetu
	
			snippet= moje.find('div', attrs={'class' : 'snippet'})
			
			
			
			if (not snippet):
				list_authors.append("0")
			else:
				
				pom_list.append(snippet.contents)
				#print pom_list
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
			#odstranenie nepotrebnych znacike
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\"","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
		
			#parsovanie citacii
			
			citations= moje.find('span', attrs={'class' : 'citations'})
			if (not citations):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
			
			#parsovanie abstraktu
			
			pubabstract= moje.find('span', attrs={'class' : 'pubabstract'})
			if (not pubabstract):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			#parsovanie poctu citacii na dielos
			if (Include == True):
				citations= moje.find('a', attrs={'class' : 'citation'})
				if (not citations):
					list_authors.append("0")
				else:
					
					pom_list.append(citations.contents)
				
					for p in range(0,len(pom_list[i])):
						pom_string=pom_string + unicode(pom_list[i][p])
					pom_string=pom_string.strip()
					pom_string=pom_string.replace("Cited by","")
					pom_string=pom_string.replace("(","")
					pom_string=pom_string.replace(")","")
					pom_string=pom_string.replace("self","")
					
					pom_string=pom_string.replace("\n","")
					pom_string=pom_string.replace("...","")
					pom_string=pom_string.replace("\t","")
					pom_string=re.sub(r'\s+', ' ', pom_string)
					pom_string=pom_string.strip()
					pom_index=0
					pom_index=pom_string.find(" ")
				
					pom_string=pom_string[:pom_index]
					list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#vlozenie do slovnika
			result_dic[dic_index]=list_authors
			
			dic_index=dic_index+1
		#koniec prehladavanie hmtl suboru
		#snazim sa najst odkaz na dalsiu stranku
		
		pager=soup.find('div',attrs={'id' : 'pager'})
		#pokial som nenasiel ziadny koncim
		if (len(pager) <2):
			break
		#inak prejdem na dalsiu stranku
		else:
			
			next_url= soup.find('div', attrs={'id' : 'pager'})
			pom_list=[]
			author_list=[]
			spom_string=""
			
			base_url="http://citeseerx.ist.psu.edu"
			html_file=urllib2.urlopen(base_url)
	
	
			pom_string= next_url.contents[1].get('href')
	
			base_url=base_url+pom_string
			try:
				html_file=urllib2.urlopen(base_url)
			except Exception:
				raise RuntimeError("Connection error")
			soup=BeautifulSoup(html_file)
	
	#koniec parsovania funkcii
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
	number_of_cycles=0
	
	
	
	
	
	puvenue=""
	pubyear=""
	snippet=""
	citations=""
	pubabstract=""
	results=""
	list_authors=[]
	pom_list=[]
	pom_string=""
	name_of_pub=""
	pom_string=unicode(pom_string)
	while (True):
		list_authors=[]
		results= soup.findAll('div', attrs={'class' : 'result'})
		
		for i in range(0,len(results)):
			number_of_cycles=number_of_cycles+1
		
		
		for i in range(0,number_of_cycles):
			moje=BeautifulSoup(str(results[i]))
			
			#parsovanie nazvu knihy
			 #a class="remove doc_details"
			name_of_pub= moje.find('a', attrs={'class' : 'doc_details'})
			
			if (not name_of_pub):
				list_authors.append("0")
			else:
				
				
				pom_list.append(name_of_pub.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""

			#parsovanie autora
			authors= moje.find('span', attrs={'class' : 'authors'})
			if (not authors):
				list_authors.append("0")
			else:
				
				
				pom_list.append(authors.contents)
			
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.strip()
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie nazvu publikacie
			pubvenue=moje.find('span', attrs={'class' : 'pubvenue'})
			if (not pubvenue):
				list_authors.append("0")
			else:
				pom_list.append(pubvenue.contents)
				
				for p in range(0,len(pom_list[i])):
					
					pom_string=pom_string + unicode(pom_list[i][p])
	
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append(unicode(pom_string))
				
				pom_string=""
			
			#parsovanie roku publikacie
			
			
			pubyear= moje.find('span', attrs={'class' : 'pubyear'})
			if (not pubyear):
				list_authors.append("0")
			else:
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#parsovanie snippetu
	
			snippet= moje.find('div', attrs={'class' : 'snippet'})
			
			
			
			if (not snippet):
				list_authors.append("0")
			else:
				
				pom_list.append(snippet.contents)
				#print pom_list
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
			#odstranenie nepotrebnych znacike
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\t","")
				pom_string=pom_string.replace("<em>","")
				pom_string=pom_string.replace("</em>","")
				pom_string=pom_string.replace("\"","")
				pom_string=pom_string.replace("...","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
		
			#parsovanie citacii
			
			citations= moje.find('span', attrs={'class' : 'citations'})
			if (not citations):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
			
				pom_string=""
			
			#parsovanie abstraktu
			
			pubabstract= moje.find('span', attrs={'class' : 'pubabstract'})
			if (not pubabstract):
				list_authors.append("0")
			else:
				pom_list=[]
				pom_list.append(pubyear.contents)
				
				for p in range(0,len(pom_list[i])):
					pom_string=pom_string + unicode(pom_list[i][p])
				pom_string=pom_string.strip()
				pom_string=pom_string.replace("\n","")
				pom_string=pom_string.replace("...","")
				pom_string=pom_string.replace("\t","")
				pom_string=re.sub(r'\s+', ' ', pom_string)
				list_authors.append((unicode(pom_string)))
				
				pom_string=""
			#parsovanie poctu citacii na dielos
			if (Include == True):
				citations= moje.find('a', attrs={'class' : 'citation'})
				if (not citations):
					list_authors.append("0")
				else:
					
					pom_list.append(citations.contents)
				
					for p in range(0,len(pom_list[i])):
						pom_string=pom_string + unicode(pom_list[i][p])
					pom_string=pom_string.strip()
					pom_string=pom_string.replace("Cited by","")
					pom_string=pom_string.replace("(","")
					pom_string=pom_string.replace(")","")
					pom_string=pom_string.replace("self","")
					
					pom_string=pom_string.replace("\n","")
					pom_string=pom_string.replace("...","")
					pom_string=pom_string.replace("\t","")
					pom_string=re.sub(r'\s+', ' ', pom_string)
					pom_string=pom_string.strip()
					pom_index=0
					pom_index=pom_string.find(" ")
				
					pom_string=pom_string[:pom_index]
					list_authors.append((unicode(pom_string)))
				
				pom_string=""
			
			#vlozenie do slovnika
			result_dic[dic_index]=list_authors
			
			dic_index=dic_index+1
		#koniec prehladavanie hmtl suboru
		#snazim sa najst odkaz na dalsiu stranku
		
		pager=soup.find('div',attrs={'id' : 'pager'})
		#pokial som nenasiel ziadny koncim
		if (len(pager) <2):
			break
		#inak prejdem na dalsiu stranku
		else:
			
			next_url= soup.find('div', attrs={'id' : 'pager'})
			pom_list=[]
			author_list=[]
			spom_string=""
			
			base_url="http://citeseerx.ist.psu.edu"
			html_file=urllib2.urlopen(base_url)
	
	
			pom_string= next_url.contents[1].get('href')
	
			base_url=base_url+pom_string
			try:
				html_file=urllib2.urlopen(base_url)
			except Exception:
				raise RuntimeError("Connection error")
			soup=BeautifulSoup(html_file)
	
	#koniec parsovania funkcii
	return result_dic
	
	
#fukcia zformuje posielanie url na zakladne pokrocileho vyhladavania
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


#funkckia url pre zakladne vyhladavanie na zakladne vyhladavacej fraze
def sendUrlGoogle_BASIC(keywordsPhrase):
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






