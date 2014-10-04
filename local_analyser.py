#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib2
from bs4 import BeautifulSoup

### retrieve and save lists of positive and negative words ###
def getWords(fileName):
	wordList = []
	with open(fileName) as inputfile:
		for row in csv.reader(inputfile):
			term = ''.join(row)
			wordList.append(term)
		return wordList

positiveWords = getWords("positive-words.txt")
negativeWords = getWords("negative-words.txt")

### retrieve list of words from html document ###
# set the url
source = "http://www.example.com"
url = urllib2.urlopen(source)
htmlSource = url.read()
url.close()
soup = BeautifulSoup(htmlSource)

# remove additional tags
[s.extract() for s in soup(["script", "style"])]

processedSoup = soup.get_text()
decodedSoup = processedSoup.encode("utf-8")

# convert all words to lower case (to match the words in lists)
decodedSoup = decodedSoup.lower()

# create a list with all words from the text
words = decodedSoup.split()

### compare the list of retrieved words with the positive and negative lists 
def comp(list1, list2):
	matchList = []
	for val in list1:
		if val in list2:
			matchList.append(val)
	return matchList

positiveMatches = comp(words, positiveWords)
numPositiveMatches = len(positiveMatches)
negativeMatches = comp(words, negativeWords)
numNegativeMatches = len(negativeMatches)

totalMatches = numPositiveMatches + numNegativeMatches
positivePercentage = (numPositiveMatches / float(totalMatches)) * 100
negativePercentage = (numNegativeMatches / float(totalMatches)) * 100

print "Positive words contained: " + str(round(positivePercentage, 2)) + "%"
print "Negative words contained: " + str(round(negativePercentage, 2)) + "%"
print "Total terms: " + str(totalMatches) + " Positive terms: " + str(numPositiveMatches) + " Negative terms: " + str(numNegativeMatches)
print
print "Full list of positive words: " + str(positiveMatches)
print "Full list of negative words: " + str(negativeMatches)