import WebScrapperWeather as rw
import WebScrapperDict as rd
import WordToDef as cw
import Calculations as calc
import CalculationTermConversion as calcConversions
import WordsAfterCom as arg
import SearchWeb as sw
import os
import subprocess
'''
This file makes all the classes/ functions from other files accesible in one
central file for easy access and clean code
'''

class Operations:
    @staticmethod
    def getWeather():
        weather = rw.returnWeather()
        return weather

    @staticmethod
    def wordToDefine(string):
        chosenWord = cw.checkForWord(string)
        return chosenWord
    
    @staticmethod
    def getDefinition(word):
        definition = rd.returnDefinition(word)
        return definition
    
    @staticmethod
    def commandArgs(string, term, addwhitespace=False):
        comArg = arg.checkCommandArgs(string, term, addwhitespace)
        return comArg

    @staticmethod
    def calcTermConversion(string, conversiontype):
        if conversiontype == 'multiplication':
            conversiontype = calcConversions.Conversions["multiplication"]
        elif conversiontype == 'subtraction':
            conversiontype = calcConversions.Conversions["subtraction"]
        elif conversiontype == 'division':
            conversiontype = calcConversions.Conversions["division"]
        converted = calcConversions.applyConversion(string, conversiontype)
        return converted

    @staticmethod
    def returnAnswer(equation):
        answer = calc.calculate(equation)
        return answer

    @staticmethod
    def returnSearch(phrase):
        sw.webSearch(phrase)
    
    @staticmethod
    def lock():
        subprocess.call('operations\lock.lnk', shell=True)
        
    @staticmethod
    def hybernate():
        subprocess.call("operations\hybernate.bat")

    @staticmethod
    def shutdown():
        subprocess.call("operations\shutdown20.bat")

    @staticmethod
    def abort():
        subprocess.call("operations\\abortshutdown.bat")
        
