def make_album(id_num, name, band, price):
    """Creates and returns a dictionary with keys id_num, name, brand, and price"""
    album = {"id_num": id_num, 
             "name": name, 
             "band": band, 
             "price": price,
             "total_sales": 0,
             "first_date_recorded": None,
             "last_date_recorded": None}
    return album

def add_sales(album, date, daily_sales):
    """updates the given dictionary by incrementing the total_sales
    value by the given number of sales for that day"""
    album["total_sales"] += int(daily_sales)
    
    if album["last_date_recorded"] == None:
        album["last_date_recorded"] = date
    
    if date > album["last_date_recorded"]:
        album["last_date_recorded"] = date
    if album['first_date_recorded'] == None:
        album['first_date_recorded'] = date
    elif album['first_date_recorded'] != None:
        if album['first_date_recorded'] > date:
            album['first_date_recorded'] = date
    else:
        album["first_date_recorded"] = date
        
def print_album(album):
    """prints the given album"""
    print("----------------------------------------")
    print("Album Name: {}".format(album.get("name")))
    print("Band: {}".format(album.get("band")))
    print("Purchase Price: ${:.2f}".format(float(album.get("price"))))
    print("First Recorded Sale: {}".format(album.get("first_date_recorded")))
    print("Last Recorded Sale: {}".format(album.get("last_date_recorded")))
    print("Total Sold: {}".format(album.get("total_sales")))    
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
    album = make_album(id_num, name, band, price)
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
                    add_sales(album, list_of_list_items[i][0], list_of_list_items[i][2])             
        
# Example with no sales section
example = [
    "Angus's album listing",
    "<album>",
    "100",
    "Now 1000",
    "Na",
    "27.50",
    "</album>",
    "# Unbearable albums follow",
    "<album>",
    "101",
    "Best Birthday Songs",
    "Serious Music's",
    "10.00",
    "</album>",
    "Phew, we're done!"
]
albums = extract_all_albums(example)
read_sales(example, albums)

for album in albums:
    print_album(album)
    print()