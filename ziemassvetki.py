from tkinter import *
import tkinter.font as font
from random import *
import random
from PIL import Image, ImageTk

root=Tk()

root.title("Laime")
root.geometry('1920x1080')
root.resizable(width=False,height=False)


myFont = font.Font(family='Courier', size=30, weight='bold')





e=Entry(root,show='')
e.pack()


# Read the Image
img = Image.open("baby.png")
 
# Resize the image using resize() method
resize_image = img.resize((500, 500))
 
img = ImageTk.PhotoImage(resize_image)
 
l_logo=Label(root,image=img)
l_logo.place(x=1100,y=50)

def get():
    label1['text']=e.get()

def change_color():
    colors=["red","green","blue","yellow","pink","orange"]
    root.config(bg=random.choice(colors))

def Whyknb():
    knb=[ "Lai spožās Ziemassvētku gaismas, dzīvības un mīlestības straume ienāk mūsu sirdī un dzīvē!",
    "Lai katrā mājā ienāk Ziemassvētku brīnums,Lai katru gadu sirds no jauna tic, cer un kvēli mīl!",
    "Lai Ziemassvētku brīnums piepilda vispārdrošākos sapņus!",
    "Sniegbaltīte klusi, klusi Visus rūķus apkniebuse Visu šņabi izdzēruse Tepat sētā atlūzuse.",
    "Lai piepildās, kas sirdī noglabāts kā neiespējams!"]
    value=choice(knb)
    lableText.configure(text=value)

lableText=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              #bg='',
              fg='blue',
              )
lableText.place(x=600,y=550)


btn=Button(root,text='Krāsa',bg='white',command=change_color,height=1,width=5)
btn.place(x=200,y=200)
btn['font'] = myFont

btn2=Button(root,text='Novēlējums',bg='white',command=Whyknb,height=1,width=10)
btn2.place(x=200,y=500)
btn2['font'] = myFont


btn3=Button(root,text='Vārds',command=get,bg='white',height=1,width=5)
btn3.pack()
btn3.place(x=200, y=800)
btn3['font'] = myFont


label1=Label(root,bg='white',fg='black',)
label1['font'] = myFont

label1.pack()


root.mainloop()