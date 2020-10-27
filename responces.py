## = ok 
### = not ok
from operations import Operations
from datetime import datetime

class Commands:
    # simple starter/ender commands
    greetings = ["hello", "hey", "hi"]
    thankCom = ["thank", "thanks", "appriciate"]
    fairwells = ["bye", "see you later", "i'm out", "by", "buy", "cya"]
    smallTalkA = ["how", "how's", "hows", "whats", "what's"] # 2 part (A)
    smallTalkB = ["going", "you", "day", "today", "life", "up", "goes", "it", "doing"] # 2 part (B)
    smallTalkC = ["howdy", "whatsapp"] # Independant

    # appology command
    appologyCom = ["sorry", "appologise"]
    
    # timely command
    morningCom = ["morning", "goodmorning"]
    afternoonCom = ["afternoon", "goodafternoon"]
    nightCom = ["night", "goodnight"]

    # rude command
    rudeCom = ["retard", "stupid", "asshole", "useless", "worthless", "dumb", "shit", "ass", "go away", "trash", "fuck", "fuk", "idiot", "arsehole", "bitch", "s***", "f***", "cunt","c***"]

    # interactions
    question = ["what", "whats", "what's", "who", "whos", "who's", "when", "whens", "when's", "is", "how", "hows", "how's"] 
    confirm = ["yes", "yea", "yeah", "ya", "ok", "cool", "nice", "yep", "awesome", "sweet"] 
    unconfirm = ["no", "na", "nah", "nar", "dont", "don't", "not"] 
    goodCom = ["good", "well", "happy", "happier", "happiest", "great", "greatest", "fantastic", "extatic", "cheerful", "cheer", "delight", "delighted", "delightful", "ecstatic", "joyful", "joy", "lively", "wonderful", "grateful", "gleeful", "love", "lovely", "exciting", "excited", "elated", "best", "smile", "smiling", "smiled", "beautiful", "nice", "nicest", "nicely", "awesome", "awesomeness", "yay", "merry", "merrier", "perfect", "perfectly", "pleasant", "sprightful", "gratifying", "blessed", "bright", "chipper", "contented", "laughing", "glad", "jolly", "jubilant", "lively", "optimisitc", "overjoyed", "peaceful", "perky", "relieved", "thrilled", "upbeat", "blissful", "gleeful", "festive", "radiant", "pleased", "beaming", "mirthful", "playful", "tickled", "gay"]
    neutralCom = ["not bad", "im ok", "i'm ok", "alright", "fine", "neutral", "so so", "calm", "cool", "easy", "relaxed", "right", "agreed", "acceptable", "adequate", "standard", "par", "tolerable", "tolerably", "acceptably", "passable", "competent"]
    badCom = ["bad", "cry", "crying", "unhappy", "sad", "saddest", "depressed", "unstable", "miserable", "heartbroken", "died", "mournful", "distressed", "down", "hurt", "grief", "disappoint", "disappointed", "broke", "broken", "depressed", "lose", "lost", "waste", "wasted", "tear", "tearing", "torn", "tore", "low", "lowest", "lower", "worst", "worse", "ruin", "ruined", "defeated", "overwhelming", "unappreciated", "mourn", "mourning", "sorrow", "deprived", "rejected", "misery", "suicide", "suicidal", "disfunctional", "sadness", "dejected", "crushed", "crushing", "upset", "upsetting", "hateful", "sorrowful", "weepy", "displeased", "failure", "helpless", "insecure", "scared", "confused", "loser", "lonely", "panic", "impotent", "troubled", "inferior", "gloomy", "blue", "desperate", "downcast", "sombre", "wretched", "woeful", "forlorn", "melancholy", "bleak", "desolate", "dire", "disheartened", "disheartening", "dispirited", "distressed", "dreary", "heartbreaking", "moody", "joyless", "pessimistic", "pitiful", "pity", "somber", "wistful"]

    # casual conversation
    singCom = ["sing", "sings"]

    # informative
    creatorCom = ["creator", "created", "born", "made", "old"]
    nameCom = ["name"]
    purposeCom = ["purpose"]
    turtleCom = ["turtle", "turtles", "facts"]

    # fun
    drunkCom = ["drunk", "drink"]
    soberCom = ["sober", "normal"]

    # operational
    poop = ["poop", "poo"]
    weather = ["weather"]
    time = ["time"] 
    day = ["day"] 
    date = ["date"] 
    define = ["define"] 
    search = ["search"] 
    calculate = ["calculate"] 
    lock = ["lock"]
    hybernate = ["hybernate", "sleep", "hibernate"]
    shutdown = ["shutdown", "shut"] 
    abort = ["abort", "cancel"] 
    target = ["computer", "pc", "PC" "laptop", "system"]

    # mood
    moodAngry = ["retard", "angry", "furious", "hate", "anger", "heated", "mad", "outraged", "rage", "raging", "wrath", "wrathful", "frown", "yelling", "yell", "fury", "infuriating", "disgusted", "infuriated", "bash", "frustrated", "frustrating", "punch", "annoyed", "annoying", "bitter", "enraged", "irritable", "irritating", "irritated", "offended", "resentful", "sullen", "uptight", "crossed", "vexed", "tumultous", "riled", "fiery", "fuming", "ireful", "provoked", "provoking", "sulky", "maddened", "berserk", "antagonized", "ferocious", "fierce", "evil", "irked", "resent", "frenzied", "testy", "warpath", "aggravated", "snary", "ticked"]
    moodConfused = ["sure", "know"]

    # help
    helpCom = ["help"]
    

class Responses:
    # simple starter/ender responses
    greetings = ["Hello", "Hey", "Hi", "How's it going?"]
    thankResp = ["You're welcome", "Anytime", "Happy to help"]
    fairwells = ["Bye", "See you later", "Have a good day!"]
    smallTalk = ["I'm great, how are you?", "I'm quite well", "Not too bad thanks, and yourself?"]
    
    # forgiveness responses
    appologyResp = ["Apology accepted", "Ok, I will let you off this time"]

    # timely responses
    morningResp = ["Good Morning. Dont forget to drink your coffee"]
    afternoonResp = ["Good Afternoon"]
    nightResp = ["Good Night, Sleep tight"]

    # rude Responses
    rudeResp = ["That was very rude", "That was uncalled for", "Learn some manners"]

    # interactions
    unconfirmResp = ["Ok then", "Understood"] 
    okResp = ["Ok then", "Got it"] 
    goodResp = ["Thats good", "Im happy to hear that"]
    badResp = ["Oh no", "Im sorry to hear that"]

    # casual conversation
    singResp = ["Me? Sing? How about no"]
    
    # informative responses
    creatorResp = ["I was created on 20 Febuary 2020 by team jorge"] 
    nameResp = ["My name is SmartBot and I am your personal assistant"]
    purposeResp = ["My only purpose is to assist you"] 
    turtleFact = ["Turtles have existed for around 215 million years",
                  "It is estimated that only one out of 1,000 hatchlings survives to be an adult",
                  "All seven species of sea turtles are considered threatened or endangered",
                  "Turtles also have a lower shell called a plastron",
                  "Some sea turtles can live to over 50 years"] 

    #fun
    drunkResp = ["Let's party up", "party time"]
    soberResp = ["I'm not doing that again", "Oh what a nighttt"] # extra t's for exageration

    # operational
    weatherResp = ["The weather is " + Operations.getWeather() + " Degrees"]  
    dayResp = ["The day is " + datetime.now().strftime("%A")] 
    dateResp = ["The date is " + datetime.now().strftime("%d %B %Y")] 
    shutdownResp = ["The computer will shutdown in 15 seconds, say cancel to cancel the shutdown"] 
    abortResp = ["Shutdown has been cancelled"]

    #mood
    moodAnalysed = ["Neutral", "Happy", "Sad", "Angry", "Confused"]

    # help 
    helpResp = ["Try asking me some things listed below"]
    commandList = ["Hi", "Hows it going", "Good Morning", "Good Afternoon", "Good Night",
                   "When were you created", "Whats your name", "Whats your purpose",
                   "Sing for me", "Tell me facts about turtles", "Get drunk", "Get sober",
                   "Whats the weather", "Whats the time", "Whats the date",
                   "Search [phrase]", "Calculate [equation]",
                   "Lock computer", "Sleep computer", "Shutdown computer",
                   "Cancel shutdown", "bye"] 

    # unknown/no command responses
    unknownCommandResp = ["Perhaps I will be more intelligent in the future, but right now I am unable to answer that (Type help for a list of things you can ask me to do)",
             "Sorry, I don't understand (Type 'help' for a list of things you can ask me to do)",
             "Sorry, I don't know the answer to that question. (Type help for a list of things you can ask me to do)"]

    noCommandResp = ["Sorry I didn't catch that"]
