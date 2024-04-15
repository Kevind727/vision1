img=[[65,251,154,127,78,190,79],
     [208,211,178,157,204,226,204],
     [231,19,8,215,213,193,210],
     [73,222,201,40,48,171,255],
     [233,124,70,61,198,123,14]]


new_img=[]     #adding rows and columns of 0
for y in range(0,13):   
    step=[]
    for x in range(0,14):
        step+=[0]
    new_img+=[step]
  
for y in range(0,len(img)):
    for x in range(0,len(img[y])):
        new_img[y+3][x+3]+=img[y][x]


filte=[[1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0]]

result=[]    
for y in range(0,len(img)):
    step=[]
    for x in range(0,len(img[y])):
        step+=[0]
    result+=[step]


for y in range(0,len(result)):           #filter calculate
    for x in range(0,len(result[y])):
        
        sum=0
        for yy in range(8):
            for xx in range(8):
                sum+=filte[yy][xx]*new_img[y+yy][x+xx]
        
        result[y][x]=sum


s=[]    
for y in range(0,len(result)):
    step=[]
    for x in range(0,len(result[y])):
        step+=[0]
    s+=[step]



for y in range(0,len(result)):      #calculate  
    for x in range(0,len(result[y])):
        s[y][x]=result[y][x]+s[y][x-1]+s[y-1][x]-s[y-1][x-1]


max=-10000
for y in range(0,len(img)):   #find less -81 and maximun value 
    for x in range(0,len(img[y])):
        if s[y][x]>max and s[y][x]<-81:
            max=s[y][x]


print(max)
