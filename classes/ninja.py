class Ninja:

    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 20:
            print(f"{self.name} is tired. Be cautious!")

    def attack(self, pirate):
        if pirate.speed > 0:
            print(f"{pirate.name} avoided the attack! remaining speed:{pirate.speed}")
            pirate.speed -= 1
            return self
        else:
            if pirate.health > self.strength:
                pirate.health -= self.strength
                print(
                    f"wow! good attack! {pirate.name}'s health reduce: {self.strength}, remaining health:{pirate.health}")
            else:
                print(
                    f"{pirate.name}'s current health: {pirate.health}. {pirate.name} cannot afford the attack of: {self.strength}")
                Ninja.gameover(self, pirate)
        return self

    def gameover(self, pirate):
        print(f"{self.name} win!")
        print(f"{pirate.name} die!")
        print("[̲̅g][̲̅a][̲̅m][̲̅e] [̲̅o][̲̅v][̲̅e][̲̅r]")
        exit()
