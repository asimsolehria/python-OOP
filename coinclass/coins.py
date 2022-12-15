import random

class Coin:
    def __init__(self) -> None:
        self.sideup='Head'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='Head'
        else:
            self.sideup='Tail'
    def get_sideup(self):
        return self.sideup
def main():
    my_coin=Coin()
    print("This is the side up: ", my_coin.get_sideup())
    print("I am tossing the coin....")
    my_coin.toss()
    print("This is side up: ", my_coin.get_sideup())
main()