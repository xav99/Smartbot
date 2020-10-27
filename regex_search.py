import re

noNumbers = lambda x: re.findall("[^0-9 ]", x)  # excludes whitespace char
noLetters = lambda x : re.findall("[^A-Za-z ]", x)  # excludes whitespace char
#numberRange = lambda x: re.findall("[0-5][0-9]", x)

def searchText(searchterm, text, maxoccurence=1, suppress=False):
    """
    Searches the text for a match
    
    :param searchterm: The term to search the text for
        options:
            '[A-Z]': Exclude all characters A to Z with capital letters
            '[a-z]': Exclude all characters a to z with lowercase letters
            '[0-9]': Exclude all numbers 0 to 9
            custom term: Any character(s) used as the parameter in excludeterm
    :param text: The text to search through
    :param maxoccurence: The maximum amount of times you want a match to be
                         printed
        example:
            if 2 is specified, it will only alert you if 2 or less matches of
            the searchterm were found in the text. Even if 5 matches were in the
            text you will only be alerted of a maximum of 2

            if "all" is specified, it will print all occurences of the
            searchterm in the text
    """
    pos = []
    if maxoccurence == "all":
        for match in re.finditer(searchterm, text):
            if not suppress:
                print("word: " + '"' + searchterm + '"' + " found at", match.span())
            pos.append(match.span())
    else:
        if maxoccurence >= 1:
            count = 0
            for match in re.finditer(searchterm, text):
                if not suppress:
                    print("word: " + '"' + searchterm + '"' + " found at", match.span())
                count += 1
                pos.append(match.span())
                if count == maxoccurence:
                    break
            if count == 0:
                if not suppress:
                    print("word not found")
        else:
            if not suppress:
                print("word not found")
    return pos

def searchExclude(excludeterm, text):
    """
    Searches the text and returns all characters in the text except for the
    exclude term
    
    :param excludeterm: The term to exclude from being returned
        example:
            if your exclude term is abc, it will return any characters in the
            text that aren't 'a' 'b' or 'c'
        options:
            'A-Z': Exclude all characters A to Z with capital letters
            'a-z': Exclude all characters a to z with lowercase letters
            '0-9': Exclude all numbers 0 to 9
            custom term: Any character(s) used as the parameter in excludeterm
    :param text: the text to search through
    """
    x = re.findall("[^" + excludeterm + "]", text)
    #print(x)
    return x

'''
print(noNumbers("hello there"))
print(noLetters("hey 123"))
#print(numberRange("61"))

searchText("[a-z]", "abc xd abc abc abc ", 6)
searchExclude("abc", "abbbcbcbbd")
'''
