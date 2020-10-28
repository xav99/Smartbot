"""
Xavier pitsilos
20/02/2020
Smart bot
"""
import speech_recognition as sr
import random
import win32com.client as sapi
import os
from responces import Commands, Responses
from datetime import datetime
from operations import Operations

commands = {"greetings": Commands.greetings,
            "fairwells": Commands.fairwells,
            "thankCom": Commands.thankCom,
            "convA": Commands.smallTalkA,
            "convB": Commands.smallTalkB,
            "convC": Commands.smallTalkC,
            "appologyCom": Commands.appologyCom,
            "morningCom": Commands.morningCom,
            "afternoonCom": Commands.afternoonCom,
            "nightCom": Commands.nightCom,
            "rudeCom": Commands.rudeCom,
            "singCom": Commands.singCom,
            "creatorCom": Commands.creatorCom,
            "nameCom": Commands.nameCom,
            "purposeCom": Commands.purposeCom,
            "turtleCom": Commands.turtleCom,
            "drunkCom": Commands.drunkCom,
            "soberCom": Commands.soberCom,
            "goodCom": Commands.goodCom,
            "neutralCom": Commands.neutralCom,
            "badCom": Commands.badCom,
            "weather": Commands.weather,
            "define": Commands.define,
            "search": Commands.search,
            "calculate": Commands.calculate,
            "time": Commands.time,
            "day": Commands.day,
            "date": Commands.date,
            "lock": Commands.lock,
            "hybernate": Commands.hybernate,
            "shutdown": Commands.shutdown,
            "abort": Commands.abort,
            "target": Commands.target,
            "confirm": Commands.confirm,
            "unconfirm": Commands.unconfirm,
            "poop": Commands.poop,
            "question": Commands.question,
            "angry": Commands.moodAngry,
            "confused": Commands.moodConfused,
            "help": Commands.helpCom
            }

responses = {"greetings": Responses.greetings,
             "fairwells": Responses.fairwells,
             "thankResp": Responses.thankResp,
             "conv": Responses.smallTalk,
             "appologyResp": Responses.appologyResp,
             "morningResp": Responses.morningResp,
             "afternoonResp": Responses.afternoonResp,
             "nightResp": Responses.nightResp,
             "rudeResp": Responses.rudeResp,
             "singResp": Responses.singResp,
             "creatorResp": Responses.creatorResp,
             "nameResp": Responses.nameResp,
             "purposeResp": Responses.purposeResp,
             "turtleResp": Responses.turtleFact,
             "drunkResp": Responses.drunkResp,
             "soberResp": Responses.soberResp,
             "goodResp": Responses.goodResp,
             "neutralResp": Responses.okResp,
             "badResp": Responses.badResp,
             "weatherResp": Responses.weatherResp,
             "dayResp": Responses.dayResp,
             "dateResp": Responses.dateResp,
             "shutdownResp": Responses.shutdownResp,
             "abortResp": Responses.abortResp,
             "unconfirmResp": Responses.unconfirmResp,
             "okResp": Responses.okResp,
             "moodAnalysed": Responses.moodAnalysed,
             "helpResp": Responses.helpResp,
             "commandList": Responses.commandList,
             "unknown": Responses.unknownCommandResp,
             "noCommandResp": Responses.noCommandResp
             }

specialResponse = None  # special response is one chosen in exclusive functions
previousSpeech = ""
botsResponse = ""
moodNotSpecified = True

def multipartConv(a, b, resp=[""], func=None, moodarg=None):
    '''
    2 parts must be present in a conversation (a and b)
    '''
    global botsResponse
    A = inConv(a)  
    B = inConv(b)
    if len(A) > 0 and len(B) > 0:
        specialResponse = random.choice(resp) # if theres only 1 choice it will return that choice anyway
        botsResponse = specialResponse
        speak.Speak(specialResponse)
        specialResponse = None
        if func is not None:
            func()
        if moodarg is not None:
            global mood, moodNotSpecified
            mood = moodarg
            print('Mood:',mood)
            moodNotSpecified = False
        
def excludeInConv(exclude, include, resp, moodarg=None):
    '''
    checks if the strings in exclude aren't in the string,
    and the strings in include are in the string
    '''
    global botsResponse
    A = inConv(exclude) # to exclude or include multiple lists use the + operator to join the lists
    B = inConv(include)
    if len(A) == 0 and len(B) > 0:
        specialResponse = random.choice(resp)
        botsResponse = specialResponse
        speak.Speak(specialResponse)
        if moodarg is not None:
            global mood, moodNotSpecified
            mood = moodarg
            print('Mood:',mood)
            moodNotSpecified = False


def drunkify():
    '''
    Changes speak rate to slowest
    '''
    speak.Rate = -10

def normal():
    '''
    Changes speak rate back to normal
    '''
    speak.Rate = 0

def faster():
    '''
    Changes speak rate back to normal
    '''
    speak.Rate = 2

def prevSpeech():
    return str(previousSpeech), str(botsResponse), str(mood)
        
rec = sr.Recognizer()
speak = sapi.Dispatch("SAPI.SpVoice")        

def launcher():
    global inConv
    global previousSpeech
    global botsResponse
    global moodNotSpecified
    global mood
    mood = responses["moodAnalysed"][0] # mood starts at and resets to neutral
    if moodNotSpecified:
        print("Mood:", mood)
    moodNotSpecified = True
    with sr.Microphone() as source:        
        rec.adjust_for_ambient_noise(source, duration=1)
        #print("Say 'help' for a list of commands")
              
        audio = rec.listen(source)
        
        try:
            #rec.energy_threshold = 30  # Makes the microphone more sensitive
            text = rec.recognize_google(audio)
            text = text.lower()
            inConv = lambda x: [i for i in text.split() if i in x] # Returns any string matches in a list
            
            for i in text.split(): # checks for single keywords
                if i in commands["angry"]: # checking for angry mood
                    mood = responses["moodAnalysed"][3]
                    print("Mood:", mood)
                    moodNotSpecified = False
                if i in commands["greetings"]:
                    botsResponse = random.choice(responses["greetings"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["fairwells"]:
                    botsResponse = random.choice(responses["fairwells"])
                    speak.Speak(botsResponse)
                    exit()
                    break
                elif i in commands["thankCom"]:
                    botsResponse = random.choice(responses["thankResp"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["appologyCom"]:
                    botsResponse = random.choice(responses["appologyResp"])
                    speak.Speak(botsResponse)
                    mood = responses["moodAnalysed"][0]
                    print("Mood:", mood)
                    moodNotSpecified = False
                    break
                elif i in commands["convC"]:
                    botsResponse = random.choice(responses["conv"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["rudeCom"]:
                    botsResponse = random.choice(responses["rudeResp"])
                    speak.Speak(botsResponse)
                    mood = responses["moodAnalysed"][3]
                    print("Mood:", mood)
                    moodNotSpecified = False
                    break
                elif i in commands["neutralCom"]:
                    botsResponse = random.choice(responses["neutralResp"])
                    speak.Speak(botsResponse)
                    mood = responses["moodAnalysed"][0]
                    mood = responses["moodAnalysed"][0]
                    print("Mood:", mood)
                    break
                elif i in commands["turtleCom"]:
                    botsResponse = random.choice(responses["turtleResp"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["drunkCom"]:
                    botsResponse = random.choice(responses["drunkResp"])
                    speak.Speak(botsResponse)
                    drunkify()
                    break
                elif i in commands["soberCom"]:
                    normal()
                    botsResponse = random.choice(responses["soberResp"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["define"]:
                    term = Operations.wordToDefine(text)
                    botsResponse = Operations.getDefinition(term)
                    speak.Speak(botsResponse)
                    break
                elif i in commands["calculate"]:
                    calculation = Operations.commandArgs(text, "calculate", True)
                    calculation = Operations.calcTermConversion(calculation, "multiplication")
                    calculation = Operations.calcTermConversion(calculation, "subtraction")
                    calculation = Operations.calcTermConversion(calculation, "division")
                    botsResponse = Operations.returnAnswer(calculation)
                    speak.Speak(botsResponse)
                    break
                elif i in commands["search"]:
                    phrase = Operations.commandArgs(text, "search", True)
                    Operations.returnSearch(phrase)
                    #breakTwice = True
                    break
                elif i in commands["abort"]:
                    botsResponse = random.choice(responses["abortResp"])
                    speak.Speak(botsResponse)
                    Operations.abort()
                    break
                elif i in commands["confirm"]:
                    botsResponse = random.choice(responses["okResp"])
                    speak.Speak(botsResponse)
                    break
                elif i in commands["poop"]:
                    mood = "poop"
                    break
                elif i in commands["help"]:
                    botsResponse = random.choice(responses["helpResp"])
                    speak.Speak(botsResponse)
                    #botsResponse = responses["commandList"]
                    os.system("start operations\help.txt")
                    break
            
            #checks for multiple keywords
            multipartConv(commands["convA"], commands["convB"], responses["conv"])
            multipartConv(commands["question"], commands["creatorCom"], responses["creatorResp"])
            multipartConv(commands["question"], commands["nameCom"], responses["nameResp"])
            multipartConv(commands["question"], commands["purposeCom"], responses["purposeResp"])
            multipartConv(commands["unconfirm"], commands["goodCom"], responses["badResp"], moodarg=responses["moodAnalysed"][2]) # not good
            multipartConv(commands["unconfirm"], commands["angry"], responses["badResp"], moodarg=responses["moodAnalysed"][0]) # not angry
            multipartConv(commands["question"], commands["weather"], responses["weatherResp"])
            #multipartConv(commands["question"], commands["day"], responses["dayResp"])
            multipartConv(commands["question"], commands["date"], responses["dateResp"])
            multipartConv(commands["question"], commands["time"], [datetime.now().strftime("%I %M %p") if not datetime.now().strftime("%I %M %p").startswith("0") else datetime.now().strftime("%I%M %p")[1:]]) # gets the time in 12 hr format with the AM/PM at the end without starting with saying '0'
            multipartConv(commands["lock"], commands["target"], func=Operations.lock)
            multipartConv(commands["hybernate"], commands["target"], func=Operations.hybernate)
            multipartConv(commands["shutdown"], commands["target"], responses["shutdownResp"], func=Operations.shutdown)
            multipartConv(commands["abort"], commands["target"]) # no response since we already have the response and action in singlepart command
            multipartConv(commands["unconfirm"], commands["confused"], moodarg=responses["moodAnalysed"][4]) #checking for confused mood
            
            # ensures certain words are included and excluded 
            excludeInConv(commands["question"], commands["morningCom"], responses["morningResp"])
            excludeInConv(commands["question"], commands["afternoonCom"], responses["afternoonResp"])
            excludeInConv(commands["question"], commands["nightCom"], responses["nightResp"])
            excludeInConv(commands["unconfirm"]+commands["morningCom"], commands["goodCom"], responses["goodResp"], moodarg=responses["moodAnalysed"][1]) # good
            excludeInConv(commands["unconfirm"], commands["badCom"], responses["badResp"], moodarg=responses["moodAnalysed"][2]) # not good
            excludeInConv(commands["goodCom"], commands["unconfirm"], responses["unconfirmResp"])
            excludeInConv(commands["question"], commands["singCom"], responses["singResp"])
            excludeInConv(["how", "hows", "how's"], commands["day"], responses["dayResp"])
            
            vali = False  # Checks for invalid commands, and responds with an error if the command is invalid
            for k, v in commands.items():
                for x in text.split():
                    if x in v:
                        vali = True
            if text == "":
                vali = True # If theres no command, we want to respond with noCommandResp, not unknown

            if not vali:
                faster()
                botsResponse = random.choice(responses["unknown"])
                speak.Speak(botsResponse)
                normal()
            try:
                previousSpeech = text
            except:
                previousSpeech = ""
                
                    
        
        except:
            botsResponse = random.choice(responses["noCommandResp"])
            speak.Speak(botsResponse)  # if no speech has been said
            #pass


