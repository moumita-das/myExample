n=input("Enter message : ")
l=len(n)
i=0
slices=[]
x=0
k=4
checksum=0
msgSent=n
while(i<l):
    slices.append(n[i:i+k])
    checksum=checksum | int(slices[x],2)
    x+=1
    i=i+k
checksum=str(bin(checksum))
checksum=checksum[checksum.find('b'):]
for i in range(0,len(checksum)):
    if(checksum[i]=='1'):
        checksum=checksum[:i]+'0'+checksum[i+1:]
    else:
        checksum=checksum[:i]+'1'+checksum[i+1:]
msgSent=msgSent+checksum
slices.append(checksum)
print("Message sent : "+str(slices))
l=len(msgSent)
i=l
checksum=0
x=0
while(i<l):
    checksum=checksum|int(slices[x],2)
    x+=1
    i+=k
if(checksum==0):
    print("Correct transmission: ")
    print("Message received : "+msgSent[:l-k])
