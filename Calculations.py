import regex_search

def calculate(equation):
    equation = regex_search.searchExclude('A-Za-z ', equation)  # remove all a-z from string
    g=""
    # x is a list now
    for i in equation: # combines all x list items into the string g (turns it into string again) 
        g += i  
    equation = g  # make x = g
    try:
        return(eval(equation))  # calculate an equation as a string
    except:
        return "Invalid operation"
