import sys
import termios
import tty

#define getch
#remove the need to press enter to enter input
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class ForLoops:

    def __init__(self):
        self.ForLoopOne
        self.ForLoopTwo

    def ForLoopOne(self):
        numbers = [1,2,3,4,5]
        for num in numbers:
            print(num)

    def ForLoopTwo(self):
        for i in range (1,6):
            print(i)

    
class WhileLoops:

    def __init__(self):
        self.WhileLoopOne
        self.WhileLoopTwo

    def WhileLoopOne(self):
        i = 1
        while i <= 5:
            print(i)
            #don't forget to update the loops variable  to avoid infinate loops
            i += 1 
    
    def WhileLoopTwo(self):
        total = 0
        limit = 10

        while total < limit:
            number = int(input("Enter a number: "))
            total += number
            print("Current Total: ", total)

        print("Reached the limit")

    def WhileLoopThree(self):
        while True:
            user_input = input("Type a letter (or 'q' to quit)")

            if user_input == 'q':
                print("Exiting the loop")
                break

            else:
                print(f"you typed: {user_input}")

    def WhileLoopFour(self):
        while True:
            print("Type a letter or 'q' to quit: ", end ='', flush=True)
            char = getch()

            if char == 'q':
                print("\nExiting the loop")
                break
            else:
                print(f"You Typed: {char}")
