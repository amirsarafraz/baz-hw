#38
def weak ():
    a=int(input())
    
    if a<=30 and a >0 :
        if a<8:
            return "1"
        elif a>=8 and a <=14:
           return "2" 
        elif a>=15 and a <=21:
           return "3" 
        elif a>=22 and a <=28:
           return "4" 
        elif a>=29 and a <=30:
           return "5"

print(weak())