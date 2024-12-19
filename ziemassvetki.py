from tkinter import *
import tkinter.font as font
from random import *
import random
from PIL import Image, ImageTk

root=Tk()

root.title("Laime")
root.geometry('1920x1080')
root.resizable(width=True,height=True)
root.configure(background='lightgreen')


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

def rinda():
    with open("info.txt","r",encoding="utf-8") as file:
            lines=file.readlines()
            if lines:
                rand=random.choice(lines[:][3:]).strip()
                lable1.configure(text=f"Prognoze uz 2025.gadu {rand}")
            else:
                lable1.configure(text="Fails ir tukšs")


lable1=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              bg='white',
              fg='blue',
              )
lable1.place(x=300,y=900)
lable1['font']= myFont

label1=Label(root,bg='white',fg='black',)
label1.pack()

lableText=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              #bg='',
              fg='blue',
              )
lableText.place(x=600,y=575)


btn=Button(root,text='Krāsa',bg='white',command=change_color,height=1,width=10)
btn.place(x=200,y=150)
btn['font'] = myFont

btn2=Button(root,text='Novēlējums',bg='white',command=Whyknb,height=1,width=10)
btn2.place(x=200,y=350)
btn2['font'] = myFont


btn3=Button(root,text='Vārds',command=get,bg='white',height=1,width=10)
btn3.pack()
btn3.place(x=200, y=550)
btn3['font'] = myFont

btn4=Button(root,text='2025',command=rinda,bg='white',height=1,width=10)
btn4.pack()
btn4.place(x=200, y=750)
btn4['font'] = myFont




root.mainloop()