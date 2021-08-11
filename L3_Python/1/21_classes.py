import random

# make a class and isntantiate it's object
class Pound:
    # this is constructor
    def __init__(self, rare=False): 
        self.rare = rare
        if self.rare:
            self.value=3.99
        else:
            self.value=1.99        
        self.color = "gold"
        self.num_edges = 1
        self.diameters = 22.5
        self. thickness = 3.15
        self.heads = True
               

    def rust(self):
        self.color = "green"
    
    def clean(self):
        self.color = "gold"


    def flip(self):
         self.heads = random.choice([True, False])
    
    # destructor in python
    def __del__(self):
        print("coin deleted")

        

coin1 = Pound()
print(coin1.value)


coin2=Pound(rare=True)
print(coin2.value)

coin2.rust()
print(coin2.color)


coin1.flip()
coin2.flip()
print(coin1.heads)
print(coin2.heads)

del coin2
print(coin2.value)
