#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib
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
source = "http://example.com"
url = urllib.urlopen(source)
htmlSource = url.read()
url.close()
soup = BeautifulSoup(htmlSource)

# remove additional tags
[s.extract() for s in soup(["script", "style"])]

processedSoup = soup.get_text()
decodedSoup = processedSoup.encode("utf-8")

# create a list with all words from the text
words = decodedSoup.split()

### compare the list of retrieved words with the positive and negative lists 
def comp(list1, list2):
	numMatches = 0
	for val in list1:
		if val in list2:
			numMatches += 1
	return numMatches

positiveMatches = comp(words, positiveWords)
negativeMatches = comp(words, negativeWords)
totalMatches = positiveMatches + negativeMatches
positivePercentage = (positiveMatches / float(totalMatches)) * 100
negativePercentage = (negativeMatches / float(totalMatches)) * 100

print "Positive words contained: " + str(round(positivePercentage, 2)) + "%"
print "Negative words contained: " + str(round(negativePercentage, 2)) + "%"
print "Total terms: " + str(totalMatches) + " Positive terms: " + str(positiveMatches) + " Negative terms: " + str(negativeMatches)