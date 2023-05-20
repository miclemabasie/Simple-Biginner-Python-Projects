

def median(numbers):
    is_even = 0
    med = None
    if len(numbers) <= 0:
        return med
    else:
        numbers.sort()
        left_half = len(numbers) // 2
        if len(numbers) % 2 == 0:
            is_even = 1
        if is_even:
            med = (numbers[left_half -1] + numbers[left_half]) / 2
            return med
        else:
            med = numbers[left_half]
    return med




def main():
    pass


if __name__ == "__main__":
    main()