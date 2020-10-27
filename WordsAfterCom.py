def checkCommandArgs(string, command, addwhitespace=False):
    '''
    Returns any words after the command we use
    '''
    string = string.split()
    for i in range(len(string)):
        if string[i] == command:
            try:
                x = ""
                string = string[i+1:]
                for i in string: # puts the string back together 
                    x += i
                    if addwhitespace:
                        x+=" "
                string = x
                return string
            except:
                pass
            
