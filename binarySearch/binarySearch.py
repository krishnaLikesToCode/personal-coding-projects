v= str(input("What letter you looking for? \t")).strip().lower()
v=v[0]
n = [
    "alpha", "alt", "apple", "apricot",
    "banana", "band", "beta", "blueberry",
    "cat", "car", "cherry", "cobra",
    "dog", "delta", "dove", "dragonfruit",
    "elephant", "echo", "emerald",
    "falcon", "fig", "fish",
    "goat", "gamma", "grape",
    "horse", "hotel", "hydra",
    "iguana", "iris", "iron",
    "jaguar", "jade", "jelly",
    "kangaroo", "kiwi", "kilo",
    "lemon", "lion", "lotus",
    "mango", "melon", "mouse",
    "nectar", "neon", "night",
    "omega", "orange", "owl",
    "panda", "peach", "pear", "plum", "python",
    "quartz", "queen", "quill",
    "rabbit", "radar", "rose",
    "snake", "solar", "strawberry", "sun",
    "tiger", "tomato", "tulip",
    "umbrella", "uranium", "ursa",
    "violet", "viper", "volcano",
    "wolf", "walnut", "watermelon",
    "xenon", "xerox", "xylophone",
    "yak", "yellow", "yogurt",
    "zebra", "zephyr", "zinc"
]

j=[]
t=0
m=0
a= list("abcdefghijklmnopqrstuvwxyz")
l= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
for i in range(len(n)):
    for k in range(len(a)):
        if a[k]== n[i][0]:
            j.append(a[k])
def cMedian():
    global n,v,t,j,m

    if len(j) == 0:       
        print(f"Done! Found {m} results")
        return

    t= len(j)//2
    if len(j) ==1 and j[t]!=v:
        exit()
    if j[t]==v:
        print(f"Found {n[t]}")
        m+=1
        del n[t]
        del j[t]
        cMedian()

    elif j[t] >v:
        n=n[:t]
        j=j[:t]
        cMedian()
        
    elif j[t]<v:
        n=n[t+1:]
        j=j[t+1:]
        cMedian()
   
    
cMedian()


