import pyttsx3
engine = pyttsx3.init()

print("---- Text To Speech ----")

rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

name = input("what is you name? ")
if name == "nathan":
    engine.say("Hello, Welcome Back" + name)
    engine.runAndWait()
else:
    print("Hello! You must be new, nice to meet you " + name)
    engine.say("Hello! You must be new, nice to meet you " + name)
    engine.runAndWait()

anything = input("Enter anything for text-to-speech ")
engine.say(anything)
engine.runAndWait()


