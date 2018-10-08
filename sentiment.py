from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import io
import sys
import os
from os import path
from tkinter import *
from tkinter import ttk






def myfunction(*event):
    if len(TextArea.get("1.0",END))>1:
        gumb.config(state='normal')
    else:
        gumb.config(state='disabled')

def pozitivan():
    for red in io.open("pozitivno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            train.append((str(red),"poz"))


def negativan(): 
    for red in io.open("negativno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            train.append((str(red),"neg"))


train=[]


def analiza():
    pozitivan()
    negativan()
    cl = NaiveBayesClassifier(train)
    sentence = TextArea.get("1.0",END)
    #sentence = sentence.lower()
    blob = TextBlob(sentence, classifier=cl)
    neg = 0
    pos = 0
    prozor2=Tk()
    prozor2.title("Riječi iz  analize")
   
    rezultat=ttk.Label(prozor2)
    tree = ttk.Treeview(prozor2,columns=("rečenica"), selectmode="extended")
    scrollbar = Scrollbar(prozor2,orient="vertical")
    tree.delete(*tree.get_children())
    tree.heading('#0', text='rečenica')
    tree.column('#0', width=710)
    
    tree.heading('#1', text='mišljenje', anchor='w')
    tree.column('#1',width=70)

    tree.grid(row=3, column=0, columnspan=6,padx=5,pady=5,  sticky=W+E)
    ##skroler
    scrollbar.grid(sticky=N+S+E, row = 3, column = 0,columnspan=6)
    tree.config(yscrollcommand=scrollbar.set) 
    scrollbar.config(command=tree.yview)

    for s in blob.sentences:
        print(s)
        print (s.classify())
        tree.insert('', 'end', text=s,values=s.classify())
        if (s.classify()=="poz"):
            pos+=1
        else:
            neg+=1
    rezultat.grid(row=0,column=0,)
    rezultat.config(text="broj pozitivnih riječi: " +  str(pos) +", broj negativnih riječi: "+ str(neg))
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
prozor.resizable(False, False)
prozor.mainloop()