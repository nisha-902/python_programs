n=int(input("enter the no of rows:"))
print("enter 1 or 0")
bool_v=input("enter:")
if bool_v=="1":
    for i in range(0,n+1):
        print("*"*i)
else:
    for i in range(n+1,0,-1):
        print("*"*i)
