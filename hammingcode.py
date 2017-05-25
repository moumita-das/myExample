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
    #pos=random.randint(0,l)
    pos=4
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
                print(str(j)+" "+str(xorans)+" "+msgSent[j-1])
        if(flag==1):
            strxorans=strxorans+str(xorans)
            print(strxorans+", "+str(xorans))
        x+=1
    else:
        msg=msg+msgSent[i-1]
    i+=1
strxorans=strxorans[::-1]
wrong=int(strxorans,2)
msg=msg[::-1]
print(msg)
if(wrong!=0):
    print(strxorans)
    if(msg[wrong-1]=='1'):
        msg=msg[:wrong]+"0"+msg[wrong+1:]
    else:
        msg=msg[:wrong]+"1"+msg[wrong+1:]

print(msg)

            
