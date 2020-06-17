#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:21:03 2020

@author: tianlu
"""

import json
from difflib import get_close_matches

data = json.load(open("dictionaryData.json"))
formatData = {k.lower():v for k, v in data.items()}

dataKeys = formatData.keys()

def getResult(userInput):
    formateInput = userInput.lower()
    if formateInput in formatData:
        return formatData[formateInput]
    elif len(get_close_matches(formateInput, dataKeys))>0:
        closeMatch = get_close_matches(formateInput, dataKeys)[0]
        choice = input('did you mean %s instead ? Enter Y or N : ' % closeMatch)
        if choice.upper() == 'Y':
            return data[closeMatch]
        else:
            return "No matching word"
    else:
        return "No matching word"


word = input("Enter a word:")
results = getResult(word)
if type(results) == list:
    for result in results:
        print(result)
else:
    print(results)



