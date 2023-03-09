import json
import re
import random_responses


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)
    
response_data = load_json('intents.json')


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
        
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
                    
        if required_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1
                    
        score_list.append(response_score)
        
    best_response = max(score_list)
    response_index = score_list.index(best_response)
    
    if input_string == "":
        return "Please type something so we can chat :)"
    
    if best_response != 0:
        return responses_data[response_index]["bot_response"]
    
    return random_responses.random_string()
            
            
while True:
    user_input = input("You: ")
    print("Bot: ", get_response(user_input))













'''import random
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
    return result'''