from tkinter import *
from tkinter import ttk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import io
 
def word_feats(words):
    return dict([(word, True) for word in words])
#negative_vocab = [ 'loš', 'užasan','beskoristan', 'zločest', ':(', "tužan", "smrt","lijen"]
#positive_vocab = [ 'dobar', 'dobro', 'izvrsno', 'pozitivno', 'pozitivan', 'odličan', 'solidan', ':)', 'trud', 'rad', 'lijep', 'predobar', 'prelijep', 'božanstven', 'Bog','koristan','lijep',"ljubav", "marljiv","voli"]
#neutral_vocab = [ 'film','škola','osoba','zgrada','je','i','ali','pa','neka','ovaj','taj','to',"ići","u"]
positive_vocab=[]
neutral_vocab=[]
negative_vocab=[]
for red in io.open("pozitivno.txt","r+",encoding='utf8'):
    red=red.strip("\n")
    positive_vocab.append(str(red.encode("utf-8")).strip("b'"))



for red in io.open("neutralno.txt","r+",encoding='utf8'):
    red=red.strip("\n")
    neutral_vocab.append(str(red.encode("utf-8")).strip("b'"))

for red in io.open("negativno.txt","r+",encoding='utf8'):
    red=red.strip("\n")
    negative_vocab.append(str(red.encode("utf-8")).strip("b'"))

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
prozor.iconbitmap(r"favicon.ico")
prozor.resizable(False, False)
prozor.mainloop()