import random

class Coin:

    def __init__(self) -> None:
        self.toss="Tale"

    
    def flipCoin(self):
        if(random.randint(0,1)==1):
            self.toss='Head';
        else:
            self.toss='Tale';


    def get_sideUp(self):
        return self.toss;


        

my_coin=Coin()

print(my_coin.toss)




