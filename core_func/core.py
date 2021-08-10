import json
import time
from difflib import SequenceMatcher
from selenium import webdriver
import spacy
from core_func.core_dict import core_dict

nlp = spacy.load('en_core_web_sm')
with open('C:\\Users\\Atishay\\Desktop\\Final year project\\final year project\\core_func\\intents.json') as file:
    intents = json.load(file)


def similarity(a: str, b: str):
    return SequenceMatcher(None, a, b).ratio()


def pattern_in_query(query: str):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if similarity(pattern, query) >= .8:
                return core_dict[intent['responses']](query)
            for word in query.split():
                if similarity(pattern, word) >= .9:
                    return core_dict[intent['responses']](query)


def exec_core(query: str):
    handle = pattern_in_query(query)

    if handle is None:
        return False
    
    if isinstance(handle, webdriver.Chrome):
        time.sleep(20)
        try:
            handle.quit()
        except:
            print('handle closed')
    
    return 'Redirecting'


if __name__ == '__main__':
    print(similarity('meetings', 'Any meetings today?'))