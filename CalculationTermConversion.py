Conversions = {"multiplication": [" x ", "multiplied", "multiply", "times"],
               "subtraction": ["minus", "take away", "subtract"],
               "division": ["divide", "divided"]
               }
    
def applyConversion(string, conversiontype):  
    conversionOperator = ''
    if conversiontype == Conversions["multiplication"]: # checks what type of conversion it is
        conversionOperator = '*'
    elif conversiontype == Conversions["subtraction"]:
        conversionOperator = '-'
    elif conversiontype == Conversions["division"]:
        conversionOperator = '/'
        
    try:
        string = string.replace(conversiontype[0], conversionOperator)
        string = string.replace(conversiontype[1], conversionOperator)
        string = string.replace(conversiontype[2], conversionOperator) # In a try block as their may not be 3 values as is the case with division
    except:
        pass
    
    return string
