import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from regex_search import searchExclude, searchText

def returnDefinition(term, url="https://www.dictionary.com/browse/"):
    try:
        url += term + "?s=t" # attaches the url with the term we want to define
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        definition = soup.find('div', attrs={'class':'css-kg6o37 e1q3nk1v3'})
        definition = str(definition)
        start = searchText('\(', definition, 1, True) # the definition is held after brackets/ankle brackets and before the closing brackets/ankle brackets
        end = searchText('\)', definition, 1, True)
        if len(start) > 0 and len(end) > 0: # Checks whether the definition is between brackets or ankle brackets
            definition = definition[start[0][1]:end[0][0]] # gets the definition from the string
        else:
            start = searchText('>', definition, 2, True) # since the definition isnt between brackets, its between ankle brackets
            end = searchText('<', definition, 3, True)
            definition = definition[start[1][1]:end[2][0]] # gets the definition from the string
    except:
        definition = "word not found" # if theres an error getting the definition or the word doesn't exist

    return definition


