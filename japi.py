import urllib.request, json, datetime 


def getStockData(stock=''):
    #creating a variable of the website name
    web = 'https://www.alphavantage.co/query'
    functionType = '?function=GLOBAL_QUOTE'
    functionVariable1 = '&symbol=' + stock
    #functionVariable2 = '&interval=60min'
    apiKEY = '&apikey=1NW1R7FS01RAQU1I'


    webQuery = web + functionType + functionVariable1 + apiKEY


    #creating connection to website
    connection = urllib.request.urlopen(webQuery)

    #reads and decodes the website
    responseString = connection.read().decode()

    theJSON = json.loads(responseString)

    quote = theJSON["Global Quote"]
    quoteStr = str(quote["05. price"])
    print("\nThe current price of %s is: %s\n" % (stock, quote["05. price"]))

    rowReturn = ('The current price of ' + stock + ' is: ' + quoteStr)

    return rowReturn

def main():
    x = 0
    rows = []

    while x != 1:
        userInput = input('Select an option.\n1. Get Stock Price\n2. Output to file\n3. Quit Application\n')

        if userInput == '1':
            stock = input('\nEnter the stock symbol: ')
            rows.append(getStockData(stock))

        elif userInput == '2':
            f = open("japi.out", "w")
            f.write(str(rows))
            f.close()
            print('\nFile created!\n\n')

        elif userInput == '3':
            x += 1


main()




