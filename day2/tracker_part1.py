import numpy as np
import os

class Submarine:
    directions = {
        "down": np.array([0,1],dtype=int),
        "up": np.array([0,-1],dtype=int),
        "forward": np.array([1,0],dtype=int)
    }
    def __init__(self) -> None:
        self.position = np.zeros(2,dtype=int)
    
    def move(self, input):
        direction, magnitude = input.split()
        self.position += self.directions[direction]*int(magnitude)

    def get_depth(self):
        return self.position[1]
    
    def get_horizontal(self):
        return self.position[0]

    def announce_position(self):
        announce = f"We are currently at a depth of {self.get_depth()} and a horizontal position of {self.get_horizontal()}"
        print(announce)


def main():
    sub = Submarine()
    current_directory = os.getcwd()
    new_directory = current_directory + "\\Day 2"
    os.chdir(new_directory)

    with open('day2input.txt', 'r') as input_file:
        move = input_file.readline()
        while move:
            sub.move(move)
            move = input_file.readline()
    sub.announce_position()

    os.chdir(current_directory)
    

if __name__ == "__main__":
    main()
