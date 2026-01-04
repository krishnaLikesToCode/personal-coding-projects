while True:
    eOrD=str(input("Encrypt or decrypt? \t").strip().lower())
    if eOrD=="encrypt":
 
        plain= (str(input("\n \n \nEnter the plaintext \t")).strip().lower())
        plain=plain.replace(" ", "")
        plain=list(plain)
        key=(str(input("Enter your keyword \t")).strip().lower())
        key=key.replace(" ","")
        key=list(key)
        numbers=[]
        for i in range(26):
            numbers.append(i)

        def vCipher(p,k):
            global numbers
            alpha= list("abcdefghijklmnopqrstuvwxyz")
            encrypt=[]
            kList=[]
            for i in range(len(p)):
                kList.append(k[i%len(k)])
    
            for j in range(len(p)):
                
                numValP= numbers[alpha.index(p[j])]
                numValK= numbers[alpha.index(kList[j])]
                l= (numValP+numValK)%26
                letterValE= alpha[numbers.index(l%26)]
                encrypt.append(letterValE)

            return ("".join(encrypt))
        print(f"\n \n The encrypted word is: {vCipher(plain,key)}")

    elif eOrD=="decrypt":
        encrypt= (str(input(" \n \n \nEnter the encrypted word \t")).strip().lower())
        encrypt=encrypt.replace(" ","")
        encrypt=list(encrypt)
        key=(str(input("Enter the keyword \t")).strip().lower())
        key=key.replace(" ","")
        key=list(key)
        numbers=[]
        for i in range(26):
            numbers.append(i)

        def vCipher(p,k):
            global numbers
            alpha= list("abcdefghijklmnopqrstuvwxyz")
            decrypt=[]
            kList=[]
            for i in range(len(p)):
                kList.append(k[i%len(k)])
    
            for j in range(len(p)):
           
                numValP= numbers[alpha.index(p[j])]
                numValK= numbers[alpha.index(kList[j])]
                l= (numValP-numValK)%26
                letterValD= alpha[numbers.index(l%26)]
                decrypt.append(letterValD)

            return ("".join(decrypt))
        print(f"\n \n The decrypted word is: {vCipher(encrypt,key)}")
    else:
        continue