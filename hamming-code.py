msg=input("Enter data to be sent : ")
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
r_arr=['r1','r2','0','r4','0','0','0','r8']
r1=[1,3,5,7,9,11,13,15]
r2=[2,3,6,7,10,11,14,15]
r4=[4,5,6,7,12,13,14,15]
r8=[8,9,10,11,12,13,14,15]
while(i<=l):
    if(msgSent[i-1]=='r'):
        c=i
        while(c<l):
            while(c<c+i):
                if(c==l):
                    flag=1
                    break
                r=r^int(msgSent[c])
            if(flag==1):
                break
            
                
print  ("Message transmitted : "+msgSent)
