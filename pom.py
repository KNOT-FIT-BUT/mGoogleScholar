#html_file = sendUrlGooGle_BASIC(keyword)
	html_file=html_doc
	soup = BeautifulSoup(html_file)
	
	
	title_parse = soup.find('meta',attrs={'name':'citation_title'})

	if (title_parse != "none"):
		parsed_list.append(title_parse)
	else:
		parsed_list.append("0")
		
	author_parse = soup.find('meta',attrs={'name':'citation_author'})
	if (title_parse != "none"):
		parsed_list.append(author_parse)
	else:
		parsed_list.append("0")
	vol_parse= soup.find('meta',attrs={'name':'citation_volume'})
	
	if (title_parse != "none"):
		parsed_list.append(vol_parse)
	else:
		parsed_list.append("0")
	date_parse= soup.find('meta',attrs={'name':'citation_date'})
	
	if (title_parse != "none"):
		parsed_list.append(vol_parse)
	else:
		parsed_list.append("0")
	issn_parse=soup.find('meta',attrs={'name':'citation_issn'})
	
	if (title_parse != "none"):
		parsed_list.append(issn_parse)
	else:
		parsed_list.append("0")
	abstract_url_parse=soup.find('meta',attrs={'name':'citation_abstract_html_url'})
	
	if (title_parse != "none"):
		parsed_list.append(abstract_url_parse)
	else:
		parsed_list.append("0")
		
	pdf_url_parse = soup.find('meta',attrs={'name':'citation_pdf_url'})
	
	if (title_parse != "none"):
		parsed_list.append(pdf_url_parse)
	else:
		parsed_list.append("0")
	language_parse=soup.find('meta',attrs={'name':'citation_language'})
	
	if (title_parse != "none"):
		parsed_list.append(language_parse)
	else:
		parsed_list.append("0")
	keywords_parse=soup.find('meta',attrs={'name':'citation_keywords'})
	
	if (title_parse != "none"):
		parsed_list.append(keywords_parse)
	else:
		parsed_list.append("0")
	isbn_parse=soup.find('meta',attrs={'name':'citation_isbn'})
	if (title_parse != "none"):
		parsed_list.append(isbn_parse)
	else:
		parsed_list.append("0")
	
	
	for h in range(0,1):
		result_dic[insert_key]=parsed_list
		insert_key=insert_key+1
	   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
   ''' spravne extrakcia '''
	url="http://www.utexas.edu/world/univ/alpha/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())
	universities=soup.findAll('a',{'class':'institution'})
	for eachuniversity in universities:
	print eachuniversity['href']+","+eachuniversity.string
''' '''
