# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Attendace Done Jainal")
# engine.setProperty('rate',10)
# engine.setProperty('volume', 10)
# engine.runAndWait()
# 
import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

a = "Say something in natural language."

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)