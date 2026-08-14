# =========================================================
# Assignment-4: Lists (Arrays) in Python
# =========================================================

numbers = [10, 20, 30, 40, 50, 20, 10, 60, 70]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


# =========================================================
# 1. Sum of Elements
# =========================================================

print("1. Sum of Elements")


def sum_of_elements(lst):
    return sum(lst)


print("Sum:", sum_of_elements(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 2. Average of Elements
# =========================================================

print("2. Average of Elements")


def average_of_elements(lst):
    return sum(lst) / len(lst)


print("Average:", average_of_elements(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 3. Find Index of an Element
# =========================================================

print("3. Find Index of an Element")

element = 40

if element in numbers:
    print("Index of", element, "is:", numbers.index(element))
else:
    print("Element not found.")

print("\n" + "=" * 50 + "\n")


# =========================================================
# 4. Check Element Presence
# =========================================================

print("4. Check Element Presence")


def check_element(lst, value):
    return value in lst


print("Is 30 present?", check_element(numbers, 30))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 5. Remove an Element
# =========================================================

print("5. Remove an Element")


def remove_element(lst, value):
    if value in lst:
        lst.remove(value)
    return lst


print("Updated List:", remove_element(numbers.copy(), 20))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 6. Copy a List
# =========================================================

print("6. Copy a List")


def copy_list(lst):
    return lst.copy()


copied_list = copy_list(numbers)

print("Copied List:", copied_list)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 7. Insert Element at Position
# =========================================================

print("7. Insert Element at Position")


def insert_element(lst, index, value):
    lst.insert(index, value)
    return lst


print("Updated List:", insert_element(numbers.copy(), 2, 99))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 8. Find Minimum and Maximum
# =========================================================

print("8. Find Minimum and Maximum")


def find_min_max(lst):
    return min(lst), max(lst)


minimum, maximum = find_min_max(numbers)

print("Minimum Value:", minimum)
print("Maximum Value:", maximum)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 9. Reverse a List
# =========================================================

print("9. Reverse a List")


def reverse_list(lst):
    return lst[::-1]


print("Reversed List:", reverse_list(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 10. Find Duplicate Elements
# =========================================================

print("10. Find Duplicate Elements")


def find_duplicates(lst):

    duplicates = []

    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates


print("Duplicate Elements:", find_duplicates(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 11. Count Even and Odd Numbers
# =========================================================

print("11. Count Even and Odd Numbers")


def count_even_odd(lst):

    even_count = 0
    odd_count = 0

    for num in lst:

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


even, odd = count_even_odd(numbers)

print("Even Numbers Count:", even)
print("Odd Numbers Count:", odd)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 12. Common Elements Between Two Lists
# =========================================================

print("12. Common Elements Between Two Lists")

common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print("Common Elements:", common_elements)

print("\n" + "=" * 50 + "\n")


# =========================================================
# 13. Remove Duplicates
# =========================================================

print("13. Remove Duplicates")


def remove_duplicates(lst):
    return list(set(lst))


print("List Without Duplicates:", remove_duplicates(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 14. Second Largest Element
# =========================================================

print("14. Second Largest Element")


def second_largest(lst):

    unique_list = list(set(lst))
    unique_list.sort()

    return unique_list[-2]


print("Second Largest Element:", second_largest(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 15. Difference Between Max and Min
# =========================================================

print("15. Difference Between Max and Min")


def difference_max_min(lst):
    return max(lst) - min(lst)


print("Difference:", difference_max_min(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 16. Check for Specific Elements
# =========================================================

print("16. Check for Specific Elements")


def check_specific_elements(lst):
    return 12 in lst and 23 in lst


sample_list = [5, 12, 23, 45]

print("Contains 12 and 23:", check_specific_elements(sample_list))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 17. Unique Elements Only
# =========================================================

print("17. Unique Elements Only")


def unique_elements(lst):

    unique = []

    for item in lst:
        if lst.count(item) == 1:
            unique.append(item)

    return unique


print("Unique Elements:", unique_elements(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 18. Frequency Count
# =========================================================

print("18. Frequency Count")


def frequency_count(lst):

    frequency = {}

    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1

    return frequency


print("Frequency Count:", frequency_count(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 19. List Sorting Without Built-in Functions
# =========================================================

print("19. List Sorting Without Built-in Functions")


def bubble_sort(lst):

    sorted_list = lst.copy()

    n = len(sorted_list)

    for i in range(n):

        for j in range(0, n - i - 1):

            if sorted_list[j] > sorted_list[j + 1]:

                sorted_list[j], sorted_list[j + 1] = (
                    sorted_list[j + 1],
                    sorted_list[j]
                )

    return sorted_list


print("Sorted List:", bubble_sort(numbers))

print("\n" + "=" * 50 + "\n")


# =========================================================
# 20. Merge Two Lists Without Duplicates
# =========================================================

print("20. Merge Two Lists Without Duplicates")


def merge_lists_without_duplicates(lst1, lst2):
    return list(set(lst1 + lst2))


merged_list = merge_lists_without_duplicates(list1, list2)

print("Merged List:", merged_list)

print("\n" + "=" * 50 + "\n")
