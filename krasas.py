from tkinter import * 
import random



root=Tk()
root.title("Spēle")
root.geometry("600x600")
root.iconbitmap('images.ico')
root['bg']= 'orange'




def change_color():
    colors=["red","green","blue","yellow","pink","orange"]
    root.config(bg=random.choice(colors))


btn=Button(root,
            text='Zmi',
            font=('Comic Sans MS',20,'bold'),
            bg='white',
            command=change_color,
            height=10,
            width=20
            )
btn.place(y=300,x=420)

root.mainloop()