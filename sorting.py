 def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
         for j in range(0, n-i-1):
             if arr[j] > arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]
     return arr

 numbers = [5, 3, 8, 6, 2]
 print("Sorted List:", bubble_sort(numbers))

#improved bug fix sorting 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# User input for flexibility
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
order = input("Sort in ascending or descending? (a/d): ").lower()

sorted_list = quick_sort(numbers)

if order == 'd':
    sorted_list.reverse()

print("Sorted List:", sorted_list)
