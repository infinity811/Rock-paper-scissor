import random 
import os

flag = True


def start():
    global flag
    os.system("clear")
    if flag:
        intro = int(input("Press 1 to start 🦕: "))
    else:
        intro = int(input("Press 1 to play again 🦖: "))
    if intro == 1:
        play()  
    else:
        print("Bye bye 👋 ")
        return 0
    
#play function
def play():
    global flag
    uc = 0
    cc = 0
    points = int(input("How many points game?"))
    while uc < points and cc < points:
        user = input("----Lets Play----\nRock(r)🪨\nPaper(p)📄\nScissors(s)✂️\n---Select one----\n ").lower()
        computer = random.choice(['r','p','s','p','s','r'])

        if user == computer:
            print("tie")
        elif who_win(user,computer):
            print("You 🧑‍💻 get one point")
            uc = uc + 1
            print ("Your points: " + str(uc))
            print ("Computer points: " + str(cc))
        else:
            print("Computer 🖥 gets a point")
            cc = cc + 1
            print ("Computer points: " + str(cc))
            print ("Your points: " + str(uc))
    
    if uc < cc:
        print(" :( Computer wins! ")
    else:
        print("You won")
    input("press enter to continue")
    flag = False
    start()

# r > p : p > r : r > s ;
    
def who_win(person,comp):
    if (person == 'r' and comp == 'p')or(person == 'p' and comp == 'r')\
        or (person == 'r' and comp == 's'):
        
        return True



start()
