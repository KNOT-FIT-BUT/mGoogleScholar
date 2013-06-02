#!/usr/bin/env python
from Scholar import BasicSearch
from Scholar import ExtendedSearch
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
            slovnik = BasicSearch(66)
        except:
            raised = True
        self.assertEquals(raised, True)

    # test should raise ValueError exception
    def test_exception2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = BasicSearch(True)
        except:
            raised = True
        self.assertEquals(raised, True)

    # test searching phrase windows
    def test_searching1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = BasicSearch("windows")
        except:
            raised=True
        self.assertEquals(raised, False)
    # test searching multiple Phrase:windows linux sort Relevance

    def test_searching2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = BasicSearch("windows linux")
        except:
            raised = True
        self.assertEquals(raised, False)
    # test  searching phrase "moj krasny fesacik" sort Relevance should have 6
    # results

    def test_searching3(self):
        slovnik = dict()
        slovnik = BasicSearch("moj krasny fesacik")
        self.assertEquals(len(slovnik), 2)

    #
    # Testing ExtendedSearch
     # test should raise ValueError exception bad Value of Occurence 0 should
     # be 1/2
    def test_exception_extend1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = ExtendedSearch(
                "Mojko vole", False, False, False, 0, "Mnauky", "Mnauky", False, "2000")
        except:
            raised = True
        self.assertEquals(raised, True)

    # test should raise ValueError exception bad Value of StartYear True -
    # should be False or Num. Value
    def test_exception_extend2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = ExtendedSearch(
                "Mojko vole", False, False, False, 2, "Mnauky", "Mnauky", True, "2000")
        except:
            raised = True
        self.assertEquals(raised, True)
    # test should raise ValueError exception bad Value WithCorrectPhrase - True should be string phrase or False
    # should be false or numeric value)

    def test_exception_extend3(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = ExtendedSearch(
                "Mojko vole", True, False, False, 2, "Mnauky", "Mnauky", False, "2000")
        except:
            raised = True
        self.assertEquals(raised, True)

   # test f no results 0 items in dictionary
    def test_searching_extend1(self):
        slovnik = dict()
        slovnik = ExtendedSearch(
            "Mojko vole", "Mnauky", "Mnauky", "Mnauky", 2, "Mnauky", "Mnauky", "1900", "2000")
        self.assertEquals(len(slovnik), 0)

    # should have 2 results
    def test_searching_extend2(self):
        slovnik = dict()
        slovnik = ExtendedSearch(
            "fesacik moj", "fesacik", False, False, 1, False, False, False, False)
        self.assertEquals(len(slovnik), 2)

    # test for complex search a lot of results
    def test_searching_extend3(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = ExtendedSearch(
                "windows", "gates", False, False, 1, False, False, "1200", "2000")
        except:
            raised = True
        self.assertEquals(raised, False)


if __name__ == '__main__':
    unittest.main()
