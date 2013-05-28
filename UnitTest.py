#!/usr/bin/python
import API_GoogleScholar_PEP8
import unittest
import sys
import string


class TestSequenceFunctions(unittest.TestCase):

    # testing BasicSearch

    # test should raise ValueError exception
    def test_exception1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = basicSearch(66)
        except:
            raised = True
        self.assertTrue(raised, 'Exception raised')

    # test should raise ValueError exception
    def test_exception2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = basicSearch(True)
        except:
            raised = True
        self.assertTrue(raised, 'Exception raised')

    # test searching phrase windows 
    def test_searching1(self):
        slovnik = dict()
        slovnik = basicSearch("windows")
        print slovnik
    # test searching multiple Phrase:windows linux sort Relevance

    def test_searching2(self):
        slovnik = dict()
        slovnik = basicSearch("windows linux")
        print slovnik
    # test  searching phrase "moj krasny fesacik" sort Relevance should have 6 results

    def test_searching3(self):
        slovnik = dict()
        slovnik = basicSearch("moj krasny fesacik")
        self.assertEqual(len(slovnik), 2)

    #
    # Testing ExtendedSearch
     # test should raise ValueError exception bad Value of Occurence 0 should be 1/2
    def test_exception_extend1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("Mojko vole",False,False,False,0,"Mnauky","Mnauky",False,"2000")
        except:
            raised = True
        self.assertTrue(raised, 'Exception raised')

    # test should raise ValueError exception bad Value of StartYear True - should be False or Num. Value
    def test_exception_extend2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("Mojko vole",False,False,False,2,"Mnauky","Mnauky",True,"2000")
        except:
            raised = True
        self.assertTrue(raised, 'Exception raised')
    # test should raise ValueError exception bad Value WithCorrectPhrase - True should be string phrase or False
    # should be false or numeric value)

    def test_exception_extend3(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("Mojko vole",True,False,False,2,"Mnauky","Mnauky",False,"2000")
        except:
            raised = True
        self.assertTrue(raised, 'Exception raised')

   #test f no results 0 items in dictionary
    def test_searching_extend1(self):
        slovnik = dict()
        slovnik = extendedSearch("Mojko vole","Mnauky","Mnauky","Mnauky",2,"Mnauky","Mnauky","1900","2000")
        self.assertEqual(len(slovnik), 0)
    
    
   
    #should have 2 results
    def test_searching_extend2(self):
        slovnik = dict()
        slovnik = extendedSearch("fesacik moj","fesacik",False,False,1,False,False,False,False)
        self.assertEqual(len(slovnik), 2)
   
    #test for complex search a lot of results
    def test_searching_extend3(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("windows","gates",False,False,1,False,False,"1200","2000")
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')



if __name__ == '__main__':
    unittest.main()
