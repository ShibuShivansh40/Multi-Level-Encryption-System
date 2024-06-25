import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Make sure to install the Pillow library for image handling

from Receiver import *

# Create the main window
root = tk.Tk()
root.title("Decryption Application")
root.geometry('1000x1000')


# Load and set the background image
background_image = Image.open("D:\Wallpapers\Asus_Black2.jpg")  # Replace with your image file
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)



# Create and place the textboxes
recev_email_box = ttk.Entry(root, font=('Arial', 20), justify='center')
recev_email_box.place(relx=0.5, rely=0.1, relwidth=0.6, anchor='center')
recev_email_box.insert(0,"Receiver's Email")

passwd_box = ttk.Entry(root, font=('Arial', 20), justify='center')
passwd_box.place(relx=0.5, rely=0.2, relwidth=0.6, anchor='center')
passwd_box.insert(0,"Receiver's Password")


def on_button_click():
    recev_email = recev_email_box.get()
    passwd = passwd_box.get()
    
    subject, content = fetching_the_latest_email(recev_email,passwd)
    lines = content.split('\n')

    # Remove leading and trailing whitespaces from each line
    lines = [line.strip() for line in lines]
    print(lines)

    decrypted_message = decryption(lines[3], lines[0])

    print_subject = ttk.Label(text=subject,font=('Arial', 20), anchor='center')
    print_subject.place(relx=0.5, rely=0.5, relwidth=0.6, anchor='center')

    message = ttk.Label(text=decrypted_message,font=('Arial', 20), anchor='center')
    message.place(relx=0.5, rely=0.6, relwidth=0.6, anchor='center')
    
    
    # print("Email : ",sender_email,"\nPassword : ",passwd,'\n')
    # encrypted_message = encryption(message)
    # send_email(sender_email, passwd, email, subject, encrypted_message)

global decrypted_message
# Create and place the button
button = ttk.Button(root, text="FETCH", command=on_button_click)
button.place(relx=0.5, rely=0.4, anchor='center')

# message = ttk.Label(text="", fg="black", bg="white")
# message.place(relx=0.5, rely=0.5, relwidth=0.6, anchor='center')

# Run the main loop
root.mainloop()
