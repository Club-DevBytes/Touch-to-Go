# import flask
import webbrowser
import time

  
# This module is imported so that we can  
# play the converted audio 
import os 

import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output
name = "jainal"
a = "Attendance done" + name

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 


# # Create the application.
# APP = flask.Flask(__name__)


# @APP.route('/')
# def index():
#     """ Displays the index page accessible at '/'
#     """
#     return flask.render_template('index.html')

# @APP.route('/index-1.html')
# def second():
#     """ Displays the index page accessible at '/'
#     """
#     return flask.render_template('index-1.html')    

    

# APP.debug=True
# APP.run()
# The text that you want to convert to audio 

  
# Language in which you want to convert 

  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

  
# Saving the converted audio in a mp3 file named 
# welcome  


webbrowser.open('http://127.0.0.1:8887/',new=1, autoraise=True)



time.sleep(3)
controller.open('http://127.0.0.1:8887/attend.html', new=0, autoraise=True)
execute_unix(c)



  
# Playing the converted file 
