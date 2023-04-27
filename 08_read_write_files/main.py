def writeToFile(file_name, text):
    """
    Open the file that was passed into the function in write mode 
    and writes to the file
    Note: It overwrites the content of the file.
    """
    with open(file_name, 'w') as file:
        file.write(text)
    
def appendTofile(file_name, text):
    """
    Open the file that is passed into the function in append mode
    and writes to the file.
    Note: This function does not overwrite the original content of the file
    but just adds to it.
    """
    with open(file_name, 'a') as file:
        file.write(text)


def readFromFile(file_name: str) -> str:
    """
    Opends a file and returns the content as text
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File with {file_name} was not found in the given location.."

def main():
    writeToFile("test.txt", "Hi, There!\nGood Morning\n")
    appendTofile("test.txt", "I wish you a lovely day.\n")
    print(readFromFile("test.txt"))

if __name__ == "__main__":
    main()