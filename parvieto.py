from tkinter import * 
import random
from PIL import Image, ImageTk
 
root=Tk()
root.title("Attēla pārvietošana")
root.geometry("1920x1080") 

# Read the Image
img = Image.open("mne.png")
 
# Resize the image using resize() method
resize_image = img.resize((500, 500))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image

 

#def in_count():


count=0


label=Label(root,text=f"Klikšķi : {count}", font=("Arial",16))
label.pack(pady=20)






def move_image():
    global img_x,img_y
    img_x += random.randint(-20,20)
    img_y += random.randint(-20,25)
    l_logo.place(x=img_x,y=img_y)

    global count 
    count+=1
    label.config(text=f"Klikšķi:{count}")




img_x,img_y= 50,50

#img=PhotoImage(file="mne.png")
l_logo=Label(root,image=img)
l_logo.place(x=img_x,y=img_y)

btn= Button(root,text="Pārvietot",command=move_image,font=("Arial ",14))
btn.pack()
btn.pack(pady=20)


root.mainloop()