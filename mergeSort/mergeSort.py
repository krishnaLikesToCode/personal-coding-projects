myList = []
hi= int(input("This is a merge sort algo. \n \n Enter the length of your list \t"))
for i in range(hi):
    p=int(input(f"Enter number {i+1} in the list \t"))
    myList.append(p)
nList = []
fList=[]
def recurSplit(listy):
    global nList
    if len(listy) == 1: # if is only one number/index
        nList.append( [listy[0]] )   # append to nList
        return

    elif len(listy) % 2 != 0: #if list is odd lenght indexes, will yeet index[0]
        nList.append([listy[0]])
        recurSplit(listy[1:]) 
    else: 
        mid = len(listy) // 2
        recurSplit(listy[:mid])
        recurSplit(listy[mid:])# the RECURSIVE part, extremley difficult oh my god its sooooo hard
def merge(l):
    global fList
    if len(l) ==1: # if list is only 1 in length
        return l # list is done
    mList=[] #yet another list, i must be bad at this
    for i in range(0,len(l),2): #heres the "fun" stuff
        if i+1 < len(l): #if there is a pair
            pair= sorted(l[i] + l[i+1]) # sort them if needed
            mList.append(pair) #append
        else:# if there is an odd number/ alone index
            mList.append(l[i]) # append it

            
    return merge(mList) #do it again until list length is 1
def flip(s):
    for i in range(len(s[0])//2):
        s[0][i], s[0][-1*(i+1)] = s[0][-1*(i+1)], s[0][i]
    return(s)

recurSplit(myList)
merge(nList)
fList=merge(nList)
print(f"Your list merged is \n {fList} \n or \n {flip(fList)}")
