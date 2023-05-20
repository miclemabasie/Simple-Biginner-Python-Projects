
def average(numbers):
    avg = None
    if len(numbers) <= 0:
        return avg
    else:
        # get the sum of numbers in the list
        sum = 0
        for num in numbers:
            sum += num
        avg = sum / len(numbers)
    return avg

def main():
    pass

if __name__=="__main__":
    main()