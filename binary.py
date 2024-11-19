# def binary_search(arr, item):
#     low = 0
#     high = len(arr) - 1
    
#     while low <= high:
#         mid = (high + low) //2
#         print(f"mid is: {mid}")
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#             print(f"high is: {high}")
#         else:
#             low = mid + 1
#             print(f"low is: {low}")
#     return None

# my_list = [1 , 2, 5, 6, 8, 9]
# print(binary_search(my_list, 6))

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#             if arr[i] < smallest:
#                     smallest = arr[i]
#                     smallest_index = i
#     return smallest_index

# def selectionSort(arr):
#     newArr = []
#     copiedArr = list(arr)
#     for _ in range(len(copiedArr)):
#         smallest = findSmallest(copiedArr)
#         newArr.append(copiedArr.pop(smallest))
#     return newArr

# print(selectionSort([5, 2, 6, 7, 1, 9]))

# def sum(list):
#     if not list:
#         return 0
#     else:
#         return list[0] + sum(list[1:])
    
    
# def count_items(lst):
#     if not lst:
#         return 0
#     else:
#         return 1 + count_items(lst[1:])
    
# lst = [1, 2, 3]
# print(count_items(lst))



# def find_max(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_of_rest = find_max(lst[1:])
#         return lst[0] if lst[0] > max_of_rest else max_of_rest


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]

#         greater = [i for i in array[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# array = [2, 5, 6, 8, 1, 3, 4, 9, 7]
# print(quicksort(array))

# voted = {}
# def check_voter(name):
#     if name in voted:
#         print('kick them out!')
#     else:
#         voted[name] = True
#         print('let them vote!')

# check_voter("tom")
# check_voter("tom")

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         # insert "key" into sorted sequence arr(0, i - 1)
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key 

# arr = [5, 2, 4, 6, 1, 3]
# insertion_sort(arr)

# print(arr)

# def insertion_sort_decrease(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]

#         j = i - 1
#         while j >=0 and arr[j] < key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# arr = [5, 2, 4, 6, 1, 3]
# insertion_sort_decrease(arr)
# print(arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i])
    sorted_array.extend(right[j])
