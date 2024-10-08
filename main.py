#                    TIMER & OPTIMUM MOVE

#                 TOWER OF HANOI GAME SETUP
#                       GAME OBJECTS

import time


class GameObject:
    def __init__(self, representation):
        self.representation = representation
        self.colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
        self.color = None

    def colorme(self, size=None):
        if size == 1:
            self.color = "\033[37m"
        elif size == 2:
            self.color = "\033[93m"
        elif size == 3:
            self.color = "\033[96m"
        else:
            self.color = "\033[91m"

        return self.color


#   Peg.representation - |
#   Disk.representation - 00, 0000, 000000, 00000000, 0000000000, 000000000000


#                 TOWER OF HANOI GAME SETUP
#             Peg Object is inherited from Game Object

#              |               |               |
#              |               |               |
#              |               |               |
#              |               |               |
#              |               |               |
#              |               |               |

# Peg OBJECT PROPERTIES
#   Peg.name   1               2               3   ( 3 Peg OBJECTS )
#   Peg.disks - empty list now, 3 to 6 in 1st Peg while starting, moves between 2nd and 3rd Pegs
# Peg OBJECT METHODS
#   Peg.add_disk(self, disk) - method to add disk to the Peg object in call

class Peg(GameObject):
    def __init__(self, name):
        super().__init__("|")
        self.name = name
        self.disks = []

    def add_disk(self, disk):
        self.disks.append(disk)


#               TOWER OF HANOI GAME SETUP
#         Disk Object is inherited from Game Object
# Disk OBJECT PROPERTIES
#   Disk.size -           1                     to                   6

class Disk(GameObject):
    def __init__(self, size):
        super().__init__("00" * size)
        self.size = size

    def colorme(self, size=None):
        if size is None:
            self.color = "\033[37m"
        else:
            self.color = self.colors[size - 1]
        return self.color

#               TOWER OF HANOI GAME SETUP
#                   TowerOfHanoi OBJECT

# PROPERTIES
#   TowerOfHanoi.pegs -  list of 3 Peg Objects
#   TowerOfHanoi.disk_count - initial value zero
# METHODS
#   TowerOfHanoi.create_disks() - creates and adds to 1st Peg
#   TowerOfHanoi.print_pegs(self, final=False) - prints the initial setup
#   TowerOfHanoi.play_game(self) - leader function


class TowerOfHanoi:
    def __init__(self):
        self.game_rules()
        self.pegs = [Peg(1), Peg(2), Peg(3)]
        self.disk_count = 0
        self.create_disks()
        self.move_count = 0
        self.optimum_moves = 2 ** len(self.pegs[0].disks) - 1

    @staticmethod
    def game_rules():
        # Print the rules
        print("\nWelcome to \"Tower of Hanoi\" Game.\n\nThere are three pegs and 1st peg will have all "
              "the disks while starting the game. You can choose to play with 3 to 6 disks as you wish.\n\nGame rules:")
        print("1. Move one disk at a time.")
        print("2. Bigger disk cannot be on top of smaller disk.")
        print("3. Move all the disks to 2nd or 3rd peg following above rules.")
        print("4. This is not a rule. System will monitor number of moves and time taken. "
              "Try and check your thinking speed and accuracy.\n")
        while True:
            user_input = input("Type yes / y  if you are ready and the timer will be ON\n").lower()
            if user_input in ["yes", "y"]:
                break
            else:
                print("okay, restart the game when you are ready")

    def create_disks(self):
        self.disk_count = int(input("Enter number of disks (3-6): "))
        while self.disk_count < 3 or self.disk_count > 6:
            self.disk_count = int(input("Invalid input. Enter number of disks (3-6): "))
        for i in range(self.disk_count, 0, -1):
            self.pegs[0].add_disk(Disk(i))

    #            TOWER OF HANOI GAME INITIAL POSITION

    #             00               |               |
    #            0000              |               |
    #           000000             |               |
    #          00000000            |               |
    #         0000000000           |               |
    #        000000000000          |               |

    #            TOWER OF HANOI GAME ARBITRARY POSITION

    #           000000             |               |
    #          00000000            |               |
    #         0000000000           |               |
    #        000000000000         00             0000

    #     TOWER OF HANOI GAME ANOTHER ARBITRARY POSITION

    #          00000000            |               |
    #         0000000000           |              00
    #        000000000000       000000           0000

    # local variable max_disks to know the height dimension

    def print_pegs(self, final=False):
        max_disks = max(len(peg.disks) for peg in self.pegs)
        for i in range(max_disks, 0, -1):  # height dimension
            for peg in self.pegs:  # width dimension
                if i <= len(peg.disks):
                    print(" " * 25 + peg.disks[i - 1].colorme(peg.disks[i - 1].size)
                          + peg.disks[i - 1].representation.center(15) + "\033[0m", end="")
                else:
                    print(" " * 25 + peg.colorme(peg.name) + peg.representation.center(15) + "\033[0m", end="")
            print()
        print(" " * 25 + "Peg-01".center(15), end="")
        print(" " * 25 + "Peg-02".center(15), end="")
        print(" " * 25 + "Peg-03".center(15))
        print("-" * 120)
        if final:
            print(f"Game over! Number of moves: {self.move_count} / Optimum: {self.optimum_moves}")
        else:
            print(f"Completed Number of moves: {self.move_count}")

    @staticmethod
    def getpegnumber(msg):
        while True:
            try:
                peg = int(input(msg))
                if peg < 1 or peg > 3:
                    print("Invalid input." + msg)
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
        return peg

    def make_move(self):
        from_peg = self.getpegnumber("Enter from-peg (1-3): ") - 1
        to_peg = self.getpegnumber("Enter to-peg (1-3): ") - 1

        disk = self.pegs[from_peg].disks[-1] if self.pegs[from_peg].disks else None
        if disk and (not self.pegs[to_peg].disks or disk.size < self.pegs[to_peg].disks[-1].size):
            self.pegs[from_peg].disks.pop()
            self.pegs[to_peg].disks.append(disk)
        else:
            print("Invalid move!, Enter a valid peg number [1-3]:")
        self.move_count += 1

    def play_game(self):
        start_time = time.time()
        while True:
            self.print_pegs()
            self.make_move()
            if len(self.pegs[0].disks) == 0 and (
                    len(self.pegs[1].disks) == self.disk_count or len(self.pegs[2].disks) == self.disk_count):
                self.print_pegs(final=True)
                print("Congratulations! You completed successfully!")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Time taken: {elapsed_time:.2f} seconds")
                break


if __name__ == "__main__":
    game = TowerOfHanoi()  # game is a TowerofHanai object. It creates Peg Object, Disk Object
    game.play_game()
