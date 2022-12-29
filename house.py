class House:
    def __init__(self, people, houseIncome, houseExpenses):
        self.people = people
        self.houseIncome = houseIncome
        self.houseExpenses = houseExpenses

    def defineTransfer(self, names, peopleList):
        peopleTransfer = []
        if self.houseIncome <= (self.houseExpenses + self.people * 100):
            outcome = f"Ok, you made less or equal to C${self.houseExpenses + self.people * 100} (spent + C${self.people * 100}), each keeps C$100.00 and:\n"
            for i in range(self.people):
                outcome += f"{names[i]} has to transfer back to mutual account: C${peopleList[i].income - 100}.\n"
        elif (self.houseExpenses + self.people * 100) < self.houseIncome <= (self.houseExpenses + self.people * 200):
            outcome = f"Ok, you made more than C${self.houseExpenses + self.people * 100} (spent + C${self.people * 100}), but made less or equal to C${self.houseExpenses + self.people * 200} (spent + C${self.people * 200}), each keeps C${(self.houseIncome - self.houseExpenses)/self.people}, and:\n"
            for i in range(self.people):
                outcome += f"{names[i]} has to tranfer back to mutual account: C${peopleList[i].income - (self.houseIncome - self.houseExpenses)/self.people}.\n"
        else:
            outcome = f"Well done! You made more than C${self.houseExpenses + self.people * 200} (spent + C${self.people * 200}):\n"
            for i in range(self.people):
                peopleTransfer.append(peopleList[i].transfer(self.houseExpenses, self.houseIncome))
                outcome += f"{names[i]} has to tranfer back to mutual account: C${peopleTransfer[i]}.\n"
            if sum(peopleTransfer) < self.houseExpenses:
                outcome += f"Whoever made more money has to transfer this amount instead: C${self.houseExpenses - min(peopleTransfer)}."
        for i in range(self.people):
            outcome += f"{names[i]}'s allowance is C${peopleList[i].income - peopleTransfer[i]}.\n"
        outcome += f"House is keeping C${sum(peopleTransfer) - self.houseExpenses}."
        return outcome