import os
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename


def newfile():
    global file
    root.title("Untitled")
    file = None
    plot_region.delete(1.0,END)

def openfile():
    global file
    file = askopenfilename(filetypes = [("All Files","*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file))
        plot_region.delete(1.0,END)
        f = open(file, "r")
        plot_region.insert(1.0,f.read())
        f.close()
        root.title(os.path.basename(file))

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled", filetypes=[("All Files","*.*")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(plot_region.get(1.0,END))
            f.close()
    else:
        f = open(file, "w")
        f.write(plot_region.get(1.0,END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    plot_region.event_generate("<<Cut>>")

def copy():
    plot_region.event_generate("<<Copy>>")

def paste():
    plot_region.event_generate("<<Paste>>")

def fromfile():
    pass

def fromdirectory():
    pass

def new_tab():
    new_tab = Toplevel(plot_region)
    new_tab.geometry("300x300")
       



if __name__ == "__main__":

    #Basic tkinter setup
    root = Tk()
    root.title("MainWindow")
    root.geometry("677x677")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(f"{width}x{height}")

    #Menubar
    Menubar = Menu(root)


    #Filemenu starts
    Filemenu = Menu(Menubar, tearoff = 0)

    #to open new file
    Filemenu.add_command(label='New File', command = newfile)

    # to open already existing file
    Filemenu.add_command(label="Open", command = openfile)

    #to save the current file
    Filemenu.add_command(label="Save", command = savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Quit", command = quitapp)
    Menubar.add_cascade(label="File", menu = Filemenu)
    root.config(menu = Menubar)
    #Filemenu ends


    #Editmenu starts
    Editmenu = Menu(Menubar,tearoff = 0)

    #to add cut, copy, paste commands
    Editmenu.add_command(label='Cut', command = cut)
    Editmenu.add_command(label='Copy', command = copy)
    Editmenu.add_command(label='Paste', command = paste)

    Menubar.add_cascade(label='Edit',menu = Editmenu)
    root.config(menu = Menubar)
    # Editmenu ends

    
    #Import Data starts
    Import = Menu(Menubar,tearoff = 0)
    
    # to add auto and manual features
    Import.add_command(label='From File', command = fromfile)
    Import.add_command(label='Fom Directory', command = fromdirectory)
    Menubar.add_cascade(label='Import Data',menu = Import)
    root.config(menu = Menubar)
    #Import Data ends

    # leftside frame
    main_frame = Frame(root,bg = "lightgrey", borderwidth=1, relief=SUNKEN)
    main_frame.pack(side = LEFT,padx= 5,fill = "y")

    frame_1 = Frame(main_frame,bg = "white",border = 5)
    frame_1.pack(side = TOP, anchor = "nw",padx = 10,pady = 15)

    frame_2 = Frame(main_frame,bg = "white",border = 5)
    frame_2.pack(side = TOP, anchor = "nw",padx = 10,pady = 15)
    
    var1 = IntVar()
    frame_1_radio_1 = Radiobutton(frame_1, text="Live Mode", width = 25,height=2, variable=var1, value = 1)
    frame_1_radio_1.pack(side=TOP,pady = 3)

    frame_1_radio_2 = Radiobutton(frame_1,text = "Existing Dataset",width = 25,height = 2, pady = 5, variable=var1, value = 2)
    frame_1_radio_2.pack(side=TOP,pady = 3)

    var2 = IntVar()
    # frame_2_radio_1 = Radiobutton(frame_2,text = "Plot all",width = 20, variable=var2, value = 1)
    # frame_2_radio_1.pack(side=TOP,pady = 3)

    # frame_2_radio_2 = Radiobutton(frame_2,text = "Select Manually",width = 20,pady = 5, variable=var2, value = 2)
    # frame_2_radio_2.pack(side=TOP,pady = 3)

    # plot_region area
    plot_region = Text(root)
    plot_region.pack(side = TOP,anchor="nw",expand=True, fill=BOTH)
    # new_tab.title("newtab")
    btn = Button(plot_region, text="+", command=new_tab)
    btn.pack(side=TOP, anchor="nw")
    
    lbl = Label(new_tab, text="hi")
    lbl.pack(side=TOP, anchor="nw")
    


    root.mainloop()

