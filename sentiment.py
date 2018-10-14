from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

import io
import sys
import os
from os import path
from tkinter import *
from tkinter import ttk

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'pozitivno.txt')



def myfunction(*event):
    if len(TextArea.get("1.0",END))>1:
        gumb.config(state='normal')
    else:
        gumb.config(state='disabled')

def neutralan():
    for red in io.open(script_dir+"/neutralno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            train.append((str(red),"neutral"))

def negativan(): 
    for red in io.open(script_dir+"/negativno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n").lower()
        if red=="":
            print ()
        else:    
            train.append((str(red),"neg"))

def pozitivan():
    for red in io.open(script_dir+"/pozitivno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            train.append((str(red),"poz"))



def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify() 


train=[]

pozitivan()
negativan()
neutralan()
def analiza():
    cl = NaiveBayesClassifier(train)
    sentence = TextArea.get("1.0",END)
    #sentence = sentence.lower()
    blob = TextBlob(sentence.lower(), classifier=cl)
    blob2 = TextBlob(sentence, classifier=cl)

    neg = 0
    pos = 0
    neu=0
    prozor2=Tk()
    prozor2.title("Riječi iz  analize")
   
    rezultat=ttk.Label(prozor2, anchor=CENTER, justify=CENTER)
    rezultat2=ttk.Label(prozor2,anchor=CENTER, justify=CENTER)

    tree = ttk.Treeview(prozor2,columns=("rečenica"), selectmode="extended")
    scrollbar = Scrollbar(prozor2,orient="vertical")
    tree.delete(*tree.get_children())
    tree.heading('#0', text='rečenica')
    tree.column('#0', width=710)
    
    tree.heading('#1', text='mišljenje', anchor='w')
    tree.column('#1',width=90)

    tree.grid(row=3, column=0, columnspan=6,padx=5,pady=5,  sticky=W+E)
    ##skroler
    scrollbar.grid(sticky=N+S+E, row = 3, column = 0,columnspan=6)
    tree.config(yscrollcommand=scrollbar.set) 
    scrollbar.config(command=tree.yview)

    for s, s2 in zip(blob.sentences, blob2.sentences):
        tree.insert('', 'end', text=s2,values=s.classify())
        if (s.classify()=="neutral"):
            neu+=1
        elif (s.classify()=="poz"):
            pos+=1
        else:
            neg+=1


    rezultat.grid(row=0,column=0,sticky=W+E, columnspan=6)
    rezultat.config(text="broj pozitivnih riječi: " +  str(pos) +", broj negativnih riječi: "+ str(neg)+", broj neutralnih riječi: "+ str(neu))

    poziti=float(format(float(pos)/(pos+neg+neu),'.2f'))*100
    nega=float(format(float(neg)/(pos+neg+neu),'.2f'))*100
    neutra=float(format(float(neu)/(pos+neg+neu),'.2f'))*100

    rezultat2.grid(row=1,column=0,sticky=W+E,columnspan=6)
    rezultat2.config(text="pozitivnost: " +  str(poziti) +"%, negativnost: "+str(nega)+"%, neutralnost: "+ str(neutra)+"%")
    prozor2.mainloop()

prozor=Tk()

TextArea = Text()
ScrollBar = ttk.Scrollbar(prozor)
ScrollBar.config(command=TextArea.yview)
TextArea.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
TextArea.pack(expand=YES, fill=BOTH)
gumb=ttk.Button(prozor, text="analiziraj", command=analiza)
gumb.pack()
gumb.config(state='disabled')



prozor.bind_class("Text","<Leave>",myfunction)
prozor.title("Analiza mišljenja")
"""prozor.iconbitmap(r"favicon.ico")"""


center(prozor)

prozor.resizable(False, False)
prozor.mainloop()