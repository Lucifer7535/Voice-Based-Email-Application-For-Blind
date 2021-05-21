import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
import email
from email.header import decode_header
import webbrowser

#function to give reply as 'ok done' to user
def ok_done():
    tts = gTTS(text="Ok Done!", lang='en')
    ttsname=("okdone.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print ("ok done!! \n")

#function for error when audio could not be recognised
def error1():
    tts = gTTS(text="Google Speech Recognition could not understand audio.", lang='en')
    ttsname=("error1.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("Google Speech Recognition could not understand audio. \n")
    choices()

#function for google speech recognition service error
def error2():
    tts = gTTS(text="Could not request results from Google Speech Recognition service", lang='en')
    ttsname=("error2.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("Could not request results from Google Speech Recognition service \n")
    choices()

#function for going back to choices menu or exiting the program
def backtomenu():
    tts = gTTS(text="Do you want to go back to choices menu for performing other actions or Do you want to Exit? Reply with Yes Or Exit Only.", lang='en')
    ttsname=("backtomenu.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("Do you want to go back to choices menu for performing other actions or Do you want to Exit.")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        text=r.recognize_google(audio)
        print ("You said : "+text +"\n") 
        if text == "yes" or text == "Yes":
            choices()             
        else:
            exit()

#function to take mail subject as input
def input_subject():
    tts = gTTS(text="Please Provide Subject For your Mail", lang='en')
    ttsname=("sub_mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Provide Subject For your Mail.")
        audio=r.listen(source)
        input_subject.subject = r.recognize_google(audio)
        print(input_subject.subject +"\n")
        ok_done()

    tts = gTTS(text=input_subject.subject, lang='en')
    ttsname=("sub_repeat.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("your subject is : " + input_subject.subject +"\n") 
    validating_sub_input()   

#function to take mail body as input
def input_body():
    tts = gTTS(text="Please Provide Body Context For your Mail.", lang='en')
    ttsname=("body_mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Provide Body For your Mail.")
        audio=r.listen(source)
        input_body.body = r.recognize_google(audio)
        print(input_body.body +"\n")
        ok_done()

    tts = gTTS(text=input_body.body, lang='en')
    ttsname=("body.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("your body is : " + input_body.body +"\n")
    validating_body_input()

#function to validate subject
def validating_sub_input():
    tts = gTTS(text="Is the provided input correct? Reply with yes or no only.", lang='en')
    ttsname=("val_input.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Is the provided input correct?")
            audio=r.listen(source)
            text = r.recognize_google(audio)
            print("you said: "+ text + "\n")
            ok_done()
            if text == "yes" or text == "YES":
                input_body()
            else:
                input_subject()  

    except:
        error1()

#function to validate body
def validating_body_input():
    tts = gTTS(text="Is the provided input correct? Reply with yes or no only.", lang='en')
    ttsname=("val_input.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Is the provided input correct?")
            audio=r.listen(source)
            text = r.recognize_google(audio)
            print("you said: "+ text + "\n")
            ok_done()
            if text == "yes" or text == "YES":
                mail_send()
            else:
                input_body() 
    except:
        error1()

#function to send mail
def mail_send():
    gmail_user = main.fullemail
    gmail_password = main.password

    sent_from = gmail_user
    to = [choices.remail]
    subject = input_subject.subject
    body = input_body.body

    email_text = f'Subject: {subject}\n\n{body}'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(main.fullemail, main.password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    
    tts = gTTS(text="Congrats! Your mail has been send. ", lang='en')
    ttsname=("send.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print ("Congrats! Your mail has send. \n")
    backtomenu()

#function to call the title
def main_project():
    tts = gTTS(text="Welcome to the Voice based Email Application", lang='en')
    ttsname=("title.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    print("Welcome to the Voice based Email Application \n")
    main()

#main function of program
def main():
    tts = gTTS(text="Please Provide your Gmail I D without @gmail.com", lang='en')
    ttsname=("I_mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Provide your Gmail ID without @gmail.com.")
        eaudio=r.listen(source)
        email_ID = r.recognize_google(eaudio)
        ok_done()
        emailcorrected = email_ID.replace(" ","")
        emaildomain = "@gmail.com"
        main.fullemail = emailcorrected + emaildomain
        print("your mail id is : " + main.fullemail + "\n")
  
    tts = gTTS(text="Please Provide your Gmail I D Password", lang='en')
    ttsname=("P_mail.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Provide your Gmail ID Password.")
        P_audio=r.listen(source)
        input_password = r.recognize_google(P_audio)
        main.password = input_password.replace(" ","")
        print("your password is : ********** \n")
        ok_done()

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    try:
        mail.login(main.fullemail,main.password)
        tts = gTTS(text="You have Succesfully Logged In to your email account!", lang='en')
        ttsname=("success.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        print("Succesfully Logged In! \n")
        choices()

    except smtplib.SMTPAuthenticationError:
        tts = gTTS(text="Your Mail I d And Password does not match. Please Provide Your Credentials again", lang='en')
        ttsname=("auth_error.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming = False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        print("Id And Password does not match")
        main()
        
def choices():
    print ("Select What You Want to do")
    tts = gTTS(text="Select your choice", lang='en')
    ttsname=("choice_title.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print ("1. Compose a mail.")
    tts = gTTS(text="Say First if you want to Compose A Mail.", lang='en')
    ttsname=("choice1.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    print ("2. Check your inbox")
    tts = gTTS(text="Say Second if you want to Check Your Inbox \n", lang='en')
    ttsname=("choice2.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    tts = gTTS(text="Your choice", lang='en')
    ttsname=("yourchoice.mp3")
    tts.save(ttsname)
    music = pyglet.media.load(ttsname, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Your choice: \n")
        audio=r.listen(source)
        text=r.recognize_google(audio)
        print ("You said : "+text + "\n")
        ok_done()
#-----------------------------------------------------------------------------------------------
        if text == 'first' or text == 'fast' or text == 'First':
            tts = gTTS(text="Please Provide recipient's Gmail I D without @gmail.com", lang='en')
            ttsname=("R_mail.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)
            print ("ok done!!")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Please Provide recipient's Gmail ID without @gmail.com.")
                raudio=r.listen(source)
                rmail_ID = r.recognize_google(raudio)
                ok_done()
                rmailcorrected = rmail_ID.replace(" ","")
                rmaildomain = "@gmail.com"
                choices.remail = rmailcorrected + rmaildomain
                print(choices.remail + "\n")
                input_subject()   
#-----------------------------------------------------------------------------------------------
        if text == '2' or text == 'tu' or text == 'two' or text == 'TWO' or text == 'to' or text == 'Second' or text == 'second' :
            mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
            mail.login(main.fullemail,main.password)
            stat, total = mail.select('Inbox')
            totalstr = str(total)
            corrected_total = totalstr.replace('b','')
            print ("Number of mails in your inbox :"+ corrected_total)
            tts = gTTS(text="Total mails are :"+corrected_total, lang='en')
            ttsname=("total.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)

            #unseen mails
            mail.select()
            unseen = len(mail.search(None, 'UnSeen')[1][0].split()) # unseen count
            print ("Number of UnSeen mails :" + str(unseen))
            tts = gTTS(text="Your Unseen mail :"+str(unseen), lang='en')
            ttsname=("unseen.mp3") 
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)

            # account credentials
            username = main.fullemail
            password = main.password
            def clean(text):
                # clean text for creating a folder
                return "".join(c if c.isalnum() else "_" for c in text)

            # create an IMAP4 class with SSL 
            imap = imaplib.IMAP4_SSL("imap.gmail.com")
            # authenticate
            imap.login(username, password)

            tts = gTTS(text="Do u want to see the unseen mails", lang='en')
            ttsname=("unseenmails.mp3") 
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Do u want to see the unseen mail?")
                audio=r.listen(source)
                text = r.recognize_google(audio)
                ok_done()
                print("you said : " + text + "\n")
            if text == 'yes' or text == 'Yes':
                N=unseen
            else:
                exit()

            status, messages = imap.select("INBOX")
            # total number of emails
            messages = int(messages[0])
            for i in range(messages, messages-N, -1):
                # fetch the email message by ID
                res, msg = imap.fetch(str(i), "(RFC822)")
                for response in msg:
                    if isinstance(response, tuple):
                        # parse a bytes email into a message object
                        msg = email.message_from_bytes(response[1])
                        # decode the email subject
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            # if it's a bytes, decode to str
                            subject = subject.decode(encoding)
                        # decode email sender
                        From, encoding = decode_header(msg.get("From"))[0]
                        if isinstance(From, bytes):
                            From = From.decode(encoding)
                        print("Subject:", subject)
                        tts = gTTS(text="Subject of Recieved mail is " + subject, lang='en')
                        ttsname=("subv.mp3")
                        tts.save(ttsname)
                        music = pyglet.media.load(ttsname, streaming = False)
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsname)
                        print("From:", From)
                        tts = gTTS(text="Mail is from" + From, lang='en')
                        ttsname=("fromv.mp3")
                        tts.save(ttsname)
                        music = pyglet.media.load(ttsname, streaming = False)
                        music.play()
                        time.sleep(music.duration)
                        os.remove(ttsname)
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
                                    if(len(body) == 0):
                                        pass
                                    else:
                                        tts = gTTS(text=body, lang='en')
                                        ttsname=("printbody.mp3")
                                        tts.save(ttsname)
                                        music = pyglet.media.load(ttsname, streaming = False)
                                        music.play()
                                        time.sleep(music.duration)
                                        os.remove(ttsname)
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
                                if(len(body) == 0):
                                        pass
                                else:
                                    tts = gTTS(text=body, lang='en')
                                    ttsname=("printbody.mp3")
                                    tts.save(ttsname)
                                    music = pyglet.media.load(ttsname, streaming = False)
                                    music.play()
                                    time.sleep(music.duration)
                                    os.remove(ttsname)
                        print("="*100)
            # close the connection and logout
            imap.close()
            imap.logout()
            backtomenu()
#------------------------------------------------------------------------------------------------
        else:
            tts = gTTS(text="Please Select the correct choice.Going Back to Choices Menu", lang='en')
            ttsname=("elsechoice.mp3")
            tts.save(ttsname)
            music = pyglet.media.load(ttsname, streaming = False)
            music.play()
            time.sleep(music.duration)
            os.remove(ttsname)
            choices()

main_project()
