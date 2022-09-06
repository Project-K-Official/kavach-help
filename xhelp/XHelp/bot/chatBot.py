import os
import sys

from pathlib import Path

sys.path.append(
   os.path.abspath(
      Path(__file__).resolve().parent.parent.parent
   )
)

import XHelp as App

import random
import json
# import torch

class ChatBot:
   responseHandler = None

   device = None
   model = None
   intents = None
   data = None

   reportActive = None
   reportMessages = None

   def start (responseHandler):
      ChatBot.responseHandler = responseHandler
      ChatBot.reportActive = False
      ChatBot.reportMessages = ''

   def reset ():
      App.Configuration.SESSION_ID += 1

   def sendResponse (message):
      original_message = str(message).strip()
      Output(message)
      return None

Greet_patterns= ["HI","HEY","HOW ARE YOU","IS ANYONE THERE?","HELLO","GOOD DAY"]
Greet_responses=["Hey :-)","Hello ","Hi there, what can I do for you?","Hi there", "how can I help?"]

Adios_patterns=["BYE","SEE YOU LATER","GOODBYE","GOOD NIGHT"]
Adios_responses= ["See you later","Have a nice day","Bye!"]

Gratitude_patterns=["THANKS","THANK YOU","THANK'S A LOT!"]
Gratitude_responses=["Happy to help!","Any time!","My pleasure","Most welcome"]

report_patterns=["I WANT TO REPORT","REPORT","HELP","I AM FACING ISSUE.","CYBER BULLYING","HARASSMENT.","CREEPY MESSAGE","BULLYING","DISTURBING.","TROUBLING"]
report_responses=["Please go ahead and give more details.","Tell us your issue. We will surely help.","Could you please share some more information regarding it"]

bullying_patterns=["VIOLENT BEHAVIOR","ABUSIVE","HATEFUL","FOUL LANGUAGE","BAD WORDS","BULLY","BULLYING","1","1 - to report cyber bullying related issues"]
bullying_responses=["->Please inform your parents.\n->Stop responding to such texts or emails.\n->You can try to get support from cybercrime.gov.in website.\n->Avoid or ignore as much as possible.\n->If possible, please block the source."]

Spam_patterns=["I HAVE BEEN SPAMMING","SPAMMING","SPAM","SPAMMED","I WANT TO REPORT SPAMMING","2","2 - to report Spamming realted isues"]
Spam_responses= ["Please specify by typing:\nA - for SPAM ADS\nB - for SPAMS TEXTS/EMAILS"]

spam2_patterns=["A","SPAM ADS","ADS","ADVERTISEMENT"]
spam2_responses=["->Please do not visit spamming websites.\n->If possible enable Ad block.\n->Also block the notifications of alike websites."]
##EMAILS
spam3_patterns=["B","SPAM TEXTS","MESSAGES","DMS","TEXT","EMAIL","SPAM EMAIL","SPAM EMAILS"]
spam3_responses=["->Report it on the messaging/mail app you use.Look for the option to report junk or spam.\n->Otherwise you can Copy the message and forward it to 7726 (SPAM).\n->If still it goes thn you can directly Report it to the Federal Trade Commission at ReportFraud.ftc.gov."]

Actions_patterns=["BLOCK","MORE HELP","TAKE ACTION","DO SOMETHING"]
Actions_responses=["we will do our best to look up on this matter and help you.","Necessary actions will be taken as soon as possible. Worry not"]

end_patterns=["SUBMIT","OK","YES","DONE","SURELY","LINK","INSTAGRAM","WHATSAPP","FACEBBOOK","EVIDENCE"]
end_responses=["Noting it down. Your report will be submitted."]

#Helpline response
helpline_patterns = ["kill", "suicide", "die", "murder", "knife", "gun"]
helpline_response = ["We recommend you to contact national helpline number at: 1098"]


import random
def rand(n):
    num = random.randint(0,n-1)
    return num

finish_text="\n\nIf done, Please type 'submit'. Otherwise please continue and Type:\n1 - to report cyber bullying related issues\n2 - to report Spamming realted isues."


def Output(user):

    if(user in'Aa'):
        ChatBot.reportMessages+='\n'
        ChatBot.reportMessages+= "SPAM ADS"

    elif(user in'Bb'):
        ChatBot.reportMessages+='\n'
        ChatBot.reportMessages+= "SPAM TEXTS/EMAILS"

    elif(user=='2'):
        ChatBot.reportMessages+='\n'
        ChatBot.reportMessages+= "report Spamming realted isues"

    elif(user=='1'):
        ChatBot.reportMessages+='\n'
        ChatBot.reportMessages+= "report cyber bullying related issues"

    else:
        ChatBot.reportMessages+='\n'
        ChatBot.reportMessages+= user

    user=user.upper()


    if user in Greet_patterns:
        i=rand(len(Gratitude_responses))
        Send_Output(Greet_responses[i])


    elif user in Adios_patterns:
        i=rand(len(Adios_responses))
        Send_Output(Adios_responses[i]+finish_text)


    elif user in Gratitude_patterns:
        i=rand(len(Gratitude_responses))
        Send_Output(Gratitude_responses[i]+finish_text)


    elif user in report_patterns:
        i=rand(len(report_responses))
        Send_Output(report_responses[i])


    elif user in bullying_patterns:
        i=rand(len(bullying_responses))
        Send_Output(bullying_responses[i]+finish_text)


    elif user in Spam_patterns:
        i=rand(len(Spam_responses))
        Send_Output(Spam_responses[i])


    elif user in spam2_patterns:
        i=rand(len(spam2_responses))
        Send_Output(spam2_responses[i]+finish_text)


    elif user in spam3_patterns:
        i=rand(len(spam3_responses))
        Send_Output(spam3_responses[i]+finish_text)


    elif user in Actions_patterns:
        i=rand(len(Actions_responses))
        Send_Output(Actions_responses[i]+finish_text)


    elif user in end_patterns:
        i=rand(len(end_responses))
        Send_Output(end_responses[i])

        App.core.EmailClient.sendMessage(ChatBot.reportMessages)


    else:
        Send_Output("Sorry, I could not get you, Please rephrase.")

def Send_Output(message):
    ChatBot.responseHandler(message)
