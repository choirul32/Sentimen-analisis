#This program takes a training set of sentiment manually classified sentiment (1,0,-1)
#and uses a Naive Bayes Classifier to determine the sentiment of other tweets.
#Input: Training set of Tweets, Tweets that need Sentiment Analysis
#Output: Predicted Sentiment of Tweets in text file
import nltk
import csv


def openText(name):
    file = open(name, encoding="utf-8")
    sentences = []
    for line in file.read().splitlines():
        words = line.split()
        sentences.append(words)
    return sentences
#define cleaning functions for training set
def get_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words
    
def take_features(document):
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document)
    return features

# Load Training set into array
file_negatif = openText('sentences_negatif.txt')
file_positif = openText('sentences_positif.txt')

#clean tweets
tweets = []

for words in file_positif:
    tweets.append((words, 1))


for words in file_negatif:
    tweets.append((words, 0))

print(tweets)
word_features = get_features(get_tweets(tweets))

#build training sets using word_features
training_set = nltk.classify.apply_features(take_features, tweets)

#build classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
classifier.show_most_informative_features()
while True:
    tweet = str(input("masukan sentimen : "))
    print(classifier.classify(take_features(tweet.split())))
    


#raw output can be analyzed in whatever software you desire since its written to a text file. 






	
	
    




