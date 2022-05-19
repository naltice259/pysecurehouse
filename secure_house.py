#!/usr/bin/python3
import sys
def main(argv):
    fkey = "FIREFIGHTER_SECRET_KEY"
    iskey = False
    unlocked = False
    whosinside = []
    line = input()
    words = line.split()
    while(line != ''):
        if words[0] == "INSERT" and words[1] == "KEY":
            inserter = words[2]
            keyinserted = words[3]
            print("KEY", words[3], "INSERTED BY", words[2])
        elif words[0] == "TURN" and words[1] == "KEY":
            for w in sys.argv:
                if w == keyinserted:
                    iskey = True
            if keyinserted == fkey:
                iskey = True
            if inserter == words[2] and iskey == True:
                print("SUCCESS", words[2], "TURNS KEY", keyinserted)
                unlocked = True
            else:
                print("FAILURE", words[2], "UNABLE TO TURN KEY", keyinserted)
                
            iskey = False
        elif words[0] == "ENTER" and words[1] == "HOUSE":
            if inserter == words[2] and unlocked == True:
                print("ACCESS ALLOWED")
                unlocked = False
                whosinside.append(inserter)
            else:
                print("ACCESS DENIED")

        elif words[0] == "WHO'S" and words[1] == "INSIDE?":
            if whosinside == []:
                print("NOBODY HOME")
            else:
                print(', '.join(whosinside))
                
        elif words[0] == "LEAVE" and words[1] == "HOUSE":
            if words[2] in whosinside:
                whosinside.remove(words[2])
                print("OK")
            else:
                print(words[2], "NOT HERE")
        elif words[0] == "CHANGE" and words[1] == "LOCKS":
            if words[2] in whosinside and words[2] == sys.argv[1]:
                sys.argv[2:] = words[3:]
                print("OK")
            else:
                print("ACCESS DENIED")
        else:
            print("ERROR")
        try:
            line = input()
            words = line.split()
        except EOFError:
            return

main(sys.argv[1:])
