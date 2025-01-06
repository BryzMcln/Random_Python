import random, os
#from clear import *

def clr(): #clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

# sort a list using stupid sort
def stupid_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list

# sort a list using radix sort
def radix_sort(num_list):
    max_num = max(num_list)
    exp = 1
    while max_num // exp > 0:
        counting_sort(num_list, exp)
        exp *= 10
    return num_list

#sort a list using counting sort
def counting_sort(num_list, exp):
    n = len(num_list)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = num_list[i] // exp % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n-1
    while i >= 0:
        index = num_list[i] // exp % 10
        output[count[index]-1] = num_list[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        num_list[i] = output[i]
    

# sort a list using quick sort
def quick_sort(num_list):
    if len(num_list) > 1:
        pivot = random.choice(num_list)
        left = [x for x in num_list if x < pivot]
        right = [x for x in num_list if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return num_list

# sort a list using merge sort
def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1
    return num_list

# sort a list using selection sort
def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if num_list[min_index] > num_list[j]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list

# sort a list using insertion sort
def insertion_sort(num_list):
    n = len(num_list)
    for i in range(1, n):
        key = num_list[i]
        j = i - 1
        while j >= 0 and num_list[j] > key:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = key
    return num_list

#sort a list using bubble sort
def bubble_sort(num_list): 
    n = len(num_list)
    for i in range(n):
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

#generate a random number in a list
def random_number_list(n):
    num_list = random.sample(range(0, 100), n)
    return num_list


def sorting():
    clr()
    print("==========================")
    print("Sorting Algorithms:")
    print("""==========================
    1. Bubble Sort
    2. Insertion Sort
    3. Selection Sort
    4. Merge Sort 
    5. Quick Sort
    6. Radix Sort
    7. Counting Sort
    8. Stupid Sorting
    9. Built-in Sort
    10. All Sorting
    0. Exit""")
    print("==========================")

    choice = None
    while choice not in range(11):
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(11):
                print("==========================")
                print("Invalid choice. Try again.")
        except ValueError:
            print("==========================")
            print("Invalid choice. Try again.")
    
    if choice == 1:
        type = "Bubble Sort"
    elif choice == 2:
        type = "Insertion Sort"
    elif choice == 3:
        type = "Selection Sort"
    elif choice == 4:
        type = "Merge Sort"
    elif choice == 5:
        type = "Quick Sort"
    elif choice == 6:
        type = "Radix Sort"
    elif choice == 7:
        type = "Counting Sort"
    elif choice == 8:
        type = "Stupid Sort"
    elif choice == 9:
        type = "Built-in Sort"
    elif choice == 10:
        type = "All Sorting"
    
    while True:
        try:
            print("==========================")
            num_list = random_number_list(int(input(f"Enter to generate a list of random numbers for {type}: ")))
            if num_list == "":
                print("==========================")
                print("Invalid input. Try again.")
                continue
            else:
                print(f"List: {num_list}")
                break
        except ValueError:
            print("Invalid input. Try again.")
    if choice == 1:
        print(f"Bubble Sorted List: {bubble_sort(num_list)}")
    elif choice == 2:
        print(f"Insertion Sorted List: {insertion_sort(num_list)}")
    elif choice == 3:
        print(f"Selection Sorted List: {selection_sort(num_list)}")
    elif choice == 4:
        print(f"Merge Sorted List: {merge_sort(num_list)}")
    elif choice == 5:
        print(f"Quick Sorted List: {quick_sort(num_list)}")
    elif choice == 6:
        print(f"Radix Sorted List: {radix_sort(num_list)}")
    elif choice == 7:
        print(f"Counting Sort List: {counting_sort(num_list, 1)}")
    elif choice == 8: 
        print(f"Stupid Sorted List: {stupid_sort(num_list)}")
    elif choice == 9:
        print(f"Built-in Sorted List: {sorted(num_list)}")
    elif choice == 10:
        print(f"Bubble Sorted List: {bubble_sort(num_list)}")
        print(f"Insertion Sorted List: {insertion_sort(num_list)}")
        print(f"Selection Sorted List: {selection_sort(num_list)}")
        print(f"Merge Sorted List: {merge_sort(num_list)}")
        print(f"Quick Sorted List: {quick_sort(num_list)}")
        print(f"Radix Sorted List: {radix_sort(num_list)}")
        #print(f"Counting Sort List: {counting_sort(num_list, 1)}")
        print(f"Stupid Sorted List: {stupid_sort(num_list)}")
        print(f"Built-in Sorted List: {sorted(num_list)}")
    elif choice == 0:
        exit()
    else:
        sorting()
    
if __name__ == "__main__":
    sorting()