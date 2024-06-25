#usr/bin/env python

#Receiver's Software

import random, os, string, hashlib
import smtplib
import ssl
import imaplib, email

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Algorithm_Decryption_ROT import *

decryptionCode = []

#Non-Automated Code-Function that provides us a List containing the order of Decryption/Encrypption
def decoding_decryptionKey_function(key):
    decryptionCode1=[]
    decryptionCode1.append(key[15]+key[16])
    decryptionCode1.append(key[32]+key[33])
    decryptionCode1.append(key[49]+key[50])
    decryptionCode1.append(key[66]+key[67])
    decryptionCode1.append(key[83]+key[84])
    print(decryptionCode1)
    return decryptionCode1


decrypter_array = [ 0,0,0,0,0,0,0,0,0,0,
                        decrypt_rot01 , decrypt_rot02 , decrypt_rot03 , decrypt_rot04 , decrypt_rot05 , decrypt_rot06 , decrypt_rot07 , decrypt_rot08 , 
                        decrypt_rot09 , decrypt_rot10 , decrypt_rot11 , decrypt_rot12 , decrypt_rot13 , decrypt_rot14 , decrypt_rot15 , decrypt_rot16 , 
                        decrypt_rot17 , decrypt_rot18 , decrypt_rot19 , decrypt_rot20 , decrypt_rot21 , decrypt_rot22 , decrypt_rot23 , decrypt_rot24 , decrypt_rot25]



def decryption(message, private_key):
    decryptionCode_array = decoding_decryptionKey_function(private_key) 
    print("arr : " , decryptionCode_array)
    decrypted_message = ""
    #Appending the indices to create Decryption Key
    for i in decryptionCode_array:
        function2 = decrypter_array[int(i)]
        print("The Algo Used : " , function2)
        decrypted_message = function2(message)
        print("Your Decrypted Message is :", decrypted_message)
    return decrypted_message


def fetching_the_latest_email(login_email, password):
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL("imap.gmail.com")
    imap_server.login(login_email, password)

    # Select the inbox
    status, messages = imap_server.select("Inbox")

    # Get the latest email ID
    latest_email_id = int(messages[0])

    # Fetch the email content
    status, data = imap_server.fetch(str(latest_email_id), "(RFC822)")

    # Parse the email
    import email

    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Access the email body
    message_body = email_message.get_payload()
    print("Subject : ", email_message['Subject'])
    if isinstance(message_body, str):
        # Message is plain text
        # print(message_body)
        f = open('C:/Users/seths/Downloads/yo_email.txt', 'a')
        f.write(message_body)
        f.close()

    else:
        # Message is multipart
        for part in message_body:
            if not part.is_multipart():
                # Extract text from non-multipart parts
                # print(part.get_payload())
                # f = open('C:/Users/seths/Downloads/yo_email2.txt', 'a')
                # f.write(part.get_payload())
                # f.close()
                return email_message['Subject'] , part.get_payload()


    # Print the message body
    # print(message_body)

    # Close the connection
    imap_server.close()
    imap_server.logout()


decryption(" PA ZOVBSK DVYR UVD","1x0ytfy6wbr2mev220uwv8b7xf0qgx9z18d4m8zkjb1jt2nog10rwxqaze23k6hztz13jb0tg416yk2dzcu16py3tntrrkomfemc")