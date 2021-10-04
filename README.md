sentiment-analyser
==================

A sentiment analysis tool for online data sources written in Python

This script takes a provided URL, extracts all the textual data from it and compares all the words to lists of positive and negative words. The end result shows a percentage of words in the source data which are positive and negative in relation to the total number of matches (so the two percentages add up to 100%) and other statistics from the processed URL.

The only supported language is English. The original lists contained mostly American English spelling, so British equivalents have been added to them. Some words were taken out as they were deemed to make the list overly US-centric (these included the following entries: anti-american, anti-israeli, anti-us, anti-white).

This is in no way intended to be accurate or to predict the actual sentiment of source data. Sentiment analysis is a complex topic and this tool is a simple experiment. The words included in the positive and negative lists are taken from http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

The following paper has more information with regards to these lists:

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
Proceedings of the ACM SIGKDD International Conference on Knowledge 
Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
Washington, USA

Usage
-----------

An online version of the script is hosted on Google App Engine:

~~http://sentiment-analyser.appspot.com/~~ (app no longer available online because Google changed something in Google App Engine and I can't be bothered to investigate and fix it)

The script can also be run locally, just use local_analyser.py. In order to use this script locally, Python as well as the Beautiful Soup library need to be installed.