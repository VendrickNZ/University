def first_chars(string_list):
    monkey = ""
    for line in string_list:
        monkey += line[0]
    return monkey

print(first_chars(["A", "Big", "Cat"]))
print(first_chars(["Fee", "fi", "fo", "fum"]))
