
img=[[65,251,154,127,78,190,79],
     [208,211,178,157,204,226,204],
     [231,19,8,215,213,193,210],
     [73,222,201,40,48,171,255],
     [233,124,70,61,198,123,14]]

s=[]    
for y in range(0,len(img)):
    step=[]
    for x in range(0,len(img[y])):
        step+=[0]
    s+=[step]


for y in range(0,len(img)):      #calculate  
    for x in range(0,len(img[y])):
        s[y][x]=img[y][x]+s[y][x-1]+s[y-1][x]-s[y-1][x-1]

max=0

for y in range(0,len(img)):   #find less342 and maximun value 
    for x in range(0,len(img[y])):
        if s[y][x]>max and s[y][x]<342:
            max=s[y][x]

for x in s:
    print(x)
print(max)
