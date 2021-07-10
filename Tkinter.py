from tkinter import * 

window = Tk()

def submit():
    """say hello to user"""
    username = entry.get()
    print(f"Hello {username}")


def delete():
    """Delete text"""
    entry.delete(0, END)


def back_space():
    """Delete last letter in text"""
    entry.delete(len(entry.get())-1, END)


window.geometry("400x400")  # Give width and height to window
window.title("App") # Give a title to window

window.config(background="cyan")    # background your window

entry = Entry(window, font=("arial",36), fg="green", bg='yellow')
entry.pack(side=TOP)

submit_button = Button(window, text="submit", command=submit, width=8, font=("arial",15,"bold") ,fg="green")
submit_button.place(x=60,y=190)


delete_button = Button(window, text="delete", width=8, fg="red" , font=("arial",15),command=delete)
delete_button.place(x=170,y=190)


back_space_button = Button(window, text="backspace", width=8,font=("arial",15), fg="blue" ,command=back_space)
back_space_button.place(x=280,y=190)



window.mainloop()   # replace windoew on screen