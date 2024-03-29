#Ali Rajgarah 1586471

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    pivot = (i + k) // 2
    middle_element = i

    while (middle_element <= k):
        while (user_ids[middle_element] < user_ids[pivot]):
            middle_element = middle_element + 1
        while (user_ids[k] > user_ids[pivot]):
            k = k - 1

        if (middle_element <= k):
            t = user_ids[middle_element]
            user_ids[middle_element] = user_ids[k]
            user_ids[k] = t
            middle_element = middle_element + 1
            k = k - 1
    return middle_element


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if (i >= k):
        return
    middle_element = partition(user_ids, i, k)
    quicksort(user_ids, i, middle_element - 1)
    quicksort(user_ids, middle_element, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
