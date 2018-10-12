from tkinter import *
from tkinter import ttk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import io
 
def pozitivan():
    positive_vocab=[]
    for red in io.open("pozitivno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            positive_vocab.append(str(red))
    return positive_vocab

def neutralan():   
    neutral_vocab=[]
    for red in io.open("neutralno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            neutral_vocab.append(str(red))
    return neutral_vocab

def negativan(): 
    negative_vocab=[]
    for red in io.open("negativno.txt","r", encoding="utf-8-sig"):
        red=red.strip("\n")
        if red=="":
            print ()
        else:    
            negative_vocab.append(str(red))
    return negative_vocab


def word_feats(words):
    return dict([(word, True) for word in words])


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


positive_vocab=pozitivan()
negative_vocab=negativan()
neutral_vocab= neutralan()

#print (positive_vocab)
#print (negative_vocab)
#print (neutral_vocab)

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]


def myfunction(*event):
    if len(TextArea.get("1.0",END))>1:
        gumb.config(state='normal')
    else:
        gumb.config(state='disabled')


def analiza():
    train_set = negative_features + positive_features + neutral_features
    classifier = NaiveBayesClassifier.train(train_set) 
    # Predict
    neg = 0
    pos = 0
    neu = 0
    sentence = TextArea.get("1.0",END)
    sentence = sentence.lower()
    sentence=sentence.replace(".","").replace(",","").replace("?","").replace("!","")
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify(word_feats(word))
<<<<<<< HEAD
=======
        print(classResult)
>>>>>>> master
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1
        if classResult == 'neu':
            neu = neu + 1
    rezultat.pack()
<<<<<<< HEAD
    rezultat.config(text="Pozitivno: " +  str(float(pos)/len(words)) +"% Negativno: "+ str(float(neg)/len(words))+"%")
=======


    poziti=float(format(float(pos)/len(words),'.2f'))*100
    nega=float(format(float(neg)/len(words),'.2f'))*100
    neutra=float(format(float(neu)/len(words),'.2f'))*100
    rezultat.config(text="Pozitivno: " + str(poziti) +"% Negativno: "+ str(nega) +"%"+" Neutralno: "+ str(neutra) +"%")

>>>>>>> master

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

rezultat=ttk.Label(prozor)

prozor.bind_class("Text","<Leave>",myfunction)
prozor.title("Analiza mišljenja")
prozor.iconbitmap(r"favicon.ico")
prozor.resizable(False, False)

prozor.mainloop()