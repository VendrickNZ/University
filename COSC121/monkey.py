def make_album(id_num, name, band, price):
    """Creates and returns a dictionary with keys id_num, name, brand, and price"""
    album = {"id_num": id_num, 
             "name": name, 
             "band": band, 
             "price": price,
             "total_sales": 0,
             "first_date_recorded": None,
             "last_date_recorded": None}
    return repr(album).replace(',',',\n')

def add_sales(album, date, daily_sales):
    """updates the given dictionary by incrementing the total_sales
    value by the given number of sales for that day"""
    album["total_sales"] = daily_sales
    album["last_date_recorded"] = date
    if album["first_date_recorded"] > 0:
        pass
    else:
        album["first_date_recorded"] = date
    return album
def print_album(album):
    """prints the given album"""
    list(album.values())
    print(album)




album = make_album(123456, 'Madder Mortem', 'Red in Tooth and Claw', 14.44)
print_album(album)
