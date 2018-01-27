import sys
from PyQt4 import *
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore, uic
import pandas as pd
import matplotlib.pyplot as plt
from socialmedia2 import twitter_strm
import random

import matplotlib.backends.backend_qt4agg
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

form_class= uic.loadUiType("tweets.ui")[0]


class getTweets(QtGui.QMainWindow,form_class):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)


        self.GetTweets.clicked.connect(self.precall)
        self.aboutButton.clicked.connect(self.showMe)

    def showMe(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.show()

    def precall(self):
        self.name = self.NameOfFirst.text()
        print 'I am fetching tweets for ' + self.name
        self.tweets = self.tweetsCount.value()
        print 'fetching ' + str(self.tweets) + '  tweets'

        tweets_df=twitter_strm(self.name, self.tweets)
 
        print 'trying to put in gui'
        for tweet in range(0,len(tweets_df)):
            self.mytextEdit_8.append( str(tweet) + ':--  ' + tweets_df.text[tweet])
        
        rtcnt = sorted(tweets_df.retweet_count,reverse=True)
        year_created = sorted(tweets_df.year,reverse=True)
        fvcnt = sorted(tweets_df.favorite_count,reverse=True)
       
        print 'Drawing graph'

        ax = self.canvas.figure.add_subplot(111)
        ax2 = self.canvas2.figure.add_subplot(111)
        ax.plot(rtcnt,'go-')
        ax.set_title('Retweet counts')
        ax2.plot(fvcnt,'ro')
        ax2.set_title('Favorite counts')
        self.canvas.draw()
        self.canvas2.draw()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = getTweets()
    window.show()

    app.exec_()
