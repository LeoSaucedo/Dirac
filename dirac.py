"""
Dirac bot.
Carlos Saucedo, David Risi
2019
"""

import json, os
import Mods.wolfram as wolfram
import Mods.CleverApi as cleverbot
from googletrans import Translator
    
with open("config.json","r") as h:
    config = json.load(h)

    """
    Generating bot objects.
    """
    # Google Translate
    trans = Translator()
    
    # Wolfram
    try:
        wolframClient = wolfram.Client(config["wolfram"]["appId"])
    except Exception as authError:
        print("Failed to instantiate Wolfram.")
    
    # CleverBot
    try:
        clever = cleverbot.Bot(config["cleverbot"]["apiUser"], config["cleverbot"]["apiKey"])
    except Exception as e:
        print("Failed to instantiate CleverBot.")

def getRawText(text, command):
    # Returns the raw text.
    return text.replace(command + " ", "")

def ask(queryText):
    """
    Ask function. Returns the created
    response using a variety
    of APIs.
    """
    # Help function.
    if(queryText.lower().startswith("help")):
        out = "I can help you with many things:\n"
        out += "1. Find your nearest ATM\n"
        out += "2. Pay your friends on Paypal.Me\n"
        out += "3. Practice financial literacy\n"
        out += "4. Get help. I'm here to talk <3\n"
        out += "5. General knowledge questions about the world (yes, even your math homework!)\n"
        return out
    
    # PayPal.me integration.
    elif(queryText.lower().startswith("pay") or queryText.lower().startswith("give")):
        queryText = queryText.lower().replace("$", "").split()
        parsedLink = "https://paypal.me/" + str(queryText[1]) + "/" + str(queryText[2])
        return(parsedLink)
    elif(queryText.lower().startswith("atm")):
        return "https://www.google.com/maps/search/ATM/"
    # Google Translate integration.
    elif(queryText.lower().startswith("translate")):
        return trans.translate(getRawText(queryText, "translate")).text

    # OwO
    elif(queryText.lower().startswith("owo")):
        translatedText = queryText.replace("r", "w")
        translatedText = translatedText.replace("l", "w")
        translatedText = translatedText.replace("n", "nya")
        translatedText = translatedText.replace("nyanya", "nya")
        translatedText += " desu~"
        return translatedText

    # Checking for the Wolfram response.
    try:
        wolframResponse = wolframClient.ask(queryText)
        if(wolframResponse != False):
            return(wolframResponse)
    except:
        print("Wolfram error.")
    # Checking for the CleverBot response.
    try:
        cleverResponse = clever.ask(queryText)
        if(cleverResponse != False):
            return(cleverResponse)
    except:
        print("CleverBot error.")