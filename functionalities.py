import random
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


#return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bag_of_words(sentence, words, show_details=True):
    #tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    #bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                #assign 1 if current word is in the vocabulary position
                bag[i] = 1
    return np.array(bag)


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result