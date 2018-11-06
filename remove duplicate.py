import re
import preprocessor as p
from string import punctuation
from collections import Counter
import csv
import tweepy
from tweepy import OAuthHandler

filesentences = open("sentences.json", "a")

def remove_duplicates(values):
    output = []
    for value in values:
        if value not in output:
            output.append(value)
    return output

def openTextSave(name):
	file = open(name, encoding="utf-8")
	sentences = []
	for line in file.read().splitlines():
		words = line.split()
		sentences.append(words)
	return sentences

def saveSentences(sentences):
	for sentence in sentences:
		filesentences.write(str(sentence))

sentences_ = open("sentences_twitter.json", encoding="utf-8")
sentences_clean = remove_duplicates(sentences_)
saveSentences(sentences_clean)
