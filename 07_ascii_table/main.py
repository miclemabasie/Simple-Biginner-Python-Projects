def printASCIITable():
    """
    This function prints out all the list of printable ASCII characters
    which are from 32 to 126 and their corresponding values.
    """
    for i in range(32, 126+1): # printable ASCII characters
        # The chr function takes as argument an ASCII number and 
        # returns the corresponding value associated to it
        print(f"[{i} -> {chr(i)}]", end="  ")
    print("")

def ASSCIIWordTranslator(word):
    """
    This function takes in a word as text and print out
    all the corresponding ASCII values.
    """
    # Loop through all the letter in the word
    for i in word:
        # The ord function takes as argument a value and 
        # returns the corresponding ASSCII value
        print(i, ':', ord(i), end=" | ")
    print("")
    return
    

def main():
    printASCIITable()
    try:
        string = input("Enter a some text to lookup the corresponding ASSCII value: ")
        ASSCIIWordTranslator(string)
    except:
        pass
    

if __name__ == "__main__":
    main()