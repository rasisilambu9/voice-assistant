import speech_recognition as sr
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time

list1=["drive.google","amazon","yahoo","youtube","reddit","ebay","walmart","linkedin","microsoft","wikipedia","instagram","gmail","facebook","twitter","snapchat","google","w3schools","javatpoint","geeksforseeks"]
r=sr.Recognizer()
while(True):
    print("Speak something...")
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=0.2)
        audio2=r.listen(source2)
        MyText=r.recognize_google(audio2)
        MyText=MyText.lower()
        print("did you say "+MyText)
        ch=input("Enter [y/n]")
        if(ch=='y'):
            keyword=MyText
            if(MyText=="exit"):
                sys.exit()
            else:
                if(MyText in list1):
                    driver=webdriver.Chrome()
                    driver.get("https://www."+MyText+".com")
                else:
                    driver=webdriver.Chrome()
                    driver.get("https://www.google.com/search?q="+MyText)
        else:
            continue;
            print("speak again")