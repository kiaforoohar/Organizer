# Kiarash Foroohar Pak
#This program organizes the files in a folder based on the organizations of those same files in another folder




import os
import shutil
import sys

import tkinter as tk
import tkinter.messagebox as tkm

1

def quitIt():
    sys.exit(0)
    
def organize():
    
    # Checks if the enteries are filled 
    if e1.get() == "":
        tkm.showinfo("Warning", "Please write an address for Original folder")
        return
    if e2.get() == "":
        tkm.showinfo("Warning", "Please write an address for Target folder")
        return

    # Gets Original folder address
    Original = e1.get()
    #Gets Target folder address
    Target = e2.get()

    # Checks if the addresses are correct
    if not(os.path.isdir(Original)):
        tkm.showinfo("Warning", "Please write a correct address for Original folder")
        return
    if not(os.path.isdir(Target)):
        tkm.showinfo("Warning", "Please write a correct address for Target folder")
        return
    
    # Creates all the folders in the original in the target
    folders = []
    # r=root, d=directories, f = files
    for roots, directs, files in os.walk(Original):
        for d in directs:
            folders.append(d)

    for d in folders:
        os.mkdir(Target + '/' + d)


    # for all folders in original 
    for roots, directs, f in os.walk(Original):
        for folder in directs:
             #for all songs in the folder
            for r,d, songs in os.walk(Original+'/'+folder):
                for song in songs:
                    if os.path.exists(Target + '/' + song):
                       shutil.move(Target + '/' + song, Target +'/' + folder)

                       
if __name__ == "__main__":
    master = tk.Tk()
    master.title("Organizer")
    master.geometry("220x72")
    tk.Label(master, text="Original Folder:").grid(row=1)
    tk.Label(master, text="Target Folder:").grid(row=3)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    b1 = tk.Button(master, text = "Enter", command = organize)
    b2 = tk.Button(master, text = "Quit", command = quitIt)
    e1.grid(row=1, column=1)
    e2.grid(row=3, column=1)
    b1.grid(row=5, column=1)
    b2.grid(row=5, column=0)
    b1.focus_set()

    master.mainloop()

