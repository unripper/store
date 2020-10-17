"""
Author : Fadhil
Author URL : https://fadhilsaheer.github.io/fadhil/
Description : This is a ai made with python
"""




#importing modules

import androidhelper

#core setup

def say(audio):
    droid = androidhelper.Android()
    droid.ttsSpeak(audio)

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
