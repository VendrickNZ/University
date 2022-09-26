class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
def backtrack(table):
    i = len(table) - 1
    j = len(table[0]) - 1
    result = []   
    while i > 0 and j > 0:
        if table[i][j] != table[i-1][j]:
            j -= items[i - 1].weight
            result.append(items[i - 1])
        i -= 1
    return result

def max_value(items, capacity):
    """The maximum value achievable with a given list of items and a given
       knapsack capacity."""
       
       # *** IMPLEMENT ME ***
    rows = capacity + 1
    columns = len(items)+1
    table = [[0 for j in range(rows)]for i in range(columns)]
    for i in range(1, columns):
        for j in range(rows):
            if items[i-1].weight <= j:
                table[i][j] = max(items[i-1].value + table[i - 1][j - items[i-1].weight], table[i - 1][j])
            elif items[i-1].weight > j:
                table[i][j] = table[i-1][j]
    return (table[-1][-1], backtrack(table))


	
# The example in the lecture notes
items = [Item(45, 3),
        Item(45, 3),
        Item(80, 4),
        Item(80, 5),
        Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(maximum)