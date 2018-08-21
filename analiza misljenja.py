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

"""
negative_vocab = ['loš', 'užasan', 'beskoristan', 'zločest', 'zloča', 'zlo', ':(', 'tužan', 'smrt', 'opasnost', 'opasan', 'lijen', 'mrzim', 'mržnja', 'glupo', 'besmisleno', 'besmislen', 'besmislenost', 'složeno', 'nejasno', 'zbunjen', 'zbunjujuće', 'tužno', 'tužan', 'tuga', 'bol', 'bolestan', 'boležljiv', 'istrebljenje', 'rasizam', 'seksizam', 'mobing', 'zlostavljanje', 'droga', 'negativno', 'negativan', 'zbunjeno', 'nejasno', 'bol', 'bolest', 'uvreda', 'vrijeđati', 'omaložavanje', 'ignoriranje', 'sramota', 'sramoćenje', 'grozan', 'grozota', 'genocid', 'rat', 'borba', 'nasilje', 'loš', 'preloš', 'oružje']
positive_vocab = [ 'dobar', 'dobro', 'izvrsno', 'pozitivno', 'pozitivan', 'odličan', 'solidan', ':)', 'trud', 'rad', 'lijep', 'predobar', 'prelijep', 'božanstven', 'Bog','koristan','lijep',"ljubav", "marljiv","voli"]
neutral_vocab = ['film','škola','osoba','zgrada','je','i','ali','pa','neka','ovaj','taj','to',"ići","u"]
"""


positive_vocab=pozitivan()
negative_vocab=negativan()
neutral_vocab= neutralan()

print (positive_vocab)
print (negative_vocab)
print (neutral_vocab)

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
    sentence = TextArea.get("1.0",END)
    sentence = sentence.lower()
    sentence=sentence.replace(".","").replace(",","").replace("?","").replace("!","")
    words = sentence.split(' ')
    for word in words:
        classResult = classifier.classify( word_feats(word))
        if classResult == 'neg':
            neg = neg + 1
        if classResult == 'pos':
            pos = pos + 1
    
    print('Positive: ' + str(float(pos)/len(words)))
    print('Negative: ' + str(float(neg)/len(words)))
    rezultat.pack()
    rezultat.config(text="Pozitivno: " + str(round(float(pos)/len(words),2)*100)+"% Negativno: "+ str(round(float(neg)/len(words),2)*100)+"%")

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
"""prozor.iconbitmap(r"favicon.ico")"""
prozor.resizable(False, False)
prozor.mainloop()