suffixes = {'0': 'th', '1': 'st', '2':'nd', '3':'rd', '4':'th', '5':'th', '7':'nth', '8':'th', '9':'th'}

def ordinal_suffix(n):
    # convert the number n into a string
    n_string = str(n)
    # get the last digit in the string in a case the the number is more than 1 integer
    last_digit = n_string[-1]
    if n_string.endswith('11') or n_string.endswith("12") or n_string.endswith('13'):
        valid_suffix = 'th'
    else:
        # get the suffix from the dictionary by matching
        for number, suffix in suffixes.items():
            # Check if the number is same as last digit 
            # and get the corresponding suffiex
            if number == last_digit:
                valid_suffix = suffix
                break
    # append the suffix to the original string
    final_string = n_string+valid_suffix
    return final_string


def main():
    try:
        value = int(input("Enter an integer to get the suffix: "))
        print(ordinal_suffix(value))
    except ValueError:
        print("Enter a valid integer.")
    
if __name__ == "__main__": 
    main()
        