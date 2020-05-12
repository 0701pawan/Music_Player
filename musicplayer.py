import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *

#### The directory chooser opens the dialog box  to select folder  in which songs are there###

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
            #print(files)

            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[0])
            pygame.mixer.music.play()
            
### This function plays the next song when we click on the nextsong button on tkinter display ### 
            
def nextsong(event):
    global index
    index+=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatesong()

### This function plays the previous song when we click on the previoussong button on tkinter display ### 

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatesong()

### This function stops the song when we click on stop song button ###

def stopsong(event):
    pygame.mixer.music.stop()



if __main__="__main__" :  
    
    root =Tk()
    root.minsize(300, 300)
    listofsongs = []

    index=0

    directorychooser()

    label = Label(root, text='Music Player')
    label.pack()

    listbox = Listbox(root)
    listbox.pack()

    listofsongs.reverse()

    for items in listofsongs:
        listbox.insert(0, items)
        
### This create the next button and binds it with its function ###

    nextbutton = Button(root, text='next song')
    nextbutton.pack()
    nextbutton.bind("<Button-1>", nextsong)
    
### This create the previous button and binds it with its function ###

    previousbutton = Button(root, text='previous song')
    previousbutton.pack()
    previousbutton.bind("<Button-1>", previoussong)

### This create the stop button and binds it with its function ###

    stopbutton = Button(root, text='stop song')
    stopbutton.pack()
    stopbutton.bind("<Button-1>", stopsong)

    songlabel = Label(root, textvariable=v, width="38")
    songlabel.pack()


    root.mainloop()











