import house
import person

people = int(input("How many people with income? "))
names = []
peopleList = []
for i in range(people):
    names.append(input(f"Please enter name for person {i + 1}: "))

print(f"Hello {names}! Today is the last day of the month and we need to balance the accounts. Let's do this?")
try:
    x = 1
    while x == 1:
        for i in range(people):
            peopleList.append(person.Person(float(input(f"Please, enter last month's income for {names[i]}: "))))
        mainHouse = house.House(people, sum(person.Person.income for person.Person in peopleList), float(input("Please, enter last month's expenses for the house: ")))
        print(f"Total house income was: C$ {mainHouse.houseIncome}.")
        for i in range(people):
            print(f"{names[i]}'s income represents {peopleList[i].calcPercent(mainHouse.houseIncome) * 100}%.")
        print(mainHouse.defineTransfer(names, peopleList))
        y = 1    
        while y == 1:    
            answer = input("Do you want to repeat? (Y/N): ").lower()
            if answer == "n":
                x = 2
                y = 2
            elif answer == "y":
                x = 1
                y = 2
            else:
                print("Please, enter Y or N!")
except:
    print('Error, please enter numeric input')