from tkinter import * 
from random import *

root=Tk()
root.title("Spēle")
root.geometry("600x600")
root.resizable(width=False,height=False)
root.iconbitmap('images.ico')
root['bg']= 'orange'

def Whyknb():
    knb=["Akmens","Šķēres","Papīrs"]
    value=choice(knb)
    lableText.configure(text=value)


lableText=Label(root,
              text='',
              font=('Comic Sans MS ',20,'bold'),
              #bg='',
              fg='blue'
              )
lableText.place(y=200,x=225)


scissors=Button(root,
            text='Šķēres',
            font=('Comic Sans MS',20,'bold'),
            bg='white',
            command=Whyknb
            )
scissors.place(x=20,y=300)

stone=Button(root,
            text='Akmens',
            font=('Comic Sans MS',20,'bold'),
            bg='white',
            command=Whyknb
            )
stone.place(x=220,y=300)


paper=Button(root,
            text='Papīrs',
            font=('Comic Sans MS',20,'bold'),
            bg='white',
            command=Whyknb
            )
paper.place(y=300,x=420)

root.mainloop()