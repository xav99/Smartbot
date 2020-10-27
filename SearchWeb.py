import webbrowser

def webSearch(phrase, browser="chrome"):
    '''
    Search the web with chosen phrase
    '''
    #webbrowser.open(browser, new=0, autoraise=True)
    try:
        webbrowser.open_new_tab("https://www.google.com.au/search?q=" + phrase)
    except:
        print('Chrome was not found, please install chrome to search the web')
            
