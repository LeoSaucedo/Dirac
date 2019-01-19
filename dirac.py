"""
Dirac bot.
Carlos Saucedo, David Risi, Liz Parra
2019
"""

import os, json, requests
import Mods.wolfram as wolfram
import Mods.CleverApi as cleverbot

with open("config.json","r") as h:
    config = json.load(h)

    """
    Generating bot objects.
    """
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

def ask(queryText):
    # Checking for the Wolfram response.
    wolframResponse = wolframClient.ask(queryText)
    if(wolframResponse != False):
        return(wolframResponse)
    
    # Checking for the CleverBot response.
    cleverResponse = clever.ask(queryText)
    if(cleverResponse != False):
        return(cleverResponse)