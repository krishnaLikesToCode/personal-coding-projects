#   NOTE- uses external library PIL, run as super-user in terminal: pip install PIL           or          pip3 install PIL
from PIL import Image
import tkinter
import os
from tkinter import filedialog

root = tkinter.Tk()#IGNORE
root.withdraw()#IGNORE

def getBinaryPixelData(img):#takes arg of image dir, gets raw binary data, replaces 0s and 1s with x and y
    binaryData=[]
    row2=[]
    for i in range(img.height):
        row=[]
        for j in range(img.width):
            row.append(str(img.getpixel((j,i))//255))
        row2 = "".join(row)
        row2=row2.replace("0","x").replace("1","y")
        binaryData.append(row2)

    return binaryData

def encodeImageData(pixelData):#takes arg of raw pixel data, encodes it and returns
    encoded=[]
    file=open("compressedImageData.txt","w")
    for i in range(len(pixelData)):
        encoded.append("".join(RLE(pixelData[i])))
        
    return encoded

def RLE(PLAIN):# takes arg of data to encode, run length encodes raw binary data 
    ENCODED=[]
    i=0
    while i < len(PLAIN):
        LETTER= PLAIN[i]
        k=i
        NUMBEROF=0
        while k <len(PLAIN) and PLAIN[k] == PLAIN[i]:
            NUMBEROF+=1
            k+=1
        if NUMBEROF==1:
            ENCODED.append((f"{PLAIN[i]}"))
        else:
            ENCODED.append((f"{NUMBEROF}{PLAIN[i]}"))
        i+= ((k-i))
    return ENCODED

def writeToFile(stuffToWrite):#takes arg of thing to be written, overwrites to file
    file= open("compressedImageData.txt","w")
    for i in range(len(stuffToWrite)):
        file.write(f"{stuffToWrite[i]}|")
    file.close()

def readCompressedFile(fileDir):#takes arg of user file dir, reads file then writes contents to list
    fileData=[]
    file=open(fileDir,"r")
    fileData=file.read().strip()
    file.close
    return fileData.split("|")


def dRLE(FILECONTENT):# takes arg of encoded pixel data, decodes numbers and returns in x y format
    NUMBERS=['1','2','3','4','5','6','7','8','9','0']
    DECODED = [[] for i in range(len(FILECONTENT))]

    for i in range(len(FILECONTENT)):
        NUMBEROF =[]
        for j in range(len(FILECONTENT[i])):
            if FILECONTENT[i][j] in NUMBERS:
                NUMBEROF.append(FILECONTENT[i][j])
            else:
                CLETTER=FILECONTENT[i][j]
                try:
                    AMM=int("".join(NUMBEROF))
                except:
                    AMM=1
                for k in range(AMM):
                    DECODED[i].append(CLETTER)
                NUMBEROF=[]

    return DECODED

def decodeImageData(theList):   # takes arg of encoded list, calls dRLE to get decoded format, replaces x with 0, y with 1, removes \n then integerises
    nList=dRLE(theList)
    for i in range(len(nList)):
        nList[i]= "".join(nList[i]).replace("x","0").replace("y","1").replace("|","")
    
    for l in range(len(nList)):
        nList[l] = [int(char) * 255 for char in nList[l]]
    return nList

def convertToImage(pixelStates):    # takes arg of binary pixel data/states (0 and 255) and turns into an image
    convertedImage=Image.new("1", (len(pixelStates[0]),len(pixelStates)),color=1)
    for i in range(len(pixelStates)):
        for j in range(len(pixelStates[i])):
            convertedImage.putpixel((j,i),pixelStates[i][j])
    convertedImage.show()


#main code
eOrD= str(input("Compress or decompress file?\t"))
if eOrD.strip().lower() == "compress":
    while True:
        imgDir=filedialog.askopenfilename(title="SELECT AN IMAGE FILE",filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
)
        try:
            cool = Image.open(imgDir).convert("1")
            writeToFile(encodeImageData(getBinaryPixelData(cool)))
            os.startfile("compressedImageData.txt")
            break
        except FileNotFoundError:
            print("Invalid file- maybe you misspelt the name or file extension?\n")
            continue
else:
    fileDir= filedialog.askopenfilename(title="SELECT A COMPRESSED IMAGE DATA FILE",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    convertToImage(decodeImageData(readCompressedFile(fileDir)))
print("\n \n \nDone!")
    





