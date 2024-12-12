from tkinter import * 

def click():
    print("Tuč!")


root=Tk()
root.title("TUČ")
root.geometry("1250x900")
root.resizable(width=False,height=False)
root.iconbitmap('images.ico')

#background
root.config(bg="lightgreen")

button=Button(root,
              text='Daun',
              command=click,
              font='Arial 20 ',
              width=20,
              height=10,
              bg='black',
              activebackground='white',
              fg='yellow'
              )
button.pack()


img=PhotoImage(file="mne.png")
l_logo=Label(root,image=img)
l_logo.place(x=10,y=350)


root.mainloop()