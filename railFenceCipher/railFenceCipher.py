
def encryption(key,plaintext):
    assortedList=[]
    for i in range(key):
        assortedList.append([])
    for i in range(0,len(plaintext)):
        assortedList[i%key].append(plaintext[i])
    print(assortedList)
    finalList=[]
    for i in range(key):
        for j in range(len(assortedList[i])):
            finalList.append(assortedList[i][j])
    return finalList

def decryption(key,encrypt):
    assortedList=[]
    lengths=[]
    decryptList=[]
    finalList=[]
    startAt=0
    for i in range(key):
        assortedList.append([])
    for i in range(len(encrypt)):
        assortedList[i%key].append(encrypt[i])
    for i in range(len(assortedList)):
        lengths.append(len(assortedList[i]))
    for i in range(len(lengths)):
        decryptList.append([])
    for i in range(len(lengths)):
        for j in range(lengths[i]):
            decryptList[i].append(encrypt[j+startAt])
        startAt+=lengths[i]
    for i in range(max(lengths)):
        for j in range(len(lengths)):
            try:
                finalList.append(decryptList[j][i])
            except:
                pass
    return finalList

eOrD=input("Encrypt or decrypt?\t")
if eOrD.strip().lower() == "encrypt":
    hello=str(input("Enter your plaintext\t"))
    key=int(input("Enter your key amount\t"))
    print(f"Ciphertext: {"".join(encryption(key,hello))}")
else:
    hello=str(input("Enter your encrypted text\t"))
    key=int(input("Enter the key used on it\t"))
    print(f"Plaintext: {"".join(decryption(key,hello))}")
