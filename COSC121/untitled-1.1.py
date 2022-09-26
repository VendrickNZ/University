"""Program that pulls in donation information and processes it to produce a
report for the user.

Author: Jakib Isherwood
Last Edited: 1/9/20
Contact the developer: jis48@uclive.ac.nz

This document was produced as a part of COSC121 2020S2 Super Quiz 2
"""

def percent_of_target(donation, goal):
    """returns a float representing the percentage of the overall
    goal that is contributed by the given donation"""
    #chimp = 0
    #for i in range(len(donation)):
    #    print(donation[i])
    #    chimp = float(donation[i]/goal)*100
    return float(donation/goal)*100

def donor_category(percent_donated, amount_donated):
    """the percent_donated is the percentage of the campaigns goal
    met by the donor and amount_donated is the actual dollar amount
    donated by that individual"""
    donations = ""

    if percent_donated > 0 and percent_donated < 2:
        if amount_donated > 0 and amount_donated < 500:
            donations = "Bronze"
            
        elif amount_donated >= 500 and amount_donated <= 1000:
            donations = "Silver"
        elif amount_donated > 1000:
            donations = "Gold"
    elif percent_donated >= 2 and percent_donated <= 15:
        if amount_donated > 1000:
            donations = "Gold" 
        else: 
            donations = "Silver"
    elif percent_donated > 15:
        if amount_donated > 1000:
            donations = "Platinum"
        else:
            donations = "Gold"
    else:
        donations = "Error"
    if amount_donated <= 0:
        donations = "Error"    
    return donations

def categorise_donations(donations, campaign_goal):
    """list of numbers that represent all the donations gained
    so far in the campaign"""
    categories = []
    for donation in donations:
        percent_donated = percent_of_target(donation, campaign_goal)
        categories.append((donation, donor_category(percent_donated, donation)))
    return categories
    


def filter_donations(donor_classification, donations):
    """donor_classification is a string that states category of donor
    we want to filter for, returns the list of all donations that matched
    donor_classification"""
    return [donation[0] for donation in donations if donation[1] == donor_classification]


def print_header():
    """prints the header"""
    category = "Category"
    subtotal = "Subtotal"
    print("{:22}{}".format(category, subtotal))
    print("------------------------------")


def print_category_subtotals(donations):
    """prints the subtotals and the total"""
    bronze = "Bronze"
    silver = "Silver"
    gold = "Gold"
    platinum = "Platinum"
    bronze_value = 0
    silver_value = 0
    gold_value = 0
    platinum_value = 0
    
    for i in range(len(donations)):

        if "Bronze" in donations[i]:
            bronze_value += donations[i][0]
        elif "Silver" in donations[i]:
            silver_value += donations[i][0]
        elif "Gold" in donations[i]:
            gold_value += donations[i][0]
        elif "Platinum" in donations[i]:
            platinum_value += donations[i][0]

    print("{:<15}{:>15.2f}".format(bronze, bronze_value))
    print("{:<15}{:>15.2f}".format(silver, silver_value))
    print("{:<15}{:>15.2f}".format(gold, gold_value))
    print("{:<15}{:>15.2f}".format(platinum, platinum_value))

    total = "TOTAL"
    total_number = (bronze_value + silver_value + gold_value + platinum_value)
    print("==============================")
    print("{:<15}{:>15.2f}".format(total, total_number))    


def print_donor_report(donations):
    """prints the entire donor report"""
    print_header()
    print_category_subtotals(donations)

def print_statistics(errors, highest, mean):
    """prints statistics of the amounts donated"""
    statistics = "STATISTICS"
    print("\n{:^30}".format(statistics))
    print("Errors" + "{:>24}".format(errors))
    print("Highest" + "{:>23.2f}".format(highest))
    print("Mean" + "{:>26.2f}".format(mean))
    


def main():
    """Gets information from the user and then prints a report using functions
    that you have written through this quiz"""
    campaign_goal = float(input("Campaign goal: "))
    print("Enter the donations received.")
    donations = 0
    a_list = []
    amount = []
    errors = 0 
    highest = 0
    mean = 0
    
    while str(donations) != "q":
        donations = input("Amount donated? ")
        
        if donations.lower() == "q": # Quit and print          
            print_donor_report(a_list)

            mean = (mean / len(a_list))
            highest = float(highest)
            mean = float(mean)
            print_statistics(errors, highest, mean)
            break
        elif float(donations) <= 0:
            errors += 1
            
        else: # Calculate your shit and append the tuple to a_list

            amount_donated = float(donations)
            percent_donated = (amount_donated/campaign_goal)*100
            category = donor_category(percent_donated, amount_donated)
            amount = amount_donated
    
            a_list.append((amount, category))
        
            if float(donations) > float(highest):
                highest = donations
            mean += float(donations)

# starts the program
main()  