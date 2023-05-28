
def getCostOfCoffee(number_of_coffee, price_of_coffee):
    if number_of_coffee > 8:
        free = number_of_coffee // 8
        number_of_coffee = number_of_coffee - free
        return number_of_coffee * price_of_coffee
    return number_of_coffee * price_of_coffee

def main():
    print(getCostOfCoffee(7, 2.50), end="\n")
    print(getCostOfCoffee(8, 2.50), end="\n")
    print(getCostOfCoffee(9, 2.50), end="\n")
    print(getCostOfCoffee(10, 2.50), end="\n")

if __name__ == "__main__":
    main()