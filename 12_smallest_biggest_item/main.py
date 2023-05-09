def getSmallest(collection):
    min = None
    # Check if all values of the list are intergers
    i = 0
    for item in collection:
        try:
            int(item)
            i += 1
        except ValueError:
            collection.remove(collection[i])
            i -+ 1
        
    if len(collection) > 0:
        for i in range(len(collection)):
            if min == None:
                min = collection[i]
            if min > collection[i]:
                min = collection[i]
        return min
    else:
        return None

def main():
    collection = [45, 3, 2, 5, 23, 'this', 34]
    print("="*100)
    print(getSmallest(collection))
    print("="*100)


if __name__ == "__main__":
    main()