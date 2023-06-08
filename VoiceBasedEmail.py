# Run the program by command streamlit run VoiceBasedEmail.py
from playsound import playsound
import speech_recognition as sr
import smtplib,ssl
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import pyttsx3
import time
import webbrowser
from email.header import decode_header

import streamlit as st
import pandas as pd

st.title("Voice Based Email for Blind")

login = os.getlogin
print ("You are logging from : "+login())
print("Project: Voice based Email for blind ")
tts = gTTS(text="Project: Voice based Email for blind", lang='en')
ttsname=("name.mp3") 
tts.save(ttsname)
playsound("name.mp3")
os.remove(ttsname)

def talk(text):
    temp=gTTS(text=text,lang='en')
    print(text)
    st.write(text)
   # x.write(text)
    tempname=("temp.mp3")
    temp.save(tempname)
    playsound("temp.mp3")
    os.remove(tempname)
    return temp
    
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        print("Ok Done!")
        st.write("Ok Done with taking Input!")
    return audio

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)
tts = talk("Welcome to our Voice Based Email Interface")
tts = talk("Please provide your Email ID and password to login")
while 1:
    tts=talk("Speak out your Email ID")

    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        audio=r.listen(source)
        print ("ok done!!")
        tts = talk("Ok Done with taking Input!")

    try:
        text=r.recognize_google(audio)
        #tts=talk("You said "+text)
        senderID = text
        senderID = senderID.replace("at the rate", "@")
        senderID = senderID.replace(" ", "")
        senderID = senderID.lower()
        print ("You said : "+senderID)
        tts=talk("You said "+senderID)
        #st.write("You said : "+senderID)
        tts=talk("Do you wish to continue yes or no?")

        r = sr.Recognizer() #recognize
        with sr.Microphone() as source:
            audio=r.listen(source)
            print ("Ok Done!!")
            tts = talk("Ok Done with taking Input!")
            #print ("Your Email ID : ")

        try:
            textc=r.recognize_google(audio)
            if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                tts=talk("You said: Yes")
                print ("You said: yes")
                break
            else:
                tts=talk("You said: No")
                print ("You said: no")
                continue
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")     
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


while 1:
    tts=talk("Speak out your mail password")
    
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:

        audio=r.listen(source)
        print ("ok done!!")
        tts = talk("Ok Done with taking Input!")
        # print ("Your password : ")

    try:
        text5=r.recognize_google(audio)
        #tts=talk("You said "+text5)
        pswd = text5
        pswd = pswd.replace("at the rate", "@")
        pswd = pswd.replace(" ", "")
        pswd = pswd.lower()
        tts=talk("You said "+pswd)
        tts=talk("Do you want to continue yes or no?")
        r = sr.Recognizer() #recognize
        with sr.Microphone() as source:
            audio=r.listen(source)
            print ("ok done!!")
            tts = talk("Ok Done with taking Input!")
            #print ("Your Email ID : ")

        try:
            textc=r.recognize_google(audio)
            if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                tts=talk("You said: Yes")
                print ("You said : yes")
                break
            else:
                tts=talk("You said: No")
                print ("You said : no")
                continue
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")     
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 


# #choices
tts=talk("option 1. compose a mail")
tts=talk("option 2. check your inbox")
tts=talk("option 3. Delete a mail")
tts=talk("option 4. Access Trash")
tts=talk("Tell your choice")


#voice recognition part
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("Your choice:")
    audio=r.listen(source)
    print ("ok done!!")

try:
    text=r.recognize_google(audio)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    tts = talk("Google Speech Recognition could not understand audio.")
     
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    tts = talk("Could not request results from Google Speech Recognition service; {0}".format(e))
#choices details
#text = 1
if text == '1' or text == '11' or text == '111' or text == 'One' or text == 'one':
    tts=talk("You said: 1 ")
    print ("You said : 1")

    while 1:
        tts=talk("Speak out receipient mail ID")

        r = sr.Recognizer() #recognize
        with sr.Microphone() as source:

            audio=r.listen(source)
            print ("ok done!!")
            tts=talk("Ok Done with taking Input!")
            # print ("Your password : ")

        try:
            text6=r.recognize_google(audio)
            RID = text6
            RID = RID.replace("at the rate", "@")
            RID = RID.replace(" ", "")
            RID = RID.lower()
            print ("That is : "+RID)
            tts=talk("You said "+RID)

            tts=talk("Do you want to continue yes or no?")
        
            r = sr.Recognizer() #recognize
            with sr.Microphone() as source:
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
                #print ("Your Email ID : ")

            try:
                textc=r.recognize_google(audio)
                if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                    tts=talk("You said: Yes ")
                    print ("You said : yes")
                    break
                else:
                    tts=talk("You said: No")
                    print ("You said : no")
                    continue
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")     
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")     
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    tts=talk("Speak out subject for the composed mail")

    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:

        audio=r.listen(source)
        print ("ok done!!")
        tts=talk("Ok Done with taking Input!")
        # print ("Your password : ")

    try:
        text7=r.recognize_google(audio)
        sub = text7
        sub = sub.replace("at the rate", "@")
        sub = sub.capitalize()
        tts=talk("You said "+sub)
        print ("That is : "+sub)    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")     
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    tts=talk("Speak out your message")
    r = sr.Recognizer() #recognize
    with sr.Microphone() as source:
        print ("Your message :")
        audio=r.listen(source)
        print ("ok done!!")
        tts=talk("Ok Done with taking Input!")
    try:
        text1=r.recognize_google(audio)
        text1 = text1.capitalize()
        tts=talk("You said: "+text1)
        msg = text1
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    context = ssl.create_default_context()
    message = MIMEMultipart("alternative")
    message["Subject"] = sub #"Testing"
    message["From"] = senderID 
    message["To"] =  RID
    part1 = MIMEText(msg, "plain")
    message.attach(part1)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as mail:
        mail.login(senderID,pswd) 
        mail.sendmail(senderID,RID,message.as_string())
        print("Mail sent successfully to " +  RID)
        tts=talk("Mail sent successfully to " +  RID)  
    
if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
    print ("You said : 2")
    tts=talk("You said: 2 ")
    mail = imaplib.IMAP4_SSL('imap.gmail.com',993) #this is host and port area.... ssl security
    mail.login(senderID,pswd)  #login
    stat, total = mail.select('Inbox')  #total number of mails in inbox
    a = str(total)
    length = int(a[3])
    print ("Total Number of mails in your inbox :"+ a[3]+a[4])
    tts=talk("Total Number of mails in your inbox are "+ a[3]+a[4])

    

    tts=talk("option 1. Read recent 5 mails")
    tts=talk("option 2. Read recent 5 unseen mails")
    tts=talk("option 3. Search mail by subject")

    tts=talk("Tell your choice")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")
        audio=r.listen(source)
        print ("ok done!!")
        tts = talk("Ok Done with taking Input!")
    try:
        text=r.recognize_google(audio)
    except sr.UnknownValueError:
       print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
       print("Could not request results from Google Speech Recognition service; {0}".format(e))

    result, data = mail.uid('search',None, "ALL")
    inbox_item_list = data[0].split() 

    if text == '1' or text == '11' or text == '111' or text == 'One' or text == 'one':
        print ("You said : 1")
        tts=talk("You said: 1 ")
        i = 1
        while i < 6:
            i = i * -1
            item = inbox_item_list[i]
            result2, email_data = mail.uid('fetch', item, '(RFC822)') #fetch
            raw_email = email_data[0][1].decode("utf-8") #decode
            email_message = email.message_from_string(raw_email)
            print ("From: "+email_message['From'])
            print ("Subject: "+str(email_message['Subject']))
            subject = email_message['Subject']

            tts = talk("Date: "+email_message['Date'])
            tts=talk("From: "+email_message['From'])
            tts =talk(" And Your subject: "+str(email_message['Subject']))
            tts=talk("Do you want to know whole content of the message Yes/No: ")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                # print ("Your choice:")
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
            try:
                text3=r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if text3 == 'YES' or text3 == 'Yes' or text3 == 'S' or text3 == 's' or text3 == 'yes':
                print('You said : Yes')
                tts=talk("You said: Yes ")
                for response in email_data:
                    if isinstance(response, tuple):
                        msg = email.message_from_bytes(response[1])
                        # if the email message is multipart
                        if msg.is_multipart():
                            # iterate over email parts
                            for part in msg.walk():
                                # extract content type of email
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    # print text/plain emails and skip attachments
                                    print(body)
                                elif "attachment" in content_disposition:
                                    # download attachment
                                    filename = part.get_filename()
                                    if filename:
                                        folder_name = clean(subject)
                                        if not os.path.isdir(folder_name):
                                            # make a folder for this email (named after the subject)
                                            os.mkdir(folder_name)
                                        filepath = os.path.join(folder_name, filename)
                                        # download attachment and save it
                                        open(filepath, "wb").write(part.get_payload(decode=True))
                        else:
                            # extract content type of email
                            content_type = msg.get_content_type()
                            # get the email body
                            body = msg.get_payload(decode=True).decode()
                            if content_type == "text/plain":
                                # print only text email parts
                                print(body)
                        tts=talk(body)
            else:
                tts = talk("You said: No")

            i = i * -1
            i = i + 1

    if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
        print("You said : 2")
        tts=talk("You said: 2 ")
        mail.select('Inbox', 
        readonly = True) 
        
        response, messages = mail.search(None, 
                                        'UnSeen')
        messages = messages[0].split()
        
        # take it from last
        latest = int(messages[-1])
        
        # take it from start
        oldest = int(messages[0])
        
        for i in range(latest, latest-5, -1):
            # fetch
            res, msg = mail.fetch(str(i), "(RFC822)")
            
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # print required information
                    print("Date: ",msg["Date"])
                    print("From: " ,msg["From"])
                    print("Subject: " ,msg["Subject"])
                    subject = msg['Subject']

                    tts=talk("Date: "+msg["Date"])
                    tts = talk("From: "+msg['From'])
                    tts = talk("And Your subject: "+str(msg['Subject']))
                    tts=talk("Do you want to know whole content of the message Yes/No:")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        # print ("Your choice:")
                        audio=r.listen(source)
                        print ("ok done!!")
                        print("Ok Done with taking Input!")
                    try:
                        text3=r.recognize_google(audio)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    if text3 == 'YES' or text3 == 'Yes' or text3 == 'S' or text3 == 's' or text3 == 'yes':
                        print('You said : Yes')
                        tts=talk("You said: Yes")
                        for response in messages:
                            if isinstance(response, tuple):
                                msg = email.message_from_bytes(response[1])
                                # if the email message is multipart
                                if msg.is_multipart():
                                    # iterate over email parts
                                    for part in msg.walk():
                                        # extract content type of email
                                        content_type = part.get_content_type()
                                        content_disposition = str(part.get("Content-Disposition"))
                                        try:
                                            # get the email body
                                            body = part.get_payload(decode=True).decode()
                                        except:
                                            pass
                                        if content_type == "text/plain" and "attachment" not in content_disposition:
                                            # print text/plain emails and skip attachments
                                            print(body)
                                            talk(body)
                                        elif "attachment" in content_disposition:
                                            # download attachment
                                            filename = part.get_filename()
                                            if filename:
                                                folder_name = clean(subject)
                                                if not os.path.isdir(folder_name):
                                                    # make a folder for this email (named after the subject)
                                                    os.mkdir(folder_name)
                                                filepath = os.path.join(folder_name, filename)
                                                # download attachment and save it
                                                open(filepath, "wb").write(part.get_payload(decode=True))
                                else:
                                    # extract content type of email
                                    content_type = msg.get_content_type()
                                    # get the email body
                                    body = msg.get_payload(decode=True).decode()
                                    if content_type == "text/plain":
                                        # print only text email parts
                                        print(body)
                                        tts=talk(body)
                    else:
                        tts = talk("You said: No")
            
    if text == '3' or text == 'three' or text == 'three three' or text == 'threethree' or text == 'Three':
        print ("You said : 3")
        tts=talk("You said: 3 ")
        tts=talk("Speak out subject: ")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            print ("ok done!!")
            print("Ok Done with taking Input!")
        try:
            text4=r.recognize_google(audio)
            tts=talk("You said "+text4)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        sub = text4
        
        i = 1
        while i < 30:
            if i<len(inbox_item_list):
                i = i * -1
                item = inbox_item_list[i]
                result2, email_data = mail.uid('fetch', item, '(RFC822)') #fetch
                raw_email = email_data[0][1].decode("utf-8") #decode
                email_message = email.message_from_string(raw_email)
                if email_message['Subject'].lower() == sub.lower():
                    tts = talk("Date: "+email_message['Date'])
                    print ("From: "+email_message['From'])
                    print ("Subject: "+str(email_message['Subject']))
                    tts=talk("From: "+email_message['From'])
                    tts = talk(" And Your subject: "+str(email_message['Subject']))
                    subject = email_message['Subject']
                    tts=talk("Do you want to know whole content of the message Yes or No: ")

                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        # print ("Your choice:")
                        audio=r.listen(source)
                        print ("ok done!!")
                        print("Ok Done with taking Input!")
                    try:
                        text3=r.recognize_google(audio)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    if text3 == 'YES' or text3 == 'Yes' or text3 == 'S' or text3 == 's' or text3 == 'yes':
                        print('You said : Yes')
                        tts=talk("You said: Yes")
                        for response in email_data:
                            if isinstance(response, tuple):
                                msg = email.message_from_bytes(response[1])
                                # if the email message is multipart
                                if msg.is_multipart():
                                    # iterate over email parts
                                    for part in msg.walk():
                                        # extract content type of email
                                        content_type = part.get_content_type()
                                        content_disposition = str(part.get("Content-Disposition"))
                                        try:
                                            # get the email body
                                            body = part.get_payload(decode=True).decode()
                                        except:
                                            pass
                                        if content_type == "text/plain" and "attachment" not in content_disposition:
                                            # print text/plain emails and skip attachments
                                            print(body)
                                            talk(body)
                                        elif "attachment" in content_disposition:
                                            # download attachment
                                            filename = part.get_filename()
                                            if filename:
                                                folder_name = clean(subject)
                                                if not os.path.isdir(folder_name):
                                                    # make a folder for this email (named after the subject)
                                                    os.mkdir(folder_name)
                                                filepath = os.path.join(folder_name, filename)
                                                # download attachment and save it
                                                open(filepath, "wb").write(part.get_payload(decode=True))
                                else:
                                    # extract content type of email
                                    content_type = msg.get_content_type()
                                    # get the email body
                                    body = msg.get_payload(decode=True).decode()
                                    if content_type == "text/plain":
                                        # print only text email parts
                                        print(body)
                                        tts=talk(body)
                    else:
                        tts = talk("You said: No")
            else:
                tts = talk("End of searching mails")
                break
            i = i * -1
            i = i + 1
    mail.close()
    mail.logout()
if text == '3' or text == 'three' or text == 'three three' or text == 'threethree' or text == 'Three' or text == 'To':
    username = senderID
    password = pswd
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    # imap.login(senderID,pswd)
    imap.select("INBOX")
    tts = talk("On what basis do you want to select a mail to delete")
    tts=talk("option 1. From senders mail ID")
    tts=talk("option 2. Based on subject")
    tts=talk("option 3. Since Date")
    tts=talk("option 4. Before Date")
    tts=talk("Option 5. Delete all mails")
    tts=talk("Tell your choice")
    flag = False

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice:")
        audio=r.listen(source)
        print ("ok done!!")
        tts = talk("Ok Done with taking Input!")
    try:
        textdel=r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if textdel == '1' or textdel == '11' or textdel == '111' or textdel == 'One' or textdel == 'one':
        tts=talk("You said: 1 ")
        print ("You said : 1")
        while 1:
            tts = talk("Speak out senders mail ID")
            print("Speak out senders mail ID")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
            try:
                textdel1=r.recognize_google(audio)
                searchstring = textdel1
                tts=talk("You said "+ searchstring)
                tts=talk("Do you want to continue yes or no?")
            
                r = sr.Recognizer() #recognize
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print ("ok done!!")
                    tts = talk("Ok Done with taking Input!")
                    #print ("Your Email ID : ")

                try:
                    textc=r.recognize_google(audio)
                    if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                        tts=talk("You said: Yes ")
                        print ("You said : yes")
                        status, messages = imap.search(None, 'FROM ' +'"' + searchstring + '"')
                        break
                    else:
                        tts=talk("You said: No")
                        print ("You said : no")
                        continue
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")     
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    elif textdel == '2' or textdel == 'tu' or textdel == 'two' or textdel == 'Tu' or textdel == 'to' or textdel == 'To' :
        tts=talk("You said: 2 ")
        print ("You said : 2")
        while 1:
            tts = talk("Speak out subject of mail")
            print("Speak out subject of mail")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
            try:
                textdel1=r.recognize_google(audio)
                searchstring = textdel1
                tts=talk("You said "+ searchstring)
                tts=talk("Do you want to continue yes or no?")
            
                r = sr.Recognizer() #recognize
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print ("ok done!!")
                    tts = talk("Ok Done with taking Input!")
                    #print ("Your Email ID : ")

                try:
                    textc=r.recognize_google(audio)
                    if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                        tts=talk("You said: Yes ")
                        print ("You said : yes")
                        status, messages = imap.search(None, 'SUBJECT ' + '"' + searchstring + '"')
                        break
                    else:
                        tts=talk("You said: No")
                        print ("You said : no")
                        continue
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")     
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    elif textdel == '3' or textdel == 'three' or textdel == 'three three' or textdel == 'threethree' or textdel == 'Three':
        tts=talk("You said: 3 ")
        print ("You said : 3")
        while 1:
            tts = talk("Speak out Date, from which you want to delete mails")
            print("Speak out Date, from which you want to delete mails")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
            try:
                textdel1=r.recognize_google(audio)
                searchstring = textdel1
                tts=talk("You said "+ searchstring)
                tts=talk("Do you want to continue yes or no?")
            
                r = sr.Recognizer() #recognize
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print ("ok done!!")
                    tts = talk("Ok Done with taking Input!")
                    #print ("Your Email ID : ")

                try:
                    textc=r.recognize_google(audio)
                    if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                        tts=talk("You said: Yes ")
                        print ("You said : yes")
                        status, messages = imap.search(None, 'SINCE ' + '"' +searchstring+'"')
                        break
                    else:
                        tts=talk("You said: No")
                        print ("You said : no")
                        continue
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")     
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    elif textdel == '4' or textdel == 'four' or textdel == 'four four' or textdel == 'fourfour' or textdel == 'Four' or textdel == '44' or textdel == '4 4' or textdel == 'For' or textdel == 'for':
        tts=talk("You said: 4 ")
        print ("You said : 4")
        while 1:
            tts = talk("Speak out Date, before which you want to delete mails")
            print("Speak out Date, from which you want to delete mails")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio=r.listen(source)
                print ("ok done!!")
                tts = talk("Ok Done with taking Input!")
            try:
                textdel1=r.recognize_google(audio)
                searchstring = textdel1
                tts=talk("You said "+ searchstring)
                tts=talk("Do you want to continue yes or no?")
            
                r = sr.Recognizer() #recognize
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print ("ok done!!")
                    tts = talk("Ok Done with taking Input!")
                    #print ("Your Email ID : ")

                try:
                    textc=r.recognize_google(audio)
                    if textc == 'YES' or textc == 'Yes' or textc == 'S' or textc == 's' or textc == 'yes':
                        tts=talk("You said: Yes ")
                        print ("You said : yes")
                        status, messages = imap.search(None, 'BEFORE ' + '"' + searchstring + '"')
                        break
                    else:
                        tts=talk("You said: No")
                        print ("You said : no")
                        continue
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio.")     
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else:
        tts=talk("You said: 5 ")
        print ("You said : 5 ")
        status, messages = imap.search(None, "ALL")
        tts = talk("Deleting All Messages!")
        print("Deleting All Messages!")
        flag = True
    messages = messages[0].split()
    if flag == True:
        for mail in messages:
            imap.store(mail, "+X-GM-LABELS", "\\Trash")
        tts = talk("Deleted All Messages!")
        print("All mails moved to trash successfully!")
    else:
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes type, decode to str
                        subject = subject.decode()
                    print("Date: ",msg["Date"])
                    print("From: " ,msg["From"])
                    print("Subject: " ,subject)

                    tts=talk("Date: "+msg["Date"])
                    tts = talk("From: "+msg['From'])
                    tts = talk("And Your subject: "+str(subject))
                    tts=talk("Do you want to delete the mail? Yes/No:")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        # print ("Your choice:")
                        audio=r.listen(source)
                        print ("ok done!!")
                        print("Ok Done with taking Input!")
                    try:
                        text3=r.recognize_google(audio)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio.")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    if text3 == 'YES' or text3 == 'Yes' or text3 == 'S' or text3 == 's' or text3 == 'yes':
                        tts = talk("You said: Yes")
                        delflag = True
                    else:
                        delflag = False
                        tts = talk("You said: No")
            # mark the mail as deleted
            if delflag == True:
                imap.store(mail, "+X-GM-LABELS", "\\Trash")
                tts = talk("Mail Moved to trash Successfully!")
    tts = talk("End of searching mails to delete")
    imap.close()
    imap.logout()

#root.mainloop()