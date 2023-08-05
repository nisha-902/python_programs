a=int(input("enter the 1 number:"))
b=int(input("enter the 2 number:"))
c=input("eneter which oper you wanna perform?:")

if(c=="+"):
   if(a==56 and b==9):
    print("77")
   else:
       print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    if(a==45 and b==3):
        print("555")
    else:
        print(a*b)
elif(c=="/"):
    if(a==56 and b==4):
        print("4")
    else:
        print(a/b)
else:
    print("can't perform")
    
