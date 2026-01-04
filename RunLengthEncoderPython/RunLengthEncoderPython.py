import os

FILE=open("fileToUse.txt","r")
FILECONTENT=[]
COMPRESSED=[]


for LINE in FILE:
    FILECONTENT.append(LINE.strip().lower())
FILE.close()

ORIGINAL=FILECONTENT

def RLE(PLAIN):
    ENCODED=[]
    i=0
    while i < len(PLAIN):
        LETTER= PLAIN[i]
        k=i
        NUMBEROF=0
        while k <len(PLAIN) and PLAIN[k] == PLAIN[i]:
            NUMBEROF+=1
            k+=1
        ENCODED.append((f"{NUMBEROF}{PLAIN[i]}"))
        i+= ((k-i))
    return ENCODED

def FORMATANDPRINT(FILECONTENT,MODE):
    ORIGINAL=(FILECONTENT).copy()
    if MODE=="encode":
        COMPRESSED=[]
        for i in range(len(FILECONTENT)):
            FILECONTENT[i]=RLE(FILECONTENT[i])

        for i in range(len(FILECONTENT)):
            COMPRESSED.append("".join(FILECONTENT[i]))
        print(f"ASCII size of decompressed was {CALCULATEASCIISIZE(ORIGINAL)} bits. The new size of the compressed is {CALCULATEASCIISIZE(COMPRESSED)} bits. \n \n \n")
        WRITETOFILE(COMPRESSED,MODE)
    else:
        FILECONTENT=dRLE(FILECONTENT)
        DECOMPRESSED=[]
        for i in range(len(FILECONTENT)):
            DECOMPRESSED.append("".join(FILECONTENT[i]))
        print(f"ASCII size of compressed was {CALCULATEASCIISIZE(ORIGINAL)} bits. The new size of the decompressed is {CALCULATEASCIISIZE(DECOMPRESSED)} bits. \n \n \n")
        WRITETOFILE(DECOMPRESSED,MODE)
        

def CALCULATEASCIISIZE(val):
    return len("".join(val))*8

def dRLE(FILECONTENT):
    NUMBERS=['1','2','3','4','5','6','7','8','9','0']
    DECODED = [[] for i in range(len(FILECONTENT))]

    for i in range(len(FILECONTENT)):
        NUMBEROF =[]
        for j in range(len(FILECONTENT[i])):
            if FILECONTENT[i][j] in NUMBERS:
                NUMBEROF.append(FILECONTENT[i][j])
            else:
                CLETTER=FILECONTENT[i][j]
                AMM=int("".join(NUMBEROF))
                for k in range(AMM):
                    DECODED[i].append(CLETTER)
                NUMBEROF=[]

    return DECODED



def WRITETOFILE(WRITELIST,MODE):
    if MODE=="encode":
        WRITEFILE=open("compressedFile.txt","w")
        os.startfile("compressedFile.txt")
    else:
        WRITEFILE=open("decompressedFile.txt","w")
        os.startfile("decompressedFile.txt")
    for i in range(len(WRITELIST)):
        WRITEFILE.write(f"{WRITELIST[i]} \n")



while True:
    MODE=str(input("Encode or Decode?\t"))
    if MODE== "encode" or MODE =="decode":
        break
    else:
        continue

FORMATANDPRINT(FILECONTENT,MODE)  