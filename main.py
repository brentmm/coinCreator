import math

#list storing coins in users bank
coinBank = []

#value of coins in users bank
bankValue = 0


#Coin info class
""" 
CONSTRUCTOR   
parameter:    
coinName => string    
"""
class coin():
    def __init__(self, coinName):
        self.coinName = coinName
        if self.coinName == "Penny":
            self.material = "94% steel 1.5% nickel 4.5% copper plating"
            self.coinRadius = 9.53
            self.value = 1
        elif self.coinName == "Nickel":
            self.material = "94.5% steel 3.5% copper 2% nickel plating"
            self.coinRadius = 10.60
            self.value = 5
        elif self.coinName == "Dime":
            self.material = "92% steel 5.5% copper 2.5% nickel plating"
            self.coinRadius = 9.02
            self.value = 10
        elif self.coinName == "Quarter":
            self.material = "94% steel 3.8% copper 2.2% nickel plating"
            self.coinRadius = 11.94
            self.value = 25
        elif self.coinName == "Loonie":
            self.material = "91.5% nickel 8.5% bronze plating (88% copper, 12% tin)"
            self.coinRadius = 13.25
            self.value = 100
        elif self.coinName == "Twoonie":
            self.material = "Ring: 99% nickel Centre: 92% copper 6% aluminium 2% nickel"
            self.coinRadius = 14.00
            self.value = 200

    #method finding coins circumference
    def getCircumference(self):
        circumference = str(2 * math.pi * self.coinRadius)
        return circumference

    #method finding coins area
    def getArea(self):
        area = str(math.pi * self.coinRadius * self.coinRadius)
        return area

    #string format after adding a coin
    def __str__(self):
        return (
            "The surface area of one side of a " + self.coinName + " is " +
            coin.getArea(self) + " milimeters, and the circumfrance is " +
            coin.getCircumference(self) + " millimeters. This coin is worth " +
            str(self.value) + " cent(s).")


#Exact change finder class
""" 
CONSTRUCTOR   
parameter:    
valueFind => integer   
"""
class coinFinder():
    def __init__(self, valueFind):
        self.valueFind = valueFind

    #method to determine what coins are needed
    def coinsNeeded(self):
        coinList = ["Twoonie", "Loonie", "Quarter", "Dime", "Nickel", "Penny"]

        #loop to choose coins until required value is met
        while self.valueFind != 0:
            if self.valueFind >= 200:
                coinsNeeded[coinList[0]] += 1
                self.valueFind = self.valueFind - 200
            elif self.valueFind >= 100:
                coinsNeeded[coinList[1]] += 1
                self.valueFind = self.valueFind - 100
            elif self.valueFind >= 25:
                coinsNeeded[coinList[2]] += 1
                self.valueFind = self.valueFind - 25
            elif self.valueFind >= 10:
                coinsNeeded[coinList[3]] += 1
                self.valueFind = self.valueFind - 10
            elif self.valueFind >= 5:
                coinsNeeded[coinList[4]] += 1
                self.valueFind = self.valueFind - 5
            elif self.valueFind >= 1:
                coinsNeeded[coinList[5]] += 1
                self.valueFind = self.valueFind - 1
            else:
                pass

    #string format for coin finder
    def __str__(self):
        coinList = ["Twoonie", "Loonie", "Quarter", "Dime", "Nickel", "Penny"]
        # coinList_index = 0
        neededCoins = ""
        # coinName = coinName = coinList[coinList_index]
        for i in coinList:
            if neededCoins == "":
                neededCoins = neededCoins + (str(coinsNeeded[i])) + " " + i
            else:
                neededCoins = neededCoins + ", " + (str(
                    coinsNeeded[i])) + " " + i
            # coinList_index += 1
        return (str(valueFind) + " cents would be " + neededCoins)


#dict to keep track of coins needed
coinsNeeded = {
    "Twoonie": 0,
    "Loonie": 0,
    "Quarter": 0,
    "Dime": 0,
    "Nickel": 0,
    "Penny": 0
}

#intro
print(
    "Welcome to the BM e-bank program. This program keeps track of the change you find and put in your coin bank, it will also give you cool facts about the coins you add."
)
print()
print("To start off...")

#user selecting action
coinName = input(
    "Enter a Canadian coin to add to your e-bank, type finder to use the change finder, or type quit to end program: "
).capitalize()

#checking if user input is valid
while coinName != "Penny" and coinName != "Nickel" and coinName != "Dime" and coinName != "Quarter" and coinName != "Loonie" and coinName != "Twoonie" and coinName != "Quit" and coinName != "Finder":
    print()
    coinName = input(
        "Please enter the correct spelling of a canadian coin, use the change finder, or quit: "
    ).capitalize()

#running program if user didnt quit
while coinName != "Quit":

    if coinName != "Quit" and coinName != "Total" and coinName != "Finder":  #running coin function
        print()
        coin_Instance = coin(coinName)
        coinBank.append(coinName)  #adding user input coin to bank
        bankValue = bankValue + coin_Instance.value  #adding coin value to total
        print(coin(coinName))  #calling class and printing coin info

    elif coinName == "Total":  #prints users bank total
        print()
        print("You currently have " + str(len(coinBank)) +
              " coins totalling " + str(bankValue) + " cent(s). ")

    elif coinName == "Finder":  #runs function to find change
        print()
        valueFind = int(input("How much change do you need in cents?: ")
                        )  #gets input for amount required to find
        requiredChange = (coinFinder(valueFind))
        requiredChange.coinsNeeded()
        print(requiredChange)  #printing the coins needed

    else:
        pass

    #asking user what they want to do
    print()
    coinName = input(
        "Add another coin, type total to ask for e-bank total, use the change finder, or quit: "
    ).capitalize()

    #checking if user input is valid
    while coinName != "Penny" and coinName != "Nickel" and coinName != "Dime" and coinName != "Quarter" and coinName != "Loonie" and coinName != "Twoonie" and coinName != "Total" and coinName != "Quit" and coinName != "Finder":
        print()
        coinName = input(
            "Please enter the correct spelling of a canadian coin, use the change finder, ask for e-bank total, or quit: "
        ).capitalize

#runs when user quits
print()
print("You have " + str(bankValue) + " cents in your e-bank.")
print()
print("Have a nice day!")
