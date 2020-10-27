def checkForWord(string):
    '''
    Checks for the word we want to define by looking for the 'define' keyword in
    the string
    '''
    string = string.split()
    for i in range(len(string)):
        if string[i] == "define":
            try:
                return string[i+1]
            except:
                pass
            
