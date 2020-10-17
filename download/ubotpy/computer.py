"""
Author : Fadhil
Author URL : https://fadhilsaheer.github.io/fadhil/
Description : This is a ai made with python
"""


#importing modules
import pyttsx3 #this will couse a error so open cmd and type "pip install pyttsx3"


#core setup

def say(audio):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(audio)
    engine.runAndWait()



#asking function

def main():
    command = input("Enter your command: ")

    #You can add many command as you wan't
    #with the format below

    if "hello" in command:
        print("Hello how are you") #printing answer
        say("Hello how are you")  #saying result
        main() #returning to main

    if "instagram" in command:
        print("Follow __fadhil_m_")
        say("Follow __fadhil_m_")
        main()

    if "youtube" in command:
        print("Unknown Ripper is the best")
        say("unknown ripper is the best")


    #else statement

    else:
        print("I don't know that")
        say("I don't know that")
        main()


main()
