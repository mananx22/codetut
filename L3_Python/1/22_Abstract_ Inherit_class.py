import random
# Abstract CLass
class coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value*1.8
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color
    
    def clean(self):
        self.color = self.clean_color

    def flip(self):
         self.heads = random.choice([True, False]) 

    def __str__(self):
        if self.original_value >= 1:
            return "{} Pound ".format(int(self.original_value)) 
        else:
            return "{} Pennies ".format(int(self.original_value*100)) 

# A class inherited from coin class
class pound(coin):
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_color" : "gold",
            "rusty_color" : "greenish",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 3.15,
            "mass" : 9.5
            }
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

    # this needs to comment because destructor  runs automatically   
    # def __del__(self):
    #     print("coin deleted")

class one_pence(coin):
    def __init__(self):
        data = {
            "original_value" : 0.01,
            "clean_color" : "bronze",
            "rusty_color" : "brownish",
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)
  
class two_pence(coin):

    def __init__(self):
        data = {
            "original_value" : 0.02,
            "clean_color" : "bronze",
            "rusty_color" : "brownish",
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

class five_pence(coin):
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "clean_color" : "silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color 

class ten_pence(coin):
    def __init__(self):
        data = {
            "original_value" : 0.10,
            "clean_color" : "silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color

class twenty_pence(coin):
    def __init__(self):
        data = {
            "original_value" : 0.20,
            "clean_color" : "silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color

class fifty_pence(coin):
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "clean_color" : "silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color

class two_pound(coin):
    def __init__(self):
        data = {
            "original_value" : 2.00,
            "clean_color" : "gold",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 20.5,
            "thickness" : 1.15,
            "mass" : 3.25
            }            
        # now we call parent class constructor to set up everything, and pass our data unpacked to it's constructor.
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color

        def clean(self):
            self.color = self.clean_color



coins = [one_pence(), two_pound(), five_pence(), twenty_pence()]

for coin in coins:
    arguments = [coin, coin.color, coin.value]
    print("{} - color: {}  - value {}".format(*arguments))
# print(coin1.value)


# coin2  = pound() 
# print(coin2.value)

# coin2.rust()
# print(coin2.color)


# coin1.flip()
# coin2.flip()
# print(coin1.heads)
# print(coin2.heads)


