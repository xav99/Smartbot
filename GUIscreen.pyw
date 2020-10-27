import tkinter as tk
from tkinter import *
from tkinter import messagebox
from GUIsource import launcher, prevSpeech
from GUIsourceType_Mode import sendCommand, returnMood
import time

class Mainframe(tk.Tk):
    """
    Defines which frame is the main frame
    """

    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = Home(self)
        self.frame.pack()

    def change(self, frame):
        """
        Deletes current frame and creates a new one
        """
        self.frame.pack_forget()  # delete current frame
        self.frame = frame(self)
        self.frame.pack()  # make new frame


class Home(tk.Frame):
    """
    Application home screen
    """

    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master.title("Smartbot")
        self.master.geometry("450x500")
        self.fileVar = StringVar()
        self.file = self.fileVar.get()
        self.master.bind("<Button-1>", self.callback)
        self.mostRecentCommand = ""
        self.mood = "Neutral"
        

        # pulldown menu initiation
        self.menubar = Menu(self)
        self.master.config(menu=self.menubar)

        # Pulldown menu file
        fileMenu = Menu(self.menubar, tearoff=0)
        fileMenu.add_command(label="Clear All", command=lambda: 0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=exit)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        #Image
        self.photo = PhotoImage(file = r"krispp.png")
        label = Button(image=self.photo)
        label.image = self.photo # keep a reference!

        #Mood emoji
        self.happy_emoji = PhotoImage(file = r"happy.png")
        self.sad_emoji = PhotoImage(file = r"sad.png")
        self.neutral_emoji = PhotoImage(file = r"neutral.png")
        self.angry_emoji = PhotoImage(file = r"angry.png")
        self.poop_emoji = PhotoImage(file = r"poop.png")
        label = Button(image=self.happy_emoji)
        label.image = self.happy_emoji 
        
        # Entry
        self.fileEntry = tk.Entry(self.master, textvariable=self.fileVar, font="ariel 16",width="30")
        self.fileEntry.place(x=8, y=460)
        self.fileVar.set("Chat with Jorge")
        self.fileEntry.focus()   

        #frame 2
        self.frame2=Frame(self.master)
        self.frame2.place(x=8, y=10)

        #scrollbar
        scrollbar = Scrollbar(self.frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        #ListBox
        self.list1=Listbox(self.frame2, height=24, width=52, font="ariel 11")
        self.list1.pack(expand=1, fill="both")
        self.list1.insert(END, "Say or type 'help' for a list of commands")
        
        #attaching scrollbar to listbox
        self.list1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.list1.yview)
        
        # Buttons
        microphoneBtn = self.newButton(self, posx=417, posy=460, image=self.photo, command=self.micPress)
        self.master.bind("<Return>", self.sendText)
        

    def addItem(self, item):
        self.list1.insert(END, item)

    def getText(self):
        return self.fileVar.get()

    def moodDisplay(self): # display the mood emoji
        dispimg = self.neutral_emoji # displaying the emoji based on mood
        if self.mood == "Happy":
            dispimg = self.happy_emoji
        elif self.mood == "Angry":
            dispimg = self.angry_emoji
        elif self.mood == "Sad":
            dispimg = self.sad_emoji
        elif self.mood == "poop":
            dispimg = self.poop_emoji
        else:
            dispimg = self.neutral_emoji
        emojiBtn = self.newButton(self, posx=379, posy=457, image=dispimg, command=None)
        
    def sendText(self, _event=None):
        self.mostRecentCommand = self.getText()
        self.addItem("You typed: "+self.getText())
        try:
            self.addItem("Bot typed: "+sendCommand(self.getText()))
        except:
            self.addItem("Bot said: "+str(sendCommand(self.getText())))
        self.mood = returnMood()
        self.moodDisplay()
        self.fileEntry.delete(0, 'end')

    def clearText(self, _event=None):
        self.fileEntry.delete(0, 'end')

    def micPress(self):
        print("talk")
        launcher()
        self.addItem("You said: "+prevSpeech()[0])
        try:
            self.addItem("Bot said: "+prevSpeech()[1])
        except:
            self.addItem("Bot said: "+str(prevSpeech()[1]))
        self.mood = str(prevSpeech()[2])
        self.moodDisplay()
        

    def sendMostRecentCommand(self):
        return self.mostRecentCommand

    def callback(self, event):
        #print("clicked at", event.x, event.y)
        if event.x > 2 and event.x < 400 and event.y >= 0 and event.y < 27:
            self.clearText()
        else:
            self.fileVar.set("Chat with Jorge")
        
        
    def newButton(self, text=None, image=None, visible=True, posx=None, posy=None, font="ariel 9", command=None):
        """
        :param text: Specify text the button displays
        :param visible: Specify whether the button should be visible
        :param posx: Specify x position
        :param posy: Specify y position
        :param command: Specify a command the button carries out when pressed
        :return: Returns the button object
        Create a button
        """
        btn = tk.Button(self.master, text=text, image=image, font=font, command=command)
        if visible:
            btn.place(x=posx, y=posy)
        return btn

    def newLabel(self, text=None, visible=True, posx=None, posy=None, font="ariel 12", textvar=None, imgage=None):
        """
        :param text: Specify text the label displays
        :param visible: Specify whether the label should be visible
        :param posx: Specify x position
        :param posy: Specify y position
        :param font: Specify font
        :return: Returns the label object
        Create a label
        """
        lbl = tk.Label(self.master, text=text, textvariable=textvar, font=font, image=imgage)
        if visible:
            lbl.place(x=posx, y=posy)
        return lbl

    def changeFrame(self, frame):
        """
        :param frame: Specify frame to change to
        Change the frame
        """
        for widget in self.master.winfo_children():
            widget.destroy()
        self.master.change(frame)

        
if __name__ == "__main__":
    app = Mainframe()
    app.mainloop()

