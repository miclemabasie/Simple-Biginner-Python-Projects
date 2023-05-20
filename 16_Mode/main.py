def mode(numbers):
    mode = None
    if len(numbers) <= 0:
        return mode
    else:
        # Create a dictionary with count of every instance in numbers
        num_count_dict = dict()
        for i in numbers:
            num_count_dict[i] = num_count_dict.get(i, 0) + 1
        numbers = []
        numbers = sorted([(k, v) for v, k in num_count_dict.items()], reverse=True)

    return numbers[0][1]


def main():
    print(mode([23, 343, 12, 12, 23, 12, 34, 123]))


if __name__ == "__main__":
    main()