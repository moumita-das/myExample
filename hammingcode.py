##hammingcode for a binary string of any length 

import random
msg=input("Enter data to be sent : ")
#sender's side
m=len(msg)
r=0
while(2**r<=(m+r+1)):
    r+=1
l=m+r
i=0
c=0
msgSent=""
while(i<l):
    if((l-i)==2**(r-1)):
        msgSent=msgSent+"r"
        r-=1
    else:
        msgSent=msgSent+msg[c]
        c+=1
    i+=1
msgSent=msgSent[::-1]
i=1
x=1
while(i<l+1):
    if(msgSent[i-1]=='r'):
        xorans=0
        for j in range(i+1,l+1):
            if(msgSent[j-1]=='r'):
                continue
            jbit=str(bin(j))
            jbit=jbit[jbit.find('b')+1:]
            jbit=jbit[::-1]
            if(jbit[x-1]=='1'):
                xorans=int(int(msgSent[j-1],2)^xorans)
        x+=1
        msgSent=msgSent[:i-1]+str(xorans)+msgSent[i:]
    i+=1
msgSent=msgSent[::-1]
error=input("Do you want to introduce error? (y/n)")
if(error=='y'):
    pos=random.randint(0,l)
    if(msgSent[pos]=='1'):
        msgSent=msgSent[:pos]+"0"+msgSent[pos+1:]
    else:
        msgSent=msgSent[:pos]+"1"+msgSent[pos+1:]
print("Message transmitted : "+msgSent)
#receiver's side
l=len(msgSent)
msgSent=msgSent[::-1]
i=1
x=1
msg=""
strxorans=""
while(i<l+1):
    if(2**(x-1)==i):
        xorans=0
        flag=0
        for j in range(i,l+1):
            jbit=str(bin(j))
            jbit=jbit[jbit.find('b')+1:]
            jbit=jbit[::-1]
            if(jbit[x-1]=='1'):
                flag=1
                xorans=int(int(msgSent[j-1],2)^xorans)
        if(flag==1):
            strxorans=strxorans+str(xorans)
        x+=1
    i+=1
strxorans=strxorans[::-1]
wrong=int(strxorans,2)
x=1
i=1
if(wrong!=0):
    print("error at : "+str(wrong+1)+" position")
    if(msgSent[wrong-1]=='1'):
        msgSent=msgSent[:wrong-1]+"0"+msgSent[wrong:]
    else:
        msgSent=msgSent[:wrong-1]+"1"+msgSent[wrong:]
    print("Corrected transmission : "+msgSent)
while(i<l+1):
    if(2**(x-1)!=i):
        msg=msg+msgSent[i-1]
    else:
        x+=1
    i+=1
msg=msg[::-1]
print("Message received : "+msg)
