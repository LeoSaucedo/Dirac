"""
Dirac bot.
Carlos Saucedo, David Risi, Liz Parra
2019
"""

import json
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
    # Google Translate integration.
    if(queryText.lower().startswith("translate")):
        return trans.translate(getRawText(queryText, "translate")).text

    # Checking for the Wolfram response.
    wolframResponse = wolframClient.ask(queryText)
    if(wolframResponse != False):
        return(wolframResponse)
    
    # Checking for the CleverBot response.
    cleverResponse = clever.ask(queryText)
    if(cleverResponse != False):
        return(cleverResponse)