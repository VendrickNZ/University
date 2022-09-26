class Album:
    
    """Creates and returns a dictionary with keys id_num, name, brand, and price"""
    def __init__(self, id_num, name, band, price):
        self.id_num = id_num
        self.name = name
        self.band = band
        self.price = price
        self.total_sales = 0
        self.first_date_recorded = None
        self.last_date_recorded = None
        

    def add_sales(self, date, daily_sales):
        """updates the given dictionary by incrementing the total_sales
        value by the given number of sales for that day"""
        self.total_sales += int(daily_sales)
        
        if self.last_date_recorded == None:
            self.last_date_recorded = date
        
        if date > self.last_date_recorded:
            self.last_date_recorded = date
        if self.first_date_recorded == None:
            self.first_date_recorded = date
        elif self.first_date_recorded != None:
            if self.first_date_recorded > date:
                self.first_date_recorded = date
        else:
            self.first_date_recorded = date
        __str__(self)
        
def __str__(self):
    """prints the given album"""
    print("----------------------------------------")
    print("Album Name: {}".format(self.name))
    print("Band: {}".format(self.band))
    print("Purchase Price: ${:.2f}".format(float(self.price)))
    print("First Recorded Sale: {}".format(self.first_date_recorded))
    print("Last Recorded Sale: {}".format(self.last_date_recorded))
    print("Total Sold: {}".format(self.total_sales))    
    print("----------------------------------------")

def extract_album(lines, index):
    """takes a list of lines and an index and returns an album dictionary"""
    album = {}
    lists = []
    for line in lines[index:]:
        lists.append(line)
    id_num = int(lists[0])
    name = lists[1]
    band = lists[2]
    price = float(lists[3])
    album = Album(id_num, name, band, price)
    return album

    
    

def extract_all_albums(lines):
    """reads all the albums in the list of lines and returns a list of albums
    in the same order they are encountered in"""
    list_items = []
    result = []
    list_albums = []
    albums = []
    seperators = ("<album>", "</album>")
    if lines[0] in seperators:
        skip = 0
    else:
        skip = 1
    for line in lines:
        if line in seperators:
            if list_items:
                result.append(list_items)
            list_items = []
        else:
            list_items.append(line)
    result.append(list_items)
    list_albums = result[skip::2]
    for item in list_albums:
        albums.append(extract_album(item, 0))
    return albums
        
               
def read_sales(lines, albums):
    """locates the sales section if there is one and updates the 
    appropriate albums details"""
    list_of_list_items = []
    list_items = []
    if "<sales>" and "</sales>" in lines:
        
        sales_index = lines.index("<sales>")
        end_sales_index = lines.index("</sales>")
        for line in lines[sales_index +1:end_sales_index]:
            list_items = line.split(",")
            list_of_list_items.append(list_items)
        for i in range(len(list_of_list_items)):
            for album in albums:
                if(int(album["id_num"]) == int(list_of_list_items[i][1])):
                    album.add_sales(list_of_list_items[i][0], list_of_list_items[i][2])             
        

file = open("album0.txt")
lines = file.read().splitlines()
albums = extract_all_albums(lines)
read_sales(lines, albums)

for album in albums:
    print(album)
    print()          