sentiment-analyser
==================

A sentiment analysis tool for online data sources written in Python

This script takes a provided url, extracts all the textual data from it and compares all the words to lists of positive and negative words. The end result shows a percentage of words in the source data which are positive and negative in relation to the total number of matches (so the two percentages add up to 100%).

This is in no way intended to be accurate or to predict the actual sentiment of source data. Sentiment analysis is extremely complex and this tool is a simple experiment. The words included in the positive and negative lists are taken from http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

The following paper has more information with regards to these lists:

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
Proceedings of the ACM SIGKDD International Conference on Knowledge 
Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
Washington, USA

Usage
-----------

In order to use this script locally, Python as well as the Beautiful Soup library need to be installed. Future development plan involves hosting the tool online as a mini web application, so that no local installation is necessary (a possible host cadidate is Google App Engine).
