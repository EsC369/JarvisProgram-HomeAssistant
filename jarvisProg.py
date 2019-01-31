import sys
from gtts import gTTS  # Google speech to text Translate   pip install gTTS --user
import speech_recognition as sr # Google speech recoginition     pip install SpeechRecognition --user
#install mpg123 package: pip install mpg123 --user
# install pyaudio: pip install pyaudio     < -- install packages
# pip install ipython -- user
# pip install --upgrade setuptools
import pyttsx3    # pip install pyttsx3 --user    # Alternative to mpg123 since its only for macs!!! :()
import os
import webbrowser
import smtplib
myBool = True
# MAKE IT LEARN HOW TO PLAY MUSIC!

### STUFF TO ADD###
# add fucntionality to where you can say (action) , (data) for advanced things
# Add functionality to have jarvis prog active/turn on with certain command, otherwise will be closed.
# Add Where i talk and it types out for me! 
##############

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang="en") # take google text to speech and set language to english
    tts.save("audio.mp3")
    # os.system("mpg123 audio.mp3") #play with mpg123
    # Utilize Python text 3 Since having issues with mpg123..
    engine = pyttsx3.init();
    # Change Voice:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # Change voice to girl
    # Speech Rate:
    speechRate = engine.getProperty('rate')
    engine.setProperty('rate', speechRate+5)
    engine.say(audio);
    engine.runAndWait() 
    

# Listens for commands:
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready for your next command!")
        # r.pause_threshold = 1 # give a bit of time before looking for sound:
        r.adjust_for_ambient_noise(source, duration=1) # Ambient noise
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You Said " + command.lower())
    #Loop back, continue to listen for commands:
    except sr.UnknownValueError: # unless its gets back command it doesnt understand
        # print("test Your here ERROR")
        assistant(myCommand())
    return command.lower()


# Aissitant to command response inptake
def assistant(command):
    # response = command.lower() # Ensure all responses are lower case to desture issues with speech recog.
    if "open google" in command:
        talkToMe("Opening Google Browser")
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        url = "https://www.google.com"
        webbrowser.get(chrome_path).open(url)
    # if "what is les" or "what is Les" or "what is lay" in command: # Suppose to be Lei but the speech regocinition is retarded...
    #     return talkToMe("The most beautiful woman in the world!")
    if "what up" in command:
        return talkToMe("Chillin Bro")
        #EMail utilizing web email socket:
    if "email" in command:
        return talkToMe("Who is the recipient?")
        recipient = myCommand()

        if "ryan" in recipient:
            talkToMe("What Should I say?")
            content = myCommand()
            # Init gmail SMTP:
            mail= smtplib.SMTP("smtp.gmail.com", 587)
            # Identify to server:
            mail.ehlo()

            # Encrypt Session:
            mail.starttls()

            # Login to mail:
            mail.login("JarvisEsC369@gmail.com", "Escmoney1234$")

            # Senf message
            mail.sendmail("Ryan Smith", "rksmith369@gmail.com", content)

            #close connectionL
            mail.close()

            # Que that mail has been sent:
            talkToMe("Email Sent!")
            # #relaunch to detur errors:
            # assistant(myCommand())
    if "shut down" in command:
        talkToMe("Shutting down!")
        sys.exit()
        myBool = False

talkToMe("I am ready for your command sir Ryan!")

# instantiate loop that will continue to ask for commands while the prog is running:
while(myBool == True):
    # talkToMe("What Is Your Command Sir?")
    assistant(myCommand())
    # myCommand()
