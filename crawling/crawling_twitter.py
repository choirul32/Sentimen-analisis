# -*- coding: utf8 -*-
import re
import preprocessor as p
from string import punctuation
from collections import Counter
import csv
import tweepy
from tweepy import OAuthHandler

punctuation =  re.sub("-", "", punctuation)

filesentences = open("sentences_twitter.json", "a")

consumer_key = 'DmHd7uZy5Gr4g7trOOKqphuhW'
consumer_secret = 'Xfjg012XcljlbmoPOFW4Rxw7hwI77ol06DAHCztaf2nssdjxVZ'
access_token = '1951831687-aqX3J0MTGegdFQDdcRXiNUS8cN5dtWNWg9qOIAA'
access_secret = 't2ObeFAUqVTZBS5eFN27aYK6e9K1VVHX2OIgCv4FHoCRJ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    return dataset

filename = 'negatif.csv'
dataset = loadCsv(filename)

def cleanRT(s):
    return re.sub(r'^rt[\s]+', '', s, flags=re.MULTILINE) 

def punctuationSpacing(s):
	s = re.sub('([.,!?()])', r' \1 ', s)
	return re.sub('\s{2,}', ' ', s)

def remove_punctuation(s):
    for t in list(punctuation):
        s = s.replace(t,'')
    return cleanRT(s)

def saveTokensWithValue(mydict):
    for key, value in sorted(counts.items()):
        #filesave.write(item_ +': '+ str(mydict[item_])+'\n')
        value_ = str(value)
        filesave.write(key+'\n')

def saveSentences(sentences):
	for sentence in sentences:
		filesentences.write(sentence+'\n')


#crawling twitter sesuai pencarian di daftar list
def crawlingToSentencesFromList(dictionary):
	print("Crawling Twitter from list to Sentences......")
	sentences = []
	for index, wordlist in enumerate(dictionary, start=0):
		print(index)
		for status in tweepy.Cursor(api.search, q=wordlist[0],tweet_mode="extended", lang="in").items(10):
			text = p.clean(status.full_text.lower())
			text = punctuationSpacing(text)
			text = remove_punctuation(text)
			text = re.sub(r'[^\x00-\x7f]',r'', text)
			filesentences.write(text+'\n')
	#data = remove_duplicates(sentences)
	#saveSentences(data)

crawlingToSentencesFromList(dataset)


#crawlingToSentences()
#crawlingToTokens():
	# print (status.created_at, status.text)
	# csvWriter.writerow([status.created_at, status.text.encode('utf-8')])
