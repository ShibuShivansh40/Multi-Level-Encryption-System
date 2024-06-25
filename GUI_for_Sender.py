import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Make sure to install the Pillow library for image handling

from  Sender import *




# Create the main window
root = tk.Tk()
root.title("Encryption Application")
root.geometry('1000x1000')



# Load and set the background image
background_image = Image.open("D:\Wallpapers\Asus_Black.jpg")  # Replace with your image file
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)



# Create and place the textboxes
sender_email_box = ttk.Entry(root, font=('Arial', 20), justify='center')
sender_email_box.place(relx=0.5, rely=0.1, relwidth=0.6, anchor='center')
sender_email_box.insert(0,"Sender's Email")

passwd_box = ttk.Entry(root, font=('Arial', 20), justify='center')
passwd_box.place(relx=0.5, rely=0.2, relwidth=0.6, anchor='center')
passwd_box.insert(0,"Sender's Password")

subject_box = ttk.Entry(root, font=('Arial', 20), justify='center')
subject_box.place(relx=0.5, rely=0.3, relwidth=0.6, anchor='center')
subject_box.insert(0,"Subject")

recep_email_box = ttk.Entry(root, font=('Arial', 20), justify='center')
recep_email_box.place(relx=0.5, rely=0.4, relwidth=0.6, anchor='center')
recep_email_box.insert(0,"Recipient's Email")

message_box = ttk.Entry(root, font=('Arial', 20), justify='center')
message_box.place(relx=0.5, rely=0.7, relwidth=0.8, relheight=0.3, anchor='center')
message_box.insert(0,"Message")



def on_button_click():
    sender_email = sender_email_box.get()
    passwd = passwd_box.get()
    subject = subject_box.get()
    email = recep_email_box.get()
    message = message_box.get().upper()
    print("Email : ",sender_email,"\nPassword : ",passwd,'\n')
    encrypted_message = encryption(message)
    send_email(sender_email, passwd, email, subject, encrypted_message)



# Create and place the button
button = ttk.Button(root, text="SEND", command=on_button_click)
button.place(relx=0.5, rely=0.9, anchor='center')



# Run the main loop
root.mainloop()
