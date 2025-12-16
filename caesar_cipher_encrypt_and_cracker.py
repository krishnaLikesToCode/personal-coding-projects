from collections import Counter
import tkinter as tk
from tkinter import filedialog
import os
hi=str(input("Welcome to my caesar cipher encrypter/cracker.\nPress any key to choose a file, which must have 'encrypt-x' where x is the shift ammount or 'decrypt' as the first line\t"))

rt=tk.Tk()
rt.withdraw()

filedir = filedialog.askopenfilename(initialdir=f"{os.getcwd()}", title="Select the file with the content to view",
filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")) )
file=open(filedir,'r')

t=[]
shifts=[]
alphabet=list("abcdefghijklmnopqrstuvwxyz")
cLine= file.readline()
if "encrypt" in cLine:
    mode="e"
    print('Mode is encrypt')
    if len(cLine) >8:
        shift=int(cLine[8]+cLine[9])
    else:
        shift=int(cLine[8])

elif cLine.strip().lower()=="decrypt":
    mode="d"
    print("Mode is decrypt")
    isConfidenceOn= (input("Confidence score on or off (filters results, and is recommended for sub 100 word inputs)\t")).strip().lower()

    try:
        if isConfidenceOn=="on":
            isConfidenceOn=True
        else:
            isConfidenceOn=False
    except:
        isConfidenceOn=True
else:
    print("File format invalid")
    exit()
cLine=file.readline()
while cLine.strip()!="":
    val=list((cLine.strip().lower()))
    t.append(val)
    cLine=file.readline()




def encryptFunc(plain):
    global alphabet
    for i in range(len(plain)):
        for j in range(len(plain[i])):
            try:
                eLetter= alphabet[((alphabet.index(plain[i][j]))+shift)%26]
                plain[i][j]=eLetter
            except:
                pass
        plain[i]="".join(plain[i])
    return plain

def decryptFunc(plain):
    allLetters=[]
    commonLetters=[]
    mostProbableDecrypts=[]
    lineSpacedVals=[]
    scores=[]
    counts=[]
    for i in range (len(plain)):
        for j in range(len(plain[i])):
            allLetters.append(plain[i][j])
    allLettersCounted= Counter(allLetters)
    mostCommon= allLettersCounted.most_common()
    
    
    for i in range(len(mostCommon)):
        if mostCommon[i][0] != " ":
            commonLetters.append(mostCommon[i][0])
    for i in range(len(mostCommon)):
        commonLetters.append(mostCommon[i][0])
    for i in range(min(10,len(commonLetters))):
        allLettersCopy = allLetters.copy()
        mostProbableDecrypts.append(solveDecryption(allLettersCopy,commonLetters[i]))
    
    for i in range(len(plain)):
        lineSpacedVals.append(mostProbableDecrypts.copy())

    return lineSpacedVals 


def solveDecryption(p,c):
    global alphabet, shifts
    if c not in alphabet:
        shifts.append(0)
        hi="".join(p)
        return hi
    shift= alphabet.index(c) - alphabet.index("e")
    shifts.append(shift)
    for i in range (len(p)):
        if p[i] in alphabet:
            p[i]= alphabet[(alphabet.index(p[i])- shift)%26]
        else:
            pass
    hi="".join(p)
    return hi

#note that this is only for the confidence rating, this is not used in the alogrithm
words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I","it", "for", "not", "on", "with", "he", "as", "you", "do", "at","this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what","so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take","people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also","back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us","is", "are", "was", "were", "had", "been", "has", "did", "shall", "may",
    "might", "must", "should", "cannot", "never", "always", "both", "each", "few", "many","much", "another", "such", "own", "same", "own", "while", "before", "after", "under",
    "again", "above", "below", "between", "during", "without", "within", "among", "against", "toward","upon", "since", "through", "across", "around", "behind", "beyond", "along", "near", "off",
    "per", "via", "than", "except", "although", "though", "however", "therefore", "because", "since","although", "despite", "towards", "amongst", "whether", "whose", "whom", "whose", "which", "what",
    "when", "where", "why", "how", "all", "any", "both", "each", "every", "some","few", "several", "many", "much", "most", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten", "hundred", "thousand", "million", "billion", "trillion","I", "you", "he", "she", "it", "we", "they", "me", "him", "her",
    "us", "them", "my", "your", "his", "her", "its", "our", "their", "mine","yours", "hers", "ours", "theirs", "this", "that", "these", "those", "here", "there",
    "now", "then", "soon", "later", "before", "after", "again", "still", "ever", "never","always", "usually", "sometimes", "often", "once", "twice", "already", "yet", "together", "alone"
]

def getProbRating(g):
    probRating=0
    for i in range(len(words)):
        if words[i] in g:
            probRating+=1
    return probRating

    

if mode =="e":
    print("\n".join(encryptFunc(t)))
else:
    scores=[]
    thing=[]
    v=decryptFunc(t)

    for i in range(len(v[0])):
        if isConfidenceOn:
            scores.append(getProbRating(v[0][i]))
        else:
            scores.append(None)
    
    for i in range(len(v[0])):
        thing.append(f"|'{v[0][i]}'\t | \tShift applied: {shifts[i]%26}\t | \tConfidence: {scores[i]}")
    print("\n")
    if scores[i]!=None:
        thing = sorted(thing, key=lambda x: int(x.split()[-1]), reverse=True)
    thing=list(dict.fromkeys(thing))
    print("\n \n".join(thing))
    
file.close()
