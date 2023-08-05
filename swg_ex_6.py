import random

l=["s","w","g"]
chance=10
human=0
comp=0
no_of_ch=0
while no_of_ch<chance:
    a=input("s,w,g?:")
    b=random.choice(l)
    #you and comp enterd same
    if a==b:
        print("tie and both got 0 mark")
        print(f"you guess {a} and comp guess {b}")
    #you enterd g
    elif a=="g" and b=="s":
        human+=1
        print(f"you got {human} marks")
        print(f"you guess {a} and comp guess {b}")
    #comp enterd s
    elif a=="s" and b=="g":
        comp+=1
        print(f"comp got {comp} marks")
        print(f"you guess {a} and comp guess {b}")
    #you enterd w
    elif a=="w" and b=="g":
        comp+=1
        print(f"comp got {comp} marks")
        print(f"you guess {a} and comp guess {b}")
    #comp enterd g
    elif a=="g" and b=="w":
        human+=1
        print(f"you got {human} marks")
        print(f"you guess {a} and comp guess {b}")
    #you enterd w
    elif a=="w" and b=="s":
        human+=1
        print(f"you got {human} marks")
        print(f"you guess {a} and comp guess {b}")
    #comp enterd w
    elif a=="s" and b=="w":
        comp+=1
        print(f"comp got {comp} marks")
        print(f"you guess {a} and comp guess {b}")
    #any other input
    else:
        print("wrong input")

    no_of_ch+=1
print("game over")
if human==comp:
    print("tie play again")
elif comp>human:
    print(f"comp win with {comp} marks and you lose with {human} marks")
else:
    print(f"you win with {human} marks and comp lose with {comp} marks")
