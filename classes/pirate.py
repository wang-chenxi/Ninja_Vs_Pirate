class Pirate:

    def __init__(self, name):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 20:
            print(f"{self.name} is running out of energy. Be cautious!")

    def attack(self, ninja):
        if ninja.speed > 0:
            print(f"{ninja.name} avoided the attack! remaining speed:{ninja.speed}")
            ninja.speed -= 1
            return self
        else:
            if ninja.health > self.strength:
                ninja.health -= self.strength
                print(
                    f"wow! good attack! {ninja.name}'s health reduce: {self.strength}, remaining health:{ninja.health}")
            else:
                print(
                    f"{ninja.name}'s current health: {ninja.health}. {ninja.name} cannot afford the attack of: {self.strength}")
                Pirate.gameover(self, ninja)
        return self

    def gameover(self, ninja):
        print(f"{self.name} win!")
        print(f"{ninja.name} die!")
        print("[̲̅g][̲̅a][̲̅m][̲̅e] [̲̅o][̲̅v][̲̅e][̲̅r]")
        exit()
