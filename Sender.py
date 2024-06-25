#usr/bin/env python

#Sender's Software

import random, os, string, hashlib
import smtplib
import ssl
import imaplib, email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Algorithm_Encryption_ROT import *


#This function create a Random Strings
def createRandomStrings(len):
    result = ''.join((random.choice(string.ascii_lowercase+string.digits) for x in range(len)))
    return result

#This function codes the Encryption Key
def coding_decryptionKey_function(decryptionKey):
    key = createRandomStrings(15) + str(decryptionKey[0]) + createRandomStrings(15) + str(decryptionKey[1]) + createRandomStrings(15) + str(decryptionKey[2]) + createRandomStrings(15) + str(decryptionKey[3]) + createRandomStrings(15) + str(decryptionKey[4]) + createRandomStrings(15) 
    print(key)
    return key

creating_DecryptionKeyList = []  
n=5
    #Shift the array by 10 indices
encrypter_array = [ 0,0,0,0,0,0,0,0,0,0, 
                        encrypt_rot01 , encrypt_rot02 , encrypt_rot03 , encrypt_rot04 , encrypt_rot05 , encrypt_rot06 , encrypt_rot07 , encrypt_rot08 , 
                        encrypt_rot09 , encrypt_rot10 , encrypt_rot11 , encrypt_rot12 , encrypt_rot13 , encrypt_rot14 , encrypt_rot15 , encrypt_rot16 , 
                        encrypt_rot17 , encrypt_rot18 , encrypt_rot19 , encrypt_rot20 , encrypt_rot21 , encrypt_rot22 , encrypt_rot23, encrypt_rot24, encrypt_rot25]

for i in range(0,5):
        x=random.randint(10, 25)
        creating_DecryptionKeyList.append(x)
        print(x)

private_key = coding_decryptionKey_function(creating_DecryptionKeyList) 
print("Private Key : ",private_key)

global encrypted_message
    
    #Randomization
def encryption(message):

    for i in creating_DecryptionKeyList:
        function1 = encrypter_array[i]
        encrypted_message = function1(message)
        print("The Algo used : " , function1)
        print("Your Encrypted Message is :", encrypted_message)
        
    final_message = private_key + "\n\n\n " + encrypted_message
    return final_message


def send_email(sender_email, password, receiver_email, subject,  message, smtp_server="smtp.gmail.com", smtp_port=465):
    # Create a MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure connection with the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        # Login to the email account
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
