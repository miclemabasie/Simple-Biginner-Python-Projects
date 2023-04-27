
def getChessSquareColor(col, row):
    if col > 7 or row > 7:
        return f"Out of bounds"
    # if the even/oddness of the columns and row match, return 'white'
    if row % 2 == col % 2:
        return f"White"
    else: # if they don't match, then return black
        return f"Black"
  


def main():
    # get the col and row from the user
    try:
        col = int(input("Enter the column: "))
        row = int(input("Enter the row: "))
        print(getChessSquareColor(col, row))
    except:
        print(f"Error input!")

if __name__ == "__main__":
    main()
