def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high) / 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None

my_list = sorted([1,2,5,6,7,4,8,23,54,123,65,765])
print binary_search(my_list,5) # return 3