"""
Dirac bot.
Carlos Saucedo, David Risi, Liz Parra
2019
"""

import json, os, dwollav2
import Mods.wolfram as wolfram
import Mods.CleverApi as cleverbot
from googletrans import Translator

finlit = False

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
    # FinLit module.
    if(queryText.lower().includes("play")):
        response = "Want to play some of my financial games?"
        response += "\nWhich one? Tip Game or Interest game?"
        return response
    elif(queryText.lower().includes("tip")):
        # Tip game
        response = "Great! Here's the Tip Game: "
        return response
    elif(queryText.lower().includes("interest")):
        # Interest game
        response = "Great! Here's the Interest Game:"
    
    # PayPal.me integration.
    elif(queryText.lower().startswith("pay")):
        rawInput = (getRawText(queryText, "pay")).replace("$", "").split
        return("https://paypal.me/" + rawInput[1] + "/" + rawInput[2])
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