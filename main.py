import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Hey, Iam Bruno,the virtual assistant, How can I help you?')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()


def takecommand():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'bruno' in command:
                command = command.replace('bruno','')
                print(command)
    except:
        pass
    return command

def runbruno():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        print('Playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        currenttime = datetime.datetime.now().strftime('%I %M %p')
        print(currenttime)
        talk('Current time is' + currenttime)

    elif 'lunch' or 'food' or 'dinner' or 'breakfast' in command:
        print('Thank you, but Iam already full with commands!')
        talk('Thank you, but Iam already full with commands!')

    elif 'joke' in command:
        fun = pyjokes.get_joke()
        print(fun)
        talk(fun)

    elif 'are you single' in command:
        print('Sorry, Iam too busy at work')
        talk('Sorry, Iam too busy at work')

    elif 'love' in command:
        print('Of course, I love my master!')
        talk('Of course, I love my master!')

    elif 'bye' in command:
        talk('Bye, see you soon!')
        exit()

    elif 'who' or 'what' in command:
        search = command.replace('who ','')
        search = command.replace('what','')
        information = wikipedia.summary(search,2)
        print(information)
        talk(information)

    else:
        mess = 'Sorry, I couldnot get you. Please say again'
        print(mess)
        talk(mess)

while True:
    runbruno()
