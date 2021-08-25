import sys
import random

class SnakeAndLadder:
    def __init__(self):
        self.ladders = {4:14,9:31,20:38,28:84,40:59,63:81,71:91}
        self.snakes = {17:7,54:34,62:18,64:60,87:24,93:73,95:75,99:78}
        self.print_welcome_messages()
        self.player_nickname = []
        self.populate_participant_info()
        self.start_game()
        self.start()
    
    def display_ladder_pos(self):
        print("Ladder positions")
        for key,val in self.ladders.items():
            print(str(key)+"->"+str(val),end=",")
        print()
    
    def display_snake_pos(self):
        print("Snake positions")
        for key,val in self.snakes.items():
            print(str(key) + "->"+str(val),end=",")
        print()

    
    def print_welcome_messages(self):
        print("*************WELCOME TO SNAKE AND LADDER GAME***************")
        print("*************HOPE YOU ENJOY THE GAME************************")
        print("MAXIMUM 4 PLAYES CAN PARTICIPATE IN THE GAME")

    def populate_participant_info(self):
        player_count = int(input("Please the number of payers participating\n"))
        if (player_count>4 or player_count<1):
            print("Didn't meet the ideal participant count exiting the game")
            sys.exit(0)
        else:
            print("Enter players nickname \n")
            i = 1
            while(i<=player_count):
                nickname = input("Enter Player"+str(i)+" nickname : ")
                nickname = nickname.strip()
                if (len(nickname)<1):
                    print("Invalid nickname entered, enter the nickname again")
                else:
                    self.player_nickname.append(nickname)
                    nickname = ""
                    i+=1
    def start_game(self):
        self.player_nickname.sort()
        print("Game will start with nickname in alphabatical order")
        for i in range(1,len(self.player_nickname)+1):
            print("Player number"+str(i)+" : " + str(self.player_nickname[i-1]))
        print("########################ALL SET LET'S START THE GAME###########################")
    
    def start(self):
        initial_positions = [1]*len(self.player_nickname)
        while 1:
            for i in range(len(self.player_nickname)):
                print(self.player_nickname[i] + " is rolling the dice with current position at "+ str(initial_positions[i])+", please press enter to roll the dice")
                self.display_ladder_pos()
                self.display_snake_pos()
                input("Waiting for " + self.player_nickname[i] +" to press enter")
                val = random.randint(1,6)
                print(self.player_nickname[i] + " got dice value of " + str(val))
                print(self.player_nickname[i] + " has moved from "+str(initial_positions[i]) + " to " + str(initial_positions[i] + val))
                if (initial_positions[i] + val >100):
                    print("Dice value should be lower than " + str(100-initial_positions[i]) + " to move the position")
                    continue
                initial_positions[i] += val
                if (initial_positions[i] in self.ladders):
                    print("**********************Congratulation a ladder is found at position " + str(initial_positions[i]))
                    print(self.player_nickname[i] + " has moved from "+ str(initial_positions[i])+ " to " + str(self.ladders[initial_positions[i]]) + " with the help of ladder")
                    initial_positions[i] = self.ladders[initial_positions[i]]
                if (initial_positions[i] in self.snakes):
                    print("----------------------Unfortunately a snake head is found at position " + str(initial_positions[i]))
                    print(self.player_nickname[i] + " has moved down from "+ str(initial_positions[i])+ " to " + str(self.snakes[initial_positions[i]]) + " due to snake")
                    initial_positions[i] = self.snakes[initial_positions[i]]
                if (initial_positions[i] == 100):
                    print("****************************Congrtulations******************************")
                    print(self.player_nickname[i] + " has won the game")
                    print("final positions of the players : ")
                    for j in range(len(self.player_nickname)):
                        print(self.player_nickname[j] + " : "+ str(initial_positions[j]))
                    print("Ending the game")
                    return
            

if __name__ == "__main__":
    game = SnakeAndLadder()