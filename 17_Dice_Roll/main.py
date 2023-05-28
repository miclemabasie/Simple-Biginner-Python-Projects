import random

def rollDice(numberOfDice):
    running_total = 0    
    for i in range(numberOfDice):
        running_total += random.randint(1, 6)

    return running_total

def main():
    print(rollDice(100))

if __name__ == "__main__":
    main()