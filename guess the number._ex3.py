def game(n):
    guess=1
    while(guess<=10):
        a=int(input("guess the no."))
        if a<n:
            print("inc the no.")
        elif a>n:
            print("dec the no.")
        else:
            print("you won")
            print(guess,"round took to finish")
            break
        print(10-guess, "round left")
        guess+=1
    if guess>10:
        print("over")

game(80)    

'''
n=90
a=int(input("guess the no."))
guess=1

while True:
    if a==n:
        print(f"you win the game with {guess} guesses")
        break
    else:
        if a<n:
            if guess==4:
                print("over")
                break
            else:
                    print("inc your no")
            guess+=1
            a=int(input("guess again"))
        else:
            if guess==4:
                print("over")
                break
            else:
                print("dec your no>")
            guess+=1
            a=int(input("guess again"))
            
'''






'''
print("guess the no., you can only try 4 gusses")
number=int(90)
a=int(input("enter your no:"))
guess=1
if a==number:
    print("you win")  
else:
    if a<number:
        print("inc your no.")
        while guess<5:
            a=int(input("guess again:"))
            if a==number:
                print(f"you win, you guesses it in {guess} round")
                break
            if a<number:
                if guess==4:
                    print("over")
                else:
                    print("inc your no.")
            elif a>number:
                if guess==4:
                    print("over")
                else:
                    print("dec your no.")
            guess+=1
    else:
        print("dec your n.")
        while guess<5:
            a=int(input("guess again:"))
            if a==number:
                print(f"you win, and you gusses it in {round} round")
                break
            if a<number:
                if guess==4:
                    print("over")
                else:
                    print("inc your no.")
            elif a>number:
                if guess==4:
                    print("over")
                else:
                    print("dec your no.")
            guess+=1
'''        
            
      
            
        
          
            
    
    
        
    
