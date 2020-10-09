import time
#Kirby Assaf, Maude Elovitz, Julia Hartnett
def main():
    print("Every choice you make has positive or negative effects on the Earth.\nBy following along, you can determine how your actions are affecting the planet.")
    time.sleep(3)
    userName = input("Before we get started, enter your name. ")
    print("Welcome, " + str(userName) + ". Let's get you into some scenarios!")
    pointTotal = 0
    pointTotal = coffeeChoice() + pointTotal
    pointTotal = recycling() + pointTotal
    pointTotal = leavingWork() + pointTotal
    pointTotal = storingFood() + pointTotal
    pointTotal = brushTeeth() + pointTotal

    if pointTotal < 5:
        time.sleep(3)
        print("\nYou have a long way to go to being environmentally friendly.\nCheck out some of the sources below to get started on your journey.")

    elif pointTotal < 8:
        time.sleep(3)
        print("\nYou're doing okay, but there are a few more changes you could make to help sustain the Earth.\nCheck out the sources to see some changes you could make.")

    else:
        time.sleep(3)
        print("\nYou are doing a great job being environmentally conscious, keep up the good work!")

    sources()

    print("\nThanks for trying to make the planet a better place!")

def coffeeChoice():
    print("\nYou start your day with a cup of coffee.")
    time.sleep(3)
    choice = input("How do you get your coffee?\nA. Using a compostable coffee filter\nB. Using a reusable K-Cup with a Keurig\nC. Going to Starbucks with a reusable coffee cup ")
    if choice == "A" or choice == "a":
        points = 2
        print("\nGreat! Now you have the beginnings of a compost bin. This is the best and most \nenvironmentally-conscious way to make your coffee.")
        print("\nDo you know where your compost goes if it's full? If not, use litterless.com to check your state!")
    if choice == "B" or choice == "b":
        points = 1
        print("\nThis is an okay option, but at some point you will have to get a new reusable K-Cup so you will eventually have waste.\nThis is way better than using disposable K-Cups, though!")
        moreInfo = input("\nWould you like information on a better way to get your coffee? Enter 'y' for yes, 'n' for no. ")
        if moreInfo == "y" or moreInfo == "Y":
            compost()
            points += 1
    if choice == "C" or choice == "c":
        points = 0
        print("\nGreat job for using a reusable cup!")
        time.sleep(2)
        print("\nHowever, large corporations like Starbucks are the main source of bad environmental habits.\nStarbucks emitted 295,000 tons of carbon into the atmosphere in 2003, according to Forbes.")
        time.sleep(2)
        print("\nIt's tough to avoid large corporations, as they are such a big part of our life. It is best to avoid them when you can!")
        moreInfo = input("\nWould you like information on a better way to get your coffee? Enter 'y' for yes, 'n' for no. ")
        if moreInfo == "y" or moreInfo == "Y":
            compost()
            points += 1
    return(points)

def compost():
    print("\nThe best method would be using a compostable a compostable coffee filter. This way, you have the beginning of a compost filter!\nWhen your compost bin is full, use litterless.com to find your state and check what to do.")

    return()

def recycling():
    print("\nOn your way to work (socially distanced with a mask of course), you realize it is the day that the truck comes to pick-up the recycling you have collected throughout the week!")
    time.sleep(2)
    print("\nYou have a bin filled with items, but you are trying to figure out which items can be recycled.")
    time.sleep(2)
    choice = input("Pick the group of items that includes only items that can be put in your recycling bin:\nA. Cardboard, bubble wrap, ceramic\nB. Milk carton, aluminum can, green glass bottle\nC. Disposable diaper, syringe, plastic bag ")
    if choice == "A" or choice == "a":
        points = 1
        print("\nWhile you can recycle cardboard, you cannot put bubble wrap or ceramic in your recycling bin.")
    if choice == "B" or choice == "b":
        points = 2
        print("\nGreat job! All of these things can be recycled. Make sure to rinse them out!")
    if choice == "C" or choice == "c":
        points = 0
        print("\nUnfortunately, none of these items should be put in your recycling bin.")
    return(points)


def leavingWork():
    print("\nThere are many ways to get to work. In this scenario, we are assuming\nthat you have many transportation options to get to work.")
    time.sleep(2)
    choice = input("\nHow would you like to go to work today? \nA. Bike or walk to work \nB. Take Public Transportation \nC. Use a rideshare app \nD. Drive your own car ")
    if choice == "A" or choice == "a":
        points = 2
        print("\nAwesome! Biking and walking are good exercise, release no carbon emissions, and it is the cheapest option!")
        time.sleep(2)
        print("\nIt is also the most environmentally conscious option.")
    if choice == "B" or choice == "b":
        points = 1
        print("\nAccording to the World Wildlife Organization, 'one fully occupied bus can replace 57 single-occupant cars' which will greatly\nreduce your carbon footprint and save you money!")
    if choice == "C" or choice == "c":
        points = 1
        print("\nAccording to the World Wildlife Organization, 'Carpooling just once a week can shrink your carbon footprint by 20%.'")
    if choice == "D" or choice == "d":
        points = 0
        print("\nThis is not the most environmentally conscious way to get to work, unfortunately.\n26% of greenhouse gas emissions came from transportation in the U.S. in 2014.\nThat’s about 1,786 million metric tons (According to the World Wildlife Organization).")
    return(points)


def storingFood():
    print("\nAfter a long day at work, cooking a nice meal is a great way to wind down.")
    time.sleep(2)
    print("\nBut, you have some leftovers!")
    choice = input("How would you like to store your food?\nA. A plastic bag\nB. A plastic container\nC. A glass container ")
    if choice == "A" or choice == "a":
        points = 0
        print("\nPlastic bags can be very damaging to marine life.\nThe United Nations Chief of Marine Life said that it is a “planetary crisis.”")
        time.sleep(2)
        print("\nPlease limit your use of plastic bags, and use a reusable shopping bag when shopping!")
    if choice == "B" or choice == "b":
        points = 1
        print("\nThis is an okay option, but make sure to wash and reuse the plastic container. These also do not last as long as other options.")
        time.sleep(2)
        print("\nAdditionally, plastics manufacturing is responsible for a significant amount of greenhouse gas emissions in the U.S.\nAvoid plastic packaging of foods, as well.")
    if choice == "C" or choice == "c":
        points = 2
        print("\nThis is your best option to store food!\nGlass containers last for a long time.")
        time.sleep(2)
        print("\nAlthough glass manufacturing still puts out heavy metal emissions, it’s way less than plastic manufacturing emissions.\nBonus: use stainless steel water bottles and straws, and you’ve got an environmentally-friendly kitchen!")
    return(points)

def brushTeeth():
    print("\nAs the day draws to a close, it becomes time to brush your teeth.")
    time.sleep(3)
    choice = input("What should you to do make sure you save water?\nA. Update your plumbing\nB. Turn off your faucet\nC. Rinse with a cup ")
    if choice == "A" or choice == "a":
        points = 2
        print("\nThere are ecologically-safe faucet heads that conserve about 50% of the water per minute.\nNot only will this lower your water bill, it will help conserve the amount of water you use!\nAlso, make sure you check your living space for dripping pipes or faucets.")
    if choice == "B" or choice == "b":
        points = 1
        print("\nThis is the easiest way to save water.\nThe EPA (Environmental Protection Agency) says that leaving the water running while brushing your teeth wastes an average of four gallons every time.\nThat’s a lot of water!")
    if choice == "C" or choice == "c":
        points = 0
        print("\nThis makes sure you don’t waste water when you rinse!\nMake sure to use a reusable cup instead of paper stacking cups, though.")
    return(points)


def sources():
    moreinfo = input("\nWould you like to learn more information about any of these topics? Enter 'Yes' if so. ")
    while moreinfo == "Yes" or moreinfo == "yes":
        which = input("Which topic would you like to learn more about? A)Starbucks' carbon footprint, B) Composting, C)Recycling, D)Sustainable commuting, E) Plastic usage, or F (all of the sources)? ")
        if which == "A" or which == "a":
            print("Visit https://www.forbes.com/2007/07/02/starbucks-emissions-environment-biz-cz_sn_0703green_carbon.html#4eebb9812681/nto learn more about Carbon Footprint.")
        if which == "B" or which == "b":
            print("Visit https://www.epa.gov/recycle/composting-home to learn more about composting. ")
        if which == "C" or which == "c":
            print("Visit https://www.explainthatstuff.com/recycling.html to learn more about recycling. ")
        if which == "D" or which == "d":
            print("Visit https://www.worldwildlife.org/magazine/issues/summer-2017/articles/reducing-the-impact-of-commuting\nto learn more about sustainable commuting.")
        if which == "E" or which == "e":
            print("Visit https://foodprint.org/issues/the-environmental-impact-of-food-packaging/ to learn more about plastic usage in our oceans, and food packaging in general.")
        if which == "F" or which == "f":
            print("Visit https://www.forbes.com/2007/07/02/starbucks-emissions-environment-biz-cz_sn_0703green_carbon.html#4eebb9812681/nto learn more about Carbon Footprint.")
            print("Visit https://www.epa.gov/recycle/composting-home to learn more about composting. ")
            print("Visit https://www.explainthatstuff.com/recycling.html to learn more about recycling. ")
            print("Visit https://www.worldwildlife.org/magazine/issues/summer-2017/articles/reducing-the-impact-of-commuting\nto learn more about sustainable commuting.")
            print("Visit https://foodprint.org/issues/the-environmental-impact-of-food-packaging/ to learn more about plastic usage in our oceans, and food packaging in general.")
        moreinfo = input("Would you like more information? ")


main()