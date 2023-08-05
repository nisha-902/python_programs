import datetime
def getdate():
    return datetime.datetime.now()
def log(arg):
    if arg==1:
        x=int(input("press 1 for excercise and 2 for food"))
        if x==1:
            info=input("type some thing here\n")
            with open("nisha_ex.txt","a")as file:
                file.write(str([str(getdate())])+": "+info+"\n")
                print("file updated successfully")
        else:
            info=input("type something here\n")
            with open("nisha_food.txt","a")as file:
                file.write(str([str(getdate())])+": "+info+"\n")
                print("file updated successfully")
    elif arg==2:
        x=int(input("press 1 for excercise and 2 for food"))
        if x==1:
            info=input("type some thing here\n")
            with open("sandy_ex.txt","a")as file:
                file.write(str([str(getdate())])+": "+info+"\n")
                print("file updated successfully")
        else:
            info=input("type something here\n")
            with open("sandy_food.txt","a")as file:
                file.write(str(str[(getdate())])+": "+info+"\n")
                print("file updated successfully")
    elif arg==3:
        x=int(input("press 1 for excercise and 2 for food"))
        if x==1:
            info=input("type some thing here\n")
            with open("ashish_ex.txt","a")as file:
                file.write(str(str([(getdate())]))+": "+info+"\n")
                print("file updated successfully")
        else:
            info=input("type something here\n")
            with open("ashish_food.txt","a")as file:
                file.write(strstr[(getdate())]+": "+info+"\n")
                print("file updated successfully")
    else:
        print("enter valid input")
def ret(arg):
    if arg==1:
        x=int(input("1 for excercise and 2 for food"))
        if x==1:
            with open("nisha_ex.txt")as file:
                for i in file:
                    print(i, end=" ")
        else:
            with open("nisha_food.txt")as file:
                for i in file:
                    print(i, end=" ")
    elif arg==2:
        x=int(input("1 for excercise and 2 for food"))
        if x==1:
            with open("sandy_ex.txt")as file:
                for i in file:
                        print(i, end=" ")
        else:
            with open("sandy_food.txt")as file:
                for i in file:
                    print(i, end=" ")
    elif arg==3:
        x=int(input("1 for excercise and 2 for food"))
        if x==1:
            with open("ashish_ex.txt")as file:
                for i in file:
                    print(i, end=" ")
        else:
            with open("ashish_food.txt")as file:
                for i in file:
                    print(i, end=" ")
    else:
        print("enter valid input")

#entry point       
print("This is my Health Managaement System") 
#taking user input
a=int(input("press 1 for log the value and 2 for retrieve"))
if a==1:
    n=int(input("press 1 for Nisha 2 for Sandy and 3 for Ashish"))
    log(n)
else:
    n=int(input("press 1 for Nisha 2 for Sandy and 3 for Ashish"))
    ret(n)
        
