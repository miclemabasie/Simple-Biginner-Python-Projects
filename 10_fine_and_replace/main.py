def findAndReplace(text, old, new):
    """
    Replaces the old word with new once in all the occurences 
    in the text
    """
    # Get the legth of the text we wish to replace
    lenght_of_old_text = len(old)
    # Loop till the end of the text
    i = 0

    new_string = ''
    text_list = list(text)
    while i < len(text_list):
        # check the current index of i + the len
        # of the new text if it == to new word
        # print(text_list[i:lenght_of_old_text+i])
        if (text_list[i:lenght_of_old_text+i] == list(old)):
            v = 0
            for j in range(i, lenght_of_old_text+i):
                text_list[j] = new[v]
                v += 1
        new_string = ''.join(text_list)
        i += 1
    return new_string
def main():
    print(findAndReplace("some text text", 'text', 'this'))

if __name__ == "__main__":
    main()