import random
import math

class Literacy(object):

    def tip(self):
        price = int(random.random() * 26) + 15

        text = "You are a customer at a restaurant."
        text += "\nYou have finished your meal and your server hands you your check."
        text += "\nThe check totals to " + str(price) + "$, but you must add the tip."
        text += "\n\nHow was your server? (good, average, bad)"
        server = input(text)

        while (server != "good" and server != "average" and server != "bad"):
            server = input("-_- That wasn't an option.\nTry again.")
        if (server == "good"):
            percentTip = .20
        elif (server == "average"):
            percentTip = .15
        elif (server == "bad"):
            percentTip = .10

        text = "Since your server is " + str(server) + ",\n they should receive a " + str(percentTip * 100) + "% tip."
        text += "\n\nWhat is the tip, in dollars, that should be paid?"
        tip = input(text)
        correctTip = price * percentTip

        if(math.fabs(tip - correctTip) < .001):
            text = "That's correct!"
            text += "Good job, you should try another financial literacy challenge."
        else:
            text = "Sorry, that wasn't right."
            text += "Maybe you should try this financial literacy challenge over again."
        print(text)

    def interest(self):
        loan = (int(random.random() * 10) * 10000) + 90000
        compoundRate = (int(random.random() * 6) + 45) / 1000.0
        simpleRate = compoundRate + .02
        sPrice = loan * (1 + simpleRate * 30)
        cPrice = loan * math.pow(1 + simpleRate, 25)

        text = "You are in need of cash to buy your first house."
        text += "\nIn order to get the money to pay for the house quickly, you take out a " + str(loan) + "$ loan."
        text += "\n\nYou are given the option of two different types of loans:"
        text += "\nThe first loan has yearly simple interest for 30 years at a rate of " + str(simpleRate * 100) + "%."
        text += "\nThe second loan has yearly compound interest for 25 years, once a year, at a rate of " + str(compoundRate * 100) + "%."
        text += "\n\nWhich loan should you take? (simple[1] or compound[2]"
        choice = input(text)
        
        while ((choice > 2) or (choice < 1)):
            choice = input("That isn't a choice.\nTry again.")

        if(choice == 1):
            text = "\nThat's correct!\nBut, do you know why?"
        else:
            text = "\nWhile it's understandable why you chose that, it actually isn't correct."
            text +="\nHere's why:"
        
        text = "\nFor yearly simple interest, the interest is based on the original loan value."
        text += "\nThe formula for calculating this is: A = P + Prt"
        text += "\nWhere 'A' is the final value, 'P' is the loan value, and 'Prt' is the formula for the interest."
        text += "\n'r' is the yearly interest rate and 't' is the time in years after the loan was taken."
        text += "\nThis can be simplified to: A = P(1 + rt)"
        text += "\nGiven the values, the total price for the simple interest loan would be: " + str(sPrice)
        text += "\n\nFor yearly compound interest, the interest is based on the total loan value"
        text += "\nThe formula for calculating this is: A = P(1 + r/n)^(nt)"
        text += "\nThe only additional variable is n, which is the number of times compounded yearly."
        text += "\nGiven the values, the total price for the compound interest loan would be: " + str(cPrice)
        print(text)


        