import time


class Disk:
    def __init__(self, size):
        self.size = size
        self.representation = "00" * size
        self.colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
        self.color = self.colors[size - 1]

    def __repr__(self):
        return f"{self.representation}{self.color}D{self.size}\033[0m"


class Peg:
    def __init__(self, name):
        self.name = name
        self.disks = []

    def add_disk(self, disk):
        if not self.disks or disk.size < self.disks[-1].size:
            self.disks.append(disk)
        else:
            print("Cannot place larger disk on smaller disk.")

    def remove_disk(self):
        if self.disks:
            return self.disks.pop()
        else:
            print("Peg is empty.")
            return None

    def __repr__(self):
        return f"{self.name}: {self.disks}"


class TowerOfHanoi:
    def __init__(self):
        self.pegs = [Peg(1), Peg(2), Peg(3)]
        self.disk_count = 0
        self.move_count = 0
        self.game_rules()
        self.create_disks()
        self.optimum_moves = 2 ** len(self.pegs[0].disks) - 1

    def create_disks(self):
        self.disk_count = int(input("Enter number of disks (3-6): "))
        while self.disk_count < 3 or self.disk_count > 6:
            self.disk_count = int(input("Invalid input. Enter number of disks (3-6): "))
        for i in range(self.disk_count, 0, -1):
            self.pegs[0].add_disk(Disk(i))

    def print_pegs(self, final=False):
        max_disks = max(len(peg.disks) for peg in self.pegs)
        for i in range(max_disks, 0, -1):
            for peg in self.pegs:
                if i <= len(peg.disks):
                    print(" " * 25 + peg.disks[i - 1].color + peg.disks[i - 1].representation.center(15)
                          + "\033[0m", end="")
                else:
                    print(" " * 40, end="")
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
    def game_rules():
        # Print the rules
        print("\nWelcome to \"Tower of Hanoi\" Game.\n\nThere are three pegs and 1st peg will have all "
              "the disks while starting the game. You can choose to play with 3 to 6 disks as you wish.\n\nGame rules:")
        print("1. Move one disk at a time.")
        print("2. Bigger disk cannot be on top of smaller disk.")
        print("3. Move all the disks to 2nd or 3rd peg following above rules.")
        print("4. This is not a rule. System will monitor number of moves and time taken. "
              "xhibit and check your thinking speed and accuracy.\n")
        while True:
            user_input = input("Type yes / y  if you are ready and the timer will be ON\n").lower()
            if user_input in ["yes", "y"]:
                break
            else:
                print("okay, restart the game when you are ready")

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
                print("Congratulations! You won!")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Time taken: {elapsed_time:.2f} seconds")
                break


if __name__ == "__main__":
    game = TowerOfHanoi()
    game.play_game()
