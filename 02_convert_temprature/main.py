import sys


def convert_to_celsius(temperature):
    """
    Converts temperature from fahraheit to celsius.
    """
    print(f"Converting {temperature}F into Celsius...\n")
    result = (temperature - 32) * (5 / 9)
    print(f"{temperature}F is: {result}C.")
    return result


def convert_to_fahranhiet(temperature):
    """
    Convers temperature from celsius to fahranhiet.
    """
    print(f"Converting {temperature} C into Fahranhiet...\n")
    result = (temperature * (9 / 5)) + 32
    print(f"{temperature}C is: {result}F.")
    return result


def main():
    try:
        choice = int(input("Enter 1 (Cel to Fah) and 2 for (Fah to Cel): "))
    except ValueError:
        print("Invalid input.")
        sys.exit()
    # Check the choice to know which function to call
    if choice == 1:
        temperature = int(input("Enter the temperature in Celsius: "))
        convert_to_fahranhiet(temperature)
        return True
    if choice == 2:
        temperature = int(input("Enter the temperature in Fahranhiet: "))
        convert_to_celsius(temperature)
        return True
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    main()
