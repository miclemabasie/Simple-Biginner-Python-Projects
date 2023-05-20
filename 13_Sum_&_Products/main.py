
def calculateSum(numbers):
    sum = 0
    if len(numbers) <= 0:
        return sum
    else:
        for number in numbers:
            sum += number
    return sum

def calculateProduct(numbers):
    product = 1
    if len(numbers) <= 0:
        return product
    else:
        for number in numbers:
            product *= number
    return product



def main():
    pass

if __name__=="__main__":
    main()