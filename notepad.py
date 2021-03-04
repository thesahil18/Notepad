import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

def newfile():
    global file
    root.title("Untitled Text Document")
    file = None
    textarea.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("Text Documet", ".txt")])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file))
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt", filetypes=[("Text Documet", ".txt")])
        if file =="":
            file=None
        else:
            f = open(file, 'w')
            f.write(textarea.get(1.0, END))
            f.close
            root.title(os.path.basename(file))
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close

def quit():
    root.destroy()

def copy():
    textarea.event_generate(("<<Copy>>"))

def cut():
    textarea.event_generate(("<<Cut>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("About us","Coded By Sahil\nContact us at abcd@abcd.com")

def help():
    showinfo("Help","Contact us at abcd@abcd.com")

if __name__ == '__main__':
    root = Tk()
    root.wm_iconbitmap("mainicon.ico")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{int(width/2)}x{height-100}')
    root.maxsize(f'{width}', f'{height}')
    root.title("Untitled Text Document")

    #text Area
    textarea = Text(root, font="lucida 15")
    file = None
    textarea.pack(expand = True, fill='both')
    #End of Text area

    #Menu Bar
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New",command = newfile)
    FileMenu.add_command(label="open", command = openfile)
    FileMenu.add_command(label="Save", command = savefile)
    FileMenu.add_command(label="Exit", command = quit)
    MenuBar.add_cascade(label="File", menu = FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About us", command=about)
    HelpMenu.add_command(label="Help", command=help)
    MenuBar.add_cascade(label="Help", menu = HelpMenu)
    root.config(menu=MenuBar)
    #end Menu Bar
    
    #Scroll Bar
    Scroll = Scrollbar(textarea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    #bottom (Status Bar)
    bottomtext = StringVar()
    bottomtext.set("Ready")
    bottomframe = Label(root, textvariable=bottomtext,relief=SUNKEN, anchor='w')
    bottomframe.pack(side=BOTTOM, fill=X)
    #end of status bar

    
    root.mainloop()
