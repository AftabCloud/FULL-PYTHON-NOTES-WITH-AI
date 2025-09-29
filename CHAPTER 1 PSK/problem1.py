import pyttsx3 #voice library
engine = pyttsx3.init() #object creation as pyttsx3.init()
voices = engine.getProperty('voices') #getting details of current voice
engine.say("ABEEY JAANA") #method to speak the given text
engine.runAndWait() #without this command, speech will not be audible to us