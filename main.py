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
        self.lastHit = 0 #check to see if Last was Positive or Negative
        

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
        
    def postCurrencyList(self):
        print(f'Current Currency List: {self.currencyList}')

    def removeCurrency(self, currencyIso: str):
        index = next((i for i, record in enumerate(self.currencyList) if record["isoCode"] == currencyIso), None)

        if index is not None:
            self.currencyList.pop(index)
            print(f'{currencyIso} has been removed from the Currency List')
        else:
            print(f'{currencyIso} does not exist in the Currency List')  

    def getConversionRate(self, iso1:str, iso2: str):
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
    
    def postCurrencyValue(self):
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
            #Scaling Values()
            print(f'Iteration [{i+1}] Completed!')
        print(f'All Iterations Complete')

    def scalingValues(self):
        random.seed()
        r = random.randint(0,99)
        isNegative = random.randint(0,1)







if __name__ == "__main__":
    currencyList = Currency()  

    for default in DEFAULTS:  
        for currency in default["Currency"]:  
            currencyList.addCurrency(currency)
   
    print("Defaults have been initialized!")

    # currencyList.getConversionRate("GBP", "JPY")
    currencyList.postCurrencyValue()
    

