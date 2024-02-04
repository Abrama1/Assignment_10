import random

# Task_1


def generate_random_list():

    return [random.randint(1, 1000) for _ in range(100)]


def linear_search(lst, target):

    for i, num in enumerate(lst):

        if num == target:

            return i

    return -1


def binary_search(sorted_lst, target):

    low, high = 0, len(sorted_lst) - 1

    while low <= high:

        mid = (low + high) // 2
        mid_element = sorted_lst[mid]

        if mid_element == target:

            return mid

        elif mid_element < target:

            low = mid + 1

        else:

            high = mid - 1

    return -1


random_list = generate_random_list()
print("Generated Random List:", random_list)

element_to_find = random.choice(random_list)
print("Element to Find:", element_to_find)

linear_search_result = linear_search(random_list, element_to_find)
print("Linear Search Result:", linear_search_result)

sorted_list = sorted(random_list)

binary_search_result = binary_search(sorted_list, element_to_find)
print("Binary Search Result:", binary_search_result)


# Task_2

multiples_of_three = lambda x: x % 3 == 0


def fill_indices_with_lambda(input_list, search_lambda):

    indexes_list = []

    for i, element in enumerate(input_list):

        if search_lambda(element):

            indexes_list.append(i)

    return indexes_list


my_list = [1, 3, 5, 6, 92, 1, 15, 18, 21, 25, 27]

filtered_indexes = fill_indices_with_lambda(my_list, multiples_of_three)

print("Original List:", my_list)
print("Indices of Multiples of Three:", filtered_indexes)

