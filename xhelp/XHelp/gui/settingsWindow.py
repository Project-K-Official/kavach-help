import os
import sys

from pathlib import Path

sys.path.append(
   os.path.abspath(
      Path(__file__).resolve().parent.parent.parent
   )
)

from PyQt5 import QtWidgets, uic
import XHelp as App

class SettingsWindow (QtWidgets.QMainWindow):
   def __init__ (self, *args, **kwargs):
      super(SettingsWindow, self).__init__(*args, **kwargs)
      
      uic.loadUi(
         App.Configuration.PACKAGE_DIR / 'gui' / 'uiFiles'
         / 'settingsWindow.ui',
         self,
      )
      
      self.pushButton.clicked.connect(App.gui.Application.settingsToHome)
      self.pushButton_2.clicked.connect(
         App.gui.Application.homeWindow.clearChats
      )
      
      # self.comboBox == session Timeout
      
      self.comboBox_2.setCurrentText(
         'On'
         if (App.Configuration.disappearingMessages == True)
         else 'Off'
      )
      
      self.comboBox_2.activated.connect(self.setDisappearingMessages)
      
      self.pushButton_3.clicked.connect(self.showBotDescription)
      self.pushButton_5.clicked.connect(self.showPrivacyPolicy)
      self.pushButton_4.clicked.connect(self.showHelpAndSupport)
      self.pushButton_6.clicked.connect(self.showTermsAndServices)
      
      self.showBotDescription()
   
   def setDisappearingMessages (self, index):
      if (self.comboBox_2.itemText(index) == 'On'):
         App.Configuration.disappearingMessages = True
         App.database.DatabaseHandler.Settings.update(
            'disappearingMessages'
         )
      elif (self.comboBox_2.itemText(index) == 'Off'):
         App.Configuration.disappearingMessages = False
         App.database.DatabaseHandler.Settings.update(
            'disappearingMessages'
         )
   
   def showBotDescription (self):
      self.label_3.setText(
         'This is a short Bot description!'
      )
   
   def showPrivacyPolicy (self):
      self.label_3.setText(
         'This is a short Privacy policy!'
      )
   
   def showHelpAndSupport (self):
      self.label_3.setText(
         'Yo, need help / support, even in help app !?\n'
         + 'Please press the red cross button on top of this screen !!!'
      )
   
   def showTermsAndServices (self):
      self.label_3.setText(
         'Term1: Do not ask for help!\n'
         + 'Thank you, you may leave!'
      )
