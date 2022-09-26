"""A program that defines an Album class and then returns a catalogue summary"""
import os.path
class Album:
    """Defines an Album class.
    Methods: add_sales(date, daily_sales)
    """
  
        
    
    def __init__(self, id_num, name, band, price):
        """Creates an init method with album arguments"""
        self.id_num = id_num
        self.name = name
        self.band = band
        self.price = price
        self.total_sales = 0
        self.first_date_recorded = None
        self.last_date_recorded = None
        self.cert = ""
        

    def add_sales(self, date, daily_sales):
        """updates the given values by incrementing the total_sales
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
    
    def update_cert(self):
        if self.total_sales >= 500000:
            self.cert = "Diamond"
        elif self.total_sales >= 100000:
            self.cert = "Platinum"
        elif self.total_sales >= 50000:
            self.cert = "Gold"
        else:
            self.cert = ""

    def __str__(self):
        """prints the given album"""
        self.update_cert()
        return "{:<5}{:<30}{:>10}{:>15}".format(self.id_num, self.name, self.total_sales, self.cert)
       
def sort_albums(albums):
    """sorts the albums by id_num"""
    albums.sort(key=lambda x: x.total_sales, reverse=True)
    return albums
    
def extract_album(lines, index):
    """takes a list of lines and an index and returns an album value"""
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
                if(album.id_num) == int(list_of_list_items[i][1]):
                    album.add_sales(list_of_list_items[i][0], list_of_list_items[i][2])             





FILENAME = input("Enter a data file name: ")
while os.path.isfile(FILENAME) == False:
    print("Invalid File Name Entered!") 
    FILENAME = input("Enter a data file name: ")
LINES = open(FILENAME).read().splitlines()
ALBUMS = extract_all_albums(LINES)
read_sales(LINES, ALBUMS)
sort_albums(ALBUMS)
print()
print("Album Catalogue Summary\n" +
            "-" *60 + 
("\n{:<5}{:<30}{:>10}{:>15}".format("ID", "ALBUM NAME", "# SOLD", "CERTIFICATE")))

for entry in ALBUMS:
    print(entry)
 