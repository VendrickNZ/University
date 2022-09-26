
import math


class Toy():
    """ """
    def __init__(self, name, colour, cost):
        self.name = name
        self.colour = colour
        self.cost = cost


class ToyBox:
    """ """ 

    def __init__(self):
        self.all_toys = []
        

    def add_toy(self, name, colour, cost):
        a_toy = Toy(name, colour, cost)
        self.all_toys.append(a_toy)
    
    def get_total_toys(self):
        count = int(0)
        for items in self.all_toys:
            count += 1
        return count
    
    def get_total_cost(self):
        sum = 0
        for toy in self.all_toys:
            sum += toy.cost
        return sum

    def get_cheapest_toy(self):
        min = math.inf
        if self.get_total_toys() == 0:
            answer = 'The toy box is empty.'
        else:
            for toy in self.all_toys:
                if toy.cost < min:
                    min = toy.cost
        return min

    def __str__(self):
        msg = f'The toy box contains {self.get_total_toys()} toys\n'
        if self.get_total_toys() == 0:
            msg = 'The toy box is empty.'
        else:
            for a_toy in self.all_toys:
                msg += f'A {a_toy.colour.lower()} {a_toy.name} which cost ${a_toy.cost:.2f}\n'
            msg += f'Total cost: ${self.get_total_cost():.2f}'
        return msg



red_toybox = ToyBox()
print(red_toybox)
cheapest_toy = red_toybox.get_cheapest_toy()
print(f'{cheapest_toy}')
print('Adding toys ...')
red_toybox .add_toy('Big Ted', 'Grey', 14.99)
red_toybox .add_toy('Buzz Lightyear', 'Yellow', 12.99)
red_toybox .add_toy('Rocking horse', 'Wooden', 19.99)
print(red_toybox)
print('Adding a cheap toy ...')
red_toybox .add_toy('Lego car', 'Green', 9.99)
print(red_toybox)
cheapest_toy = red_toybox.get_cheapest_toy()
print(f'{cheapest_toy=}')