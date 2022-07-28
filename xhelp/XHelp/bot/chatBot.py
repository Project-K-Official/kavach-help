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
import torch

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
      
      App.bot.NltkUtils.start()
      
      ChatBot.device = torch.device(
         'cuda'
         if torch.cuda.is_available()
         else 'cpu'
      )
      
      with open(
            App.Configuration.PACKAGE_DIR / 'bot' / 'intents.json',
            'r',
         ) as json_data:
         ChatBot.intents = json.load(json_data)
      
      ChatBot.data = torch.load(
         App.Configuration.PACKAGE_DIR / 'bot' / 'data.pth'
      )
      
      ChatBot.model = App.bot.Models.NeuralNet(
         ChatBot.data['input_size'],
         ChatBot.data['hidden_size'],
         ChatBot.data['output_size'],
      ).to(ChatBot.device)
      ChatBot.model.load_state_dict(ChatBot.data['model_state'])
      ChatBot.model.eval()
      
      ChatBot.reportActive = False
      ChatBot.reportMessages = ''
   
   def reset ():
      App.Configuration.SESSION_ID += 1
   
   def sendResponse (message):
      original_message = str(message).strip()
      
      if (ChatBot.responseHandler != None):
         message = App.bot.NltkUtils.tokenize(message)
         X = App.bot.NltkUtils.bag_of_words(
            message,
            ChatBot.data['all_words'],
         )
         X = X.reshape(1, X.shape[0])
         X = torch.from_numpy(X).to(ChatBot.device)
         
         output = ChatBot.model(X)
         _, predicted = torch.max(output, dim=1)
         
         tag = ChatBot.data['tags'][predicted.item()]
         
         probs = torch.softmax(output, dim=1)
         prob = probs[0][predicted.item()]
         if prob.item() >= App.Configuration.BOT_PATTERN_MATCH_PROBABILITY:
           for intent in ChatBot.intents['intents']:
               if tag == intent['tag']:
                   if (tag == 'report' and (not ChatBot.reportActive)):
                      ChatBot.reportActive = True
                      ChatBot.reportMessages = '' + original_message
                      
                      ChatBot.responseHandler(
                          str(random.choice(intent['responses'])),
                      )
                   elif (tag == 'Actions.'
                         and ChatBot.reportActive
                         and ChatBot.reportMessages
                      ):
                      ChatBot.reportMessages += '\n' + original_message
                      
                      App.core.EmailClient.sendMessage(ChatBot.reportMessages)
                      
                      ChatBot.reportActive = False
                      ChatBot.reportMessages = ''
                      
                      ChatBot.responseHandler(
                          (
                             str(random.choice(intent['responses']))
                             + '\n'
                             + 'Your report has been successfully submitted !'
                          ),
                      )
                   elif (ChatBot.reportActive):
                      ChatBot.reportMessages += '\n' + original_message
                      
                      ChatBot.responseHandler(
                          (
                            "Noting it down, please continue ...\n"
                            + "If done, please type 'action'."
                          ),
                      )
                   else:
                      ChatBot.responseHandler(
                          str(random.choice(intent['responses'])),
                      )
                   
                   return None
         else:
            if (ChatBot.reportActive and original_message):
               ChatBot.reportMessages += '\n' + original_message
               ChatBot.responseHandler(
                   (
                     "Noting it down, please continue ...\n"
                     + "If done, please type 'action'."
                   ),
               )
            else:
               ChatBot.responseHandler(
                   ("I didn't understand your query! Please rephrase."),
               )
            return None
         
      return None
