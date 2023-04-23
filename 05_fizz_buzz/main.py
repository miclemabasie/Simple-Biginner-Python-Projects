def fizz_buzz(upto):
    for i in range(1, upto+1):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FIZZ-BUZZ", end="  ")
        elif (i % 3) == 0:
            print("FIZZ", end="  ")
        elif (i % 5) == 0:
            print("BUZZ", end="  ")
        else:
            print(i, end="  ")
    print("")


def main():
    try:
        upto = int(input("Enter a number for the FIZZ BUZZ game: "))
        fizz_buzz(upto)
    except ValueError:
        print("Error! The value you entered was not an integer.")

if __name__ == "__main__":
    main()