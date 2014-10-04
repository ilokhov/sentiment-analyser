#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib2
import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup

def analyse(input_url):

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
	source = input_url

	# check if the input has http or https, if not then insert http
	httpCheck = ['http', 'https']
	if not any(x in source for x in httpCheck):
		source_http = "http://" + source
	else:
		source_http = source

	# test if the url exists/works, return an error if not
	try:
	    urllib2.urlopen(source_http)
	except ValueError, ex:
	    return 0, str(ex)
	except urllib2.HTTPError, ex:
	    return 0, str(ex)
	except urllib2.URLError, ex:
	    return 0, str(ex)
	except Exception, ex:
	    return 0, str(ex)

	url = urllib2.urlopen(source_http)
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

	# check if there are any matches at all
	# matches exist
	if totalMatches > 0:
		positivePercentage = (numPositiveMatches / float(totalMatches)) * 100
		negativePercentage = (numNegativeMatches / float(totalMatches)) * 100

		# construct output
		mainOutput = [str(round(positivePercentage, 2)), str(round(negativePercentage, 2)), str(totalMatches), str(numPositiveMatches), str(numNegativeMatches), str(positiveMatches), str(negativeMatches)]

	# zero matches
	else:
		return 0, "No matches found in the submitted URL"

	return 1, mainOutput