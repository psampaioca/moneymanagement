class Person:
    def __init__(self,income):
        self.income = income

    def calcPercent(self, houseIncome):
        return self.income/houseIncome

    def transfer(self, houseExpenses, houseIncome):
        personPercent = self.calcPercent(houseIncome)
        personSavings = 0.5 * (self.income - personPercent * houseExpenses)
        if self.income - personPercent * houseExpenses - personSavings <= 200:
            personTransfer = houseExpenses * personPercent + (self.income - houseExpenses * personPercent - 200)
        elif self.income - personPercent * houseExpenses - personSavings > 300:
            personSavings = 0.6 * (self.income - personPercent * houseExpenses)
            personTransfer = houseExpenses * personPercent + personSavings
        else:
            personTransfer = houseExpenses * personPercent + personSavings
        return personTransfer