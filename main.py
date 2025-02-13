import matplotlib
import numpy
import json
import string
import random

DEFAULTS = [{
    "Currency": [
        {
            "currency_Name" : "United States Dollar",
            "isoCode": "USD",
            "value": 1.00
        },
        {
            "currency_Name": "Euro",
            "isoCode": "EUR",
            "value": .97
        },
        {
            "currency_Name": "Pound Sterling",
            "isoCode": "GBP",
            "value": .81
        },
        {
            "currency_Name": "Canadian Dollar",
            "isoCode": "CAD",
            "value": 1.44
        },
        {
            "currency_Name": "Swiss Franc",
            "isoCode": "CHF",
            "value": .91
        },
        {
            "currency_Name": "Japanese Yen",
            "isoCode": "JPY",
            "value": 155.15
        },
        {
            "currency_Name": "Australian Dollar",
            "isoCode": "AUD",
            "value": 1.61
        },
        {
            "currency_Name": "Hong Kong Dollar",
            "isoCode": "HKD",
            "value": 7.79
        },
        {
            "currency_Name": "New Zealand Dollar",
            "isoCode": "NZD",
            "value": 1.78
        },
        {
            "currency_Name": "Swedish Krona",
            "isoCode": "SEK",
            "value": 11.07
        },
        {
            "currency_Name": "South Korean Won",
            "isoCode": "KRW",
            "value": 1460.15
        },
        {
            "currency_Name": "Singapore Dollar",
            "isoCode": "SGD",
            "value": 1.36
        },
        {
            "currency_Name": "Norwegian Krone",
            "isoCode": "NOK",
            "value": 11.35
        },
        {
            "currency_Name": "Mexican Peso",
            "isoCode": "MXN",
            "value": 20.34
        },
        {
            "currency_Name": "Majeks Universal Currency",
            "isoCode": "MUX",
            "value": 1.002
        } 
        ]
    }
]


class Currency:
    def __init__(self):
        print("Initializing Currency object...")
        self.currencyList = []
        self.muxValue = 0
        self.concurrentHit = 0
        
        self.lastHit = [0, 0] #check to see if Last was Positive or Negative

    def addCurrency(self, currency: dict): 
        # Check if the currency already exists (by isoCode)
        index = next((i for i, record in enumerate(self.currencyList) if record["isoCode"] == currency["isoCode"]), None)

        if index is not None:
            # Replace the existing currency
            self.currencyList[index] = currency
            # print(f'Updated {currency["isoCode"]} in the currencyList')
        else:
            # Add the new currency
            self.currencyList.append(currency)
            # print(f'{currency["isoCode"]} has been added to the currencyList')

    # def init_MUX(self):
    #     for i, record in enumerate(self.currencyList):
    #         if record["isoCode"] == "MUX":
    #             self.muxValue =  record["value"]


    def removeCurrency(self, currencyIso: str):
        index = next((i for i, record in enumerate(self.currencyList) if record["isoCode"] == currencyIso), None)

        if index is not None:
            self.currencyList.pop(index)
            print(f'{currencyIso} has been removed from the Currency List')
        else:
            print(f'{currencyIso} does not exist in the Currency List')  
        
    def postCurrencyList(self):
        print(f'Current Currency List: {self.currencyList}')

    def printCurrencyValue(self):
        # print(self.currencyList)
        for _ in self.currencyList:
            print(_['isoCode'])
            # print(self.currencyList[i]["isoCode"])
        isoChoice = input( f'Please Select a Currency from the List: ')

        isoReturn = next((i for i, record in enumerate(self.currencyList) if isoChoice.upper() == record["isoCode"].upper()), None)
        # print(isoReturn) 
        if isoReturn is not None:
            print(f'The {self.currencyList[isoReturn]["currency_Name"]} is valued at: ' + "{:.2f}".format(self.currencyList[isoReturn]["value"]))

    def runIterations(self):
        iterations = input("Please enter the number of iterations you would like to run: ")
        for i in range(int(iterations)):
            print(f'Iteration [{i+1}] Started!')
            self.scalingValues()
            print(f'Iteration [{i+1}] Completed!')
        print(f'All Iterations Complete')


    def printConversionRate(self):
        iso1 = input("Please Enter The ISO of the First Value: ")
        iso2 = input("Please Enter The ISO of the Second  Value: ")
        index1 = next((i for i, record in enumerate(self.currencyList) if record["isoCode"] == iso1), None)
        index2 = next((i for i, record in enumerate(self.currencyList) if record["isoCode"] == iso2), None)

        if index1 is not None:
            val1 = self.currencyList[index1]["value"]
        else:
            print(f'Cannot find {iso1} in the Currency List')
        
        if index2 is not None:
            val2 = self.currencyList[index2]["value"]
        else:
            print(f'Cannot find {iso2} in the Currency List')
        
        if val1 and val2:
            conversionRate = val2/val1
            print(f'The Conversion rate from {iso1} to {iso2} is {conversionRate}') 
    
    def invest(self):

        print(f'The Current Value of MUX is: {self.muxValue}')
        if self.muxValue <= -0.75:
            print("You're Fucked if you do, Bro.")
        elif self.muxValue <= -0.5 and self.muxValue > -0.75:
            print("Don't Invest.")
        elif self.muxValue <= -0.25 and self.muxValue > -0.5:
            print("Meh, Not the best. But it could be worse. Probably not though.")
        elif self.muxValue <= 0 and self.muxValue > -0.25:
            print("Could be worse. Sit on it. I would say its okay!")
        elif self.muxValue <= 0.25 and self.muxValue > 0:
            print("Wouldn't hurt. Go for it!")
        elif self.muxValue <= 0.5 and self.muxValue > 0.25:
            print("Looking Good! Invest!")
        elif self.muxValue <= 0.75 and self.muxValue > 0.5:
            print("Why haven't you invested? This shit is golden")
        elif self.muxValue <= 1 and self.muxValue > 0.75:
            print("BOI, PUT YO DAMN DOLLAR IN THE MUX!!! IT'S GOLDEN HOUR!!!") 
    
    def scaler(self, concurrentHit, muxValue, magnitude):
        scalingValue = 0.00
        if concurrentHit < 2:
            scalingValue = .5
        elif concurrentHit < 3:
            scalingValue = 1.0
        elif concurrentHit < 4:
            scalingValue = 2.5
        elif concurrentHit < 5:
            scalingValue = 5.0
        elif concurrentHit < 10:
            scalingValue = 10.00
        else:
            scalingValue = 15.0

        muxValue += (-1 * scalingValue) * magnitude
        if muxValue <= -1:
            return -1.00
        elif muxValue >= 1:
            return 1.00

        return muxValue
    

    def scalingValues(self):
        random.seed()

        for i, record in enumerate(self.currencyList):
            if record["isoCode"] ==  "MUX":
                average = 0.00
                for j in range(5):
                    average = average + self.currencyList[j]["value"]
                average = average/5
                if average < record["value"]:
                    magnitude = average - record["value"]
                    self.muxValue = self.scaler(self.concurrentHit, self.muxValue, magnitude)
                    self.lastHit[0] = self.lastHit[1]
                    self.lastHit[1] = 1 #Negative
                else:
                    magnitude = average - record["value"]
                    self.muxValue = self.scaler(self.concurrentHit, self.muxValue, magnitude)
                    self.lastHit[0] = self.lastHit[1]
                    self.lastHit[1] = 0 #Postive
                if self.lastHit[0] == self.lastHit[1]:
                    self.concurrentHit += 1
                else:
                    self.concurrentHit = 1
            
                record["value"] = average
            elif record["isoCode"] ==  "USD":
                pass
            else:
                r = random.randint(0,5)
                rDouble = r/1000
                isNegative = random.randint(0,1)
                
                if isNegative == 1:
                    rDouble = rDouble * -1
                    if record["value"] >= 0.05:
                        record["value"] = record["value"] + rDouble 
                else:
                    if record["value"] >= 0.05:
                        record["value"] = record["value"] + rDouble 

                
    

if __name__ == "__main__":
    currencyList = Currency()  

    for default in DEFAULTS:  
        for currency in default["Currency"]:  
            currencyList.addCurrency(currency)
    print("Defaults have been initialized!")
    
    while True:
        print("============================")
        print("Welcome to Majeks Currency!")
        print("============================")
        print("1. Display current Currencies \n"
        + "2. Print Currency Value \n"
        + "3. Compare Two Currency Values \n"
        + "4. Run Iterations \n"
        + "5. Should you Invest? \n"
        + "6. Exit \n")
        userInput = input("Your Choice: ")

        if userInput == "1":
            currencyList.postCurrencyList()
        elif userInput == "2":
            currencyList.printCurrencyValue()
        elif userInput == "3":
            currencyList.printConversionRate()
        elif userInput == "4":
            currencyList.runIterations()
        elif userInput == "5":
            currencyList.invest()
        elif userInput == "6":
            print("Thank you for using Majeks Currency, See you later!")
            break
        else:
            print("Invalid Input!")


