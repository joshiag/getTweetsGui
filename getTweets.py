#import necessary libraries

import sys
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore, uic
import pandas as pd
import matplotlib.pyplot as plt
from socialmedia2 import twitter_strm
#just in case if required
import random

# necessary for graphs on canvas of GUI

import matplotlib.backends.backend_qt4agg
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

#get the ui file created with qt designer

form_class= uic.loadUiType("tweets.ui")[0]

#main Class

class getTweets(QtGui.QMainWindow,form_class):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)

#when buttons are clicked call necessary functions
        self.GetTweets.clicked.connect(self.precall)
        self.aboutButton.clicked.connect(self.showMe)

        #Messagebox for about
    def showMe(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

    #call function from socialmedia2.py which actually gets the tweets and puts it in a dataframe which is processed here
        
    def precall(self):
        self.name = self.NameOfFirst.text()
  
#printing on command line to see what its doing

        print 'I am fetching tweets for ' + self.name
        self.tweets = self.tweetsCount.value()
#how many tweets are fetched
        print 'fetching ' + str(self.tweets) + '  tweets'

        tweets_df=twitter_strm(self.name, self.tweets)
 #draw grapns on gui
        print 'trying to put in gui'
        for tweet in range(0,len(tweets_df)):
            self.mytextEdit_8.append( str(tweet) + ':--  ' + tweets_df.text[tweet])
        
        rtcnt = sorted(tweets_df.retweet_count,reverse=True)
        year_created = sorted(tweets_df.year,reverse=True)
        fvcnt = sorted(tweets_df.favorite_count,reverse=True)
  
        print 'Drawing graph'
    
#draw graphs of retweet and favorite count in gui canvas widget
        ax = self.canvas.figure.add_subplot(111)
        ax2 = self.canvas2.figure.add_subplot(111)
        ax.plot(rtcnt,'go-')
        ax.set_title('Retweet counts')
        ax2.plot(fvcnt,'ro')
        ax2.set_title('Favorite counts')
        self.canvas.draw()
        self.canvas2.draw()

  #initialize the application

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = getTweets()
    window.show()

    app.exec_()
