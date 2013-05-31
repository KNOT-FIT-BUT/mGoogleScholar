#!/usr/bin/env python

"""
    API Modul pre sluzbu GoogleScholar
    Implementuje zakladne vyhladavanie pomocou tejto sluzby
    Modul obsahuje 2 vyhladavacie funkcie: basicSearch a extendedSearch
"""
from bs4 import BeautifulSoup
import sys
import urllib2
import re
import time
"""
     @param keyword: Vyhladaci retazec pre sluzbu
        CiteSeerX. Moze obsahovat viac klucovych
        slov pre vyhladavanie
     @return: Slovnik pricom kazda polozka odpoveda jednemu
        vysledku vyhladavania so vsetkymi informaciami o nej
"""


def BasicSearch(keyword):
    result_dic = dict()
    author_parse = ""
    title_parse = ""
    date_parse = ""
    vol_parse = ""
    issn_parse = ""
    abstract_url_parse = ""
    pdf_url_parse = ""
    language_parse = ""
    keywords_parse = ""
    isbn_parse = ""
    insert_key = 0
    html_file = ""
    parsed_list = []
    soup = ""
    base_url = "http://scholar.google.cz"
    response = ""
    base_url = sendUrlGoogle_BASIC(keyword)

    cit_link = ""
    pom_link = ""
    # time.sleep(15)
    try:
        response = urllib2.urlopen(urllib2.Request(base_url,
                                   headers={"User-Agent":
                                   "Mozilla/5.0 Cheater/1.0"}))
    except Exception:
        raise Exception("Connection error")

    soup = BeautifulSoup(response)

    vysledok = ""
    vysledok = soup.findAll('div', attrs={'class': 'gs_ri'})
    nazov = ""

    vysledok = str(vysledok)
    vysledok = BeautifulSoup(vysledok)

    number_of_cycles = 0

    dic_index = 1
    puvenue = ""
    pubyear = ""
    snippet = ""
    citations = ""
    pubabstract = ""
    results = ""
    list_authors = []
    pom_list = []
    pom_string = ""
    name_of_pub = ""
    lib_link = ""
    pom_link = "http://scholar.google.cz"
    pom_string = unicode(pom_string)
    while (True):
        list_authors = []
        results = soup.findAll('div', attrs={'class': 'gs_ri'})

        for i in range(0, len(results)):
            number_of_cycles = number_of_cycles + 1

        for i in range(0, number_of_cycles):
            moje = BeautifulSoup(str(results[i]))

            # nazov knizky
            niecoo = ""
            niecoo = moje.find('a')
            if (not niecoo):
                list_authors.append("0")
            else:
                pom_string = ""
                pom_list = []

                # pomocne parsovanie kvoli zisteniu ci sa nejedna o cit
                authors = moje.find('div', attrs={'class': 'gs_rs'})
                if (authors):
                    pom_list = niecoo.contents
                else:
                    pomoz = moje.findAll('h3')
                    najdi = 0
                    pomoz = str(pomoz[0].contents)
                    najdi = pomoz.find("</span>")
                    ret = ""
                    ret = pomoz[najdi:]
                    pom_list.append(ret)
                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                pom_string = pom_string.replace("<br>", "")
                pom_string = pom_string.replace("</br>", "")
                list_authors.append(unicode(pom_string))

                pom_string = ""
            # autora a zanru a roku vydania

            name_of_pub = moje.find('div', attrs={'class': 'gs_a'})

            if (not name_of_pub):
                list_authors.append("0")
            else:
                pom_string = ""
                pom_list = []
                pom_list = name_of_pub.contents

                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string2 = str(name_of_pub.contens)

                # odstranenie prebytocnych znakov
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                pom_index = 0
                pom_index2 = 0
                pom_index3 = 0
                pom_string3 = ""
                pom_index4 = pom_string.find("-")
                pom_string8 = ""
                pom_pom_index = 0
                pom_pom_index = pom_string.find(">")
                if (pom_pom_index == -1):
                    pom_string8 = pom_string[:pom_index4 - 1]
                else:
                    pom_string8 = pom_string[pom_pom_index + 1:pom_index4 - 1]
                    pom_string8 = pom_string8.replace("</a>", "")
                for m in re.finditer(",", pom_string):
                    pom_index = m.start()
                for m in re.finditer("-", pom_string):
                    pom_index2 = m.start()
                # parsovanie nazvu vydavatelstva

                pom_string3 = pom_string[pom_index2 + 2:len(pom_string) - 2]
                if (pom_string8.find("<") == -1):
                    list_authors.append(pom_string8)
                else:
                    pom_indexx = pom_string8.find("<")
                    pom_string8 = pom_string8[:pom_indexx]
                    list_authors.append(pom_string8)

                if (pom_index2 != pom_index4):
                    pom_string2 = pom_string[pom_index + 2:pom_index2 - 1]
                else:
                    pom_string2 = pom_string[pom_index2 + 2:]

                pom_string = pom_string[pom_index4 + 2:pom_index]
                if (len(pom_string) != 0):

                    pom_string = unicode(pom_string)

                    if (len(pom_string) < 6):
                        list_authors.append(unicode(pom_string))

                    else:

                        pom_string = pom_string[:]
                        list_authors.append(unicode(pom_string))
                else:
                    list_authors.append("0")
                # ulozenie roku vydania
                if (pom_string2.find("2") == -1 and pom_string2.find("1") == -1):
                    list_authors.append("0")
                else:
                    if (len(pom_string2) <= 5):
                        list_authors.append(pom_string2)
                    else:
                        pom_string2 = pom_string2[len(pom_string2) - 4:]
                        list_authors.append(pom_string2)
                pom_string = ""

            # parsovanie abstraktu
            authors = moje.find('div', attrs={'class': 'gs_rs'})

            if (not authors):
                list_authors.append("0")
            else:

                pom_list = []
                pom_list = authors.contents

                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("<br/>", "")
                pom_string = pom_string.replace("<br>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("Abstract:", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                list_authors.append(unicode(pom_string))

                pom_string = ""

            # poctu citacii clanku a parsovanie odkazu na citacie
            pubvenue = moje.find('div', attrs={'class': 'gs_fl'})

            pubvenue = str(pubvenue)
            pubvenue = BeautifulSoup(pubvenue)
            nazov = pubvenue.findAll('a')

            cit_link = str(nazov[0].get('href'))

            if (not cit_link):
                list_authors.append("0")
            else:
                pom_link = "http://scholar.google.cz"
                pom_link = pom_link + cit_link
                if (cit_link.find("#") == -1):
                    list_authors.append(pom_link)
                else:
                    list_authors.append("0")
            # nazov publikacie
            if (not nazov):
                list_authors.append("0")
            else:

                nazov = nazov[0].contents
                pom_index = 0
                nazov = str(nazov)
                pom_index = nazov.find(":")
                if (pom_index != -1):
                    nazov = nazov[pom_index + 2:len(nazov) - 2]
                    list_authors.append(nazov)
                else:
                    list_authors.append("0")
                pom_string = ""

            # parsovanie odkazu do kniznice kde sa nachadza citacia
            lib_link = moje.find('a')
            if (not lib_link):
                list_authors.append("0")
            else:
                list_authors.append(str(lib_link.get('href')))

            # vlozenie do slovnika
            result_dic[dic_index] = list_authors

            list_authors = []
            dic_index = dic_index + 1
        # koniec prehladavanie hmtl suboru
        # snazim sa najst odkaz na dalsiu stranku

        nazov = soup.findAll('table')
        nazov = str(nazov)
        nazov = BeautifulSoup(nazov)
        nazov = nazov.find('a')
        print "nazov", result_dic[5][0]
        sys.exit(0)
        # pokial som nenasiel ziadny koncim
        if ((str(nazov)) == "None"):

            break
        # inak prejdem na dalsiu stranku
        else:

            base_url = ""
            base_url = "http://scholar.google.cz"
            base_url = base_url + str(nazov['href'])

            try:
                html_file = urllib2.urlopen(urllib2.Request(base_url,
                                                            headers={"User-Agent":
                                                                     "Mozilla/5.0 Cheater/1.0"}))
            except Exception:
                raise Exception("Connection error")

            soup = BeautifulSoup(html_file)

    # koniec parsovania funkcii
    return result_dic

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
    @return: Slovnik pricom kazda polozka odpoveda jednemu
        vysledku vyhladavania so vsetkymi informaciami o nej
"""


def ExtendedSearch(AllWords, WithCorrectPhrase, LeastOneWord, WithoutWords,
                   Occurence, Author, Venue, StartYear, EndYear):

    base_url = ""
    base_url = sendGoogle_EXTENDED(AllWords, WithCorrectPhrase,
                                   LeastOneWord, WithoutWords, Occurence,
                                   Author, Venue, StartYear, EndYear)

    result_dic = dict()
    try:
        response = urllib2.urlopen(urllib2.Request(
                                   base_url, headers={"User-Agent": "Mozilla/5.0 Cheater/1.0"}))
    except Exception:
        raise Exception("Connection error")
    soup = ""
    soup = BeautifulSoup(response)
    vysledok = ""
    vysledok = soup.findAll('div', attrs={'class': 'gs_ri'})
    nazov = ""

    vysledok = str(vysledok)
    vysledok = BeautifulSoup(vysledok)

    number_of_cycles = 0

    dic_index = 1
    puvenue = ""
    pubyear = ""
    snippet = ""
    citations = ""
    pubabstract = ""
    results = ""
    list_authors = []
    pom_list = []
    pom_string = ""
    name_of_pub = ""
    pom_string = unicode(pom_string)
    while (True):
        list_authors = []
        results = soup.findAll('div', attrs={'class': 'gs_ri'})

        for i in range(0, len(results)):
            number_of_cycles = number_of_cycles + 1

        for i in range(0, number_of_cycles):
            moje = BeautifulSoup(str(results[i]))

            # nazov knizky
            niecoo = ""
            niecoo = moje.find('a')
            if (not niecoo):
                list_authors.append("0")
            else:
                pom_string = ""
                pom_list = []

                # pomocne parsovanie kvoli zisteniu ci sa nejedna o cit
                authors = moje.find('div', attrs={'class': 'gs_rs'})
                if (authors):
                    pom_list = niecoo.contents
                else:
                    pomoz = moje.findAll('h3')
                    najdi = 0
                    pomoz = str(pomoz[0].contents)
                    najdi = pomoz.find("</span>")
                    ret = ""
                    ret = pomoz[najdi:]
                    pom_list.append(ret)
                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                pom_string = pom_string.replace("<br>", "")
                pom_string = pom_string.replace("</br>", "")
                list_authors.append(unicode(pom_string))

                pom_string = ""
            # autora a zanru a roku vydania

            name_of_pub = moje.find('div', attrs={'class': 'gs_a'})

            if (not name_of_pub):
                list_authors.append("0")
            else:
                pom_string = ""
                pom_list = []
                pom_list = name_of_pub.contents

                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string2 = str(name_of_pub.contens)

                # odstranenie prebytocnych znakov
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                pom_index = 0
                pom_index2 = 0
                pom_index3 = 0
                pom_string3 = ""
                pom_index4 = pom_string.find("-")
                pom_string8 = ""
                pom_pom_index = 0
                pom_pom_index = pom_string.find(">")
                if (pom_pom_index == -1):
                    pom_string8 = pom_string[:pom_index4 - 1]
                else:
                    pom_string8 = pom_string[pom_pom_index + 1:pom_index4 - 1]
                    pom_string8 = pom_string8.replace("</a>", "")
                for m in re.finditer(",", pom_string):
                    pom_index = m.start()
                for m in re.finditer("-", pom_string):
                    pom_index2 = m.start()
                # parsovanie nazvu vydavatelstva

                pom_string3 = pom_string[pom_index2 + 2:len(pom_string) - 2]
                if (pom_string8.find("<") == -1):
                    list_authors.append(pom_string8)
                else:
                    pom_indexx = pom_string8.find("<")
                    pom_string8 = pom_string8[:pom_indexx]
                    list_authors.append(pom_string8)

                if (pom_index2 != pom_index4):
                    pom_string2 = pom_string[pom_index + 2:pom_index2 - 1]
                else:
                    pom_string2 = pom_string[pom_index2 + 2:]

                pom_string = pom_string[pom_index4 + 2:pom_index]
                if (len(pom_string) != 0):

                    pom_string = unicode(pom_string)

                    if (len(pom_string) < 6):
                        list_authors.append(unicode(pom_string))

                    else:

                        pom_string = pom_string[:]
                        list_authors.append(unicode(pom_string))
                else:
                    list_authors.append("0")
                # ulozenie roku vydania
                if (pom_string2.find("2") == -1 and pom_string2.find("1") == -1):
                    list_authors.append("0")
                else:
                    if (len(pom_string2) <= 5):
                        list_authors.append(pom_string2)
                    else:
                        pom_string2 = pom_string2[len(pom_string2) - 4:]
                        list_authors.append(pom_string2)
                pom_string = ""

            # parsovanie abstraktu
            authors = moje.find('div', attrs={'class': 'gs_rs'})

            if (not authors):
                list_authors.append("0")
            else:

                pom_list = []
                pom_list = authors.contents

                for p in range(0, len(pom_list)):

                    pom_string = pom_string + unicode(pom_list[p])
                pom_string = pom_string.replace("<em>", "")
                pom_string = pom_string.replace("</em>", "")
                pom_string = pom_string.replace("</b>", "")
                pom_string = pom_string.replace("<b>", "")
                pom_string = pom_string.replace("<br/>", "")
                pom_string = pom_string.replace("<br>", "")
                pom_string = pom_string.replace("\n", "")
                pom_string = pom_string.replace("Abstract:", "")
                pom_string = pom_string.replace("...", "")
                pom_string = pom_string.replace("\t", "")
                pom_string = pom_string.strip()
                pom_string = re.sub(r'\s+', ' ', pom_string)
                list_authors.append(unicode(pom_string))

                pom_string = ""

            # poctu citacii clanku a parsovanie odkazu na citacie
            pubvenue = moje.find('div', attrs={'class': 'gs_fl'})

            pubvenue = str(pubvenue)
            pubvenue = BeautifulSoup(pubvenue)
            nazov = pubvenue.findAll('a')

            cit_link = str(nazov[0].get('href'))

            if (not cit_link):
                list_authors.append("0")
            else:
                pom_link = "http://scholar.google.cz"
                pom_link = pom_link + cit_link
                if (cit_link.find("#") == -1):
                    list_authors.append(pom_link)
                else:
                    list_authors.append("0")
            # nazov publikacie
            if (not nazov):
                list_authors.append("0")
            else:

                nazov = nazov[0].contents
                pom_index = 0
                nazov = str(nazov)
                pom_index = nazov.find(":")
                if (pom_index != -1):
                    nazov = nazov[pom_index + 2:len(nazov) - 2]
                    list_authors.append(nazov)
                else:
                    list_authors.append("0")
                pom_string = ""

            # parsovanie odkazu do kniznice kde sa nachadza citacia
            lib_link = moje.find('a')
            if (not lib_link):
                list_authors.append("0")
            else:
                list_authors.append(str(lib_link.get('href')))

            # vlozenie do slovnika
            result_dic[dic_index] = list_authors

            list_authors = []
            dic_index = dic_index + 1
        # koniec prehladavanie hmtl suboru
        # snazim sa najst odkaz na dalsiu stranku

        nazov = soup.findAll('table')
        nazov = str(nazov)
        nazov = BeautifulSoup(nazov)
        nazov = nazov.find('a')
        print "nazov", result_dic[5][0]
        sys.exit(0)
        # pokial som nenasiel ziadny koncim
        if ((str(nazov)) == "None"):

            break
        # inak prejdem na dalsiu stranku
        else:

            base_url = ""
            base_url = "http://scholar.google.cz"
            base_url = base_url + str(nazov['href'])

            try:
                html_file = urllib2.urlopen(urllib2.Request(base_url,
                                                            headers={"User-Agent":
                                                                     "Mozilla/5.0 Cheater/1.0"}))
            except Exception:
                raise Exception("Connection error")

            soup = BeautifulSoup(html_file)

    # koniec parsovania funkcii
    return result_dic
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
    @return: Spravne vyparsovane url
"""


def sendGoogle_EXTENDED(AllWords, WithCorrectPhrase,
                        LeastOneWord, WithoutWords, Occurence, Author,
                        Venue, StartYear, EndYear):
    http_req = ""
    if (type(AllWords) is int or  type(WithCorrectPhrase) is int or type(LeastOneWord) is int or type(WithoutWords) is int or  type(Author) is int or type(Venue) is int):
        raise ValueError("Prohoibited type of arguments")
    if (type(Occurence) is not int):
        raise ValueError("Prohibited type of Occurence")
    if (Occurence != 1 and Occurence != 2):
        raise ValueError("Bad Value of parameter Occurence")

    try:
        if (AllWords is not False):
            AllWords = AllWords.strip()
            AllWords = AllWords.replace(" ", "+")
        else:
            AllWords = str(AllWords)
            AllWords = ""

        if (WithCorrectPhrase is not False):
            WithCorrectPhrase = WithCorrectPhrase.strip()
            WithCorrectPhrase = WithCorrectPhrase.replace(" ", "+")
        else:
            WithCorrectPhrase = str(WithCorrectPhrase)
            WithCorrectPhrase = ""

        if (LeastOneWord is not False):
            LeastOneWord = LeastOneWord.strip()
            LeastOneWord = LeastOneWord.replace(" ", "+")
        else:
            LeastOneWord = str(LeastOneWord)
            LeastOneWord = ""

        if (WithoutWords is not False):
            WithoutWords = WithoutWords.strip()
            WithoutWords = WithoutWords.replace(" ", "+")
        else:
            WithoutWords = str(WithoutWords)
            WithoutWords = ""

        if (Author is not False):
            Author = Author.strip()
            Author = Author.replace(" ", "+")
        else:
            Author = str(AllWords)
            Author = ""

        if (Venue is not False):
            Venue = Venue.strip()
            Venue = Venue.replace(" ", "+")
        else:
            Venue = str(Venue)
            Venue = ""

        if (Occurence == 1):
            Occurence = "any"
        if (Occurence == 2):
            Occurence = "title"
        if (StartYear is True or EndYear is True):
            raise ValueError("Prohibited value of startyear/endyear")
        if (StartYear is not False):
            StartYear = StartYear.strip()
        else:
            StartYear = str(StartYear)
            StartYear = ""

        if (EndYear is not False):
            EndYear = EndYear.strip()
        else:
            EndYear = str(EndYear)
            EndYear = ""

        http_req = "http://scholar.google.cz/scholar?as_q=" + AllWords + \
            "&as_epq=" + \
            WithCorrectPhrase + "&as_oq=" + LeastOneWord + "&as_eq=" + \
            WithoutWords + \
            "&as_occt=" + Occurence + "&as_sauthors=" + \
            Author + "&as_publication=" + \
            Venue + \
            "&as_ylo=" + str(StartYear) + "&as_yhi=" + \
            str(EndYear) + "&btnG=&hl=cs&as_sdt=0%2C5"
    except:
        raise ValueError("Uncorrect value")

    return http_req


"""
    @param keywordsPhrase: Vyhladavacia fraza
    @return: Spravny vyparsovane url
"""


def sendUrlGoogle_BASIC(keywordsPhrase):
    http_req = ""
    response = ""
    try:
        keywordsPhrase = keywordsPhrase.strip()
        keywordsPhrase = keywordsPhrase.replace(" ", "+")
        http_req = "http://scholar.google.cz/scholar?hl=cs&q=" + \
            keywordsPhrase + "&btnG="
    except Exception:
        raise ValueError("Not String")

    return http_req
