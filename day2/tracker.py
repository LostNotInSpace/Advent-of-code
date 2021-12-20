import numpy as np

class Submarine:
    def __init__(self) -> None:
        self.position = np.zeros(2,dtype=int)
        self.aim = 0
    
    def move(self, input):
        direction, magnitude = input.split()
        magnitude = int(magnitude)

        if direction == "down":
            self.aim += magnitude
        elif direction == "up":
            self.aim -= magnitude
        elif direction == "forward":
            self.position = self.position + magnitude*np.array([1,self.aim],dtype=int)
        else:
            raise ValueError

    def get_depth(self):
        return self.position[1]
    
    def get_horizontal(self):
        return self.position[0]

    def announce_position(self):
        announce = f"We are currently at a depth of {self.get_depth()} and a horizontal position of {self.get_horizontal()}"
        print(announce)


def main():
    sub = Submarine()

    with open('day2input.txt', 'r') as input_file:
        move = input_file.readline()
        while move:
            sub.move(move)
            move = input_file.readline()
    sub.announce_position()
    

if __name__ == "__main__":
    main()
