s = input("Enter the word : ")
lower,upper = 0,0
for i in s: 
     if (i>='A'and i<='Z'): 
        upper =upper+1 
    
     if (i>='a'and i<='z'): 
        lower = lower+1 
        
if (upper > lower):
    print(s.upper())
else:
    print(s.lower())