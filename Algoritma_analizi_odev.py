from timeit import default_timer as timer
import random

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
 
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
 

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        number = bucket[i]
        j = i - 1
        while (j >= 0 and number < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = number

def bucket_sort(array):
    max_number = max(array)
    size = max_number / len(array)

    bucket_list = []
    for x in range(len(array)):
        bucket_list.append([])

    for i in range(len(array)):
        j = int(array[i] / size)
        if j != len(array):
            bucket_list[j].append(array[i])
        else:
            bucket_list[len(array) - 1].append(array[i])

    for z in range(len(array)):
        insertion_sort(bucket_list[z])

    result_list = []
    for x in range(len(array)):
        result_list = result_list + bucket_list[x]
    return result_list

def counting_sort(arr, exp1): 
  
    n = len(arr) 
  
    output = [0] * (n) 
  
    count = [0] * (10) 
  
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int(index % 10)] += 1
  
    for i in range(1, 10): 
        count[i] += count[i - 1] 
  
    i = n - 1
    while i >= 0: 
        index = (arr[i] / exp1) 
        output[count[int(index % 10)] - 1] = arr[i] 
        count[int(index % 10)] -= 1
        i -= 1
  
    i = 0
    for i in range(0, len(arr)): 
        arr[i] = output[i] 

def radixSort(arr): 
  
    max1 = max(arr) 
  
    exp = 1
    while max1 / exp > 0: 
        counting_sort(arr, exp) 
        exp *= 10
  

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def linearsearch(arr, n, x,process): 

    for i in range(0, n):
        process += 1
        if (arr[i] == x): 
            return i,process
    return -1,process
  


def binarySearch (arr, l, r, x,process):
  
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        if arr[mid] == x:
            process+=1
            return mid,process
           
        elif arr[mid] > x: 
            process+=1
            return binarySearch(arr, l, mid-1, x,process) 
   
        else: 
            process+=1
            return binarySearch(arr, mid + 1, r, x,process) 
  
    else:  
        return -1


def menu():
    print("""Creating an array""")
    lengthofarray = int(input("Please enter array length: "))
    minlimit = int(input("Minimum length of range: "))
    maxlimit = int(input("Maximum length of range: "))
    while(minlimit >= maxlimit):
        print("Minimum length cannot be smaller than maximum.")
        minlimit = int(input("Minimum length of range: "))
        maxlimit = int(input("Maximum length of range: "))
    allarrays = {}
    arr = []
    for i in range(lengthofarray):
        arr.append(random.randint(minlimit,maxlimit))
    print(arr)
    print("""You can use sorting or searching algorithms below.
    1. Searching
    2. Sorting
    q for quit
    """)
    option = input("Select an option: ")
    if(option == "q"):
        return option
    elif(option == "1" or option == "2" or option == "3"):
        if option == "1":
            print("""Searching algorithms
            1. Linear
            2. Binary
            3. All
            q for quit""")
            option = input("Select an option: ")
            if option == "1":
                print("Linear")
                number = int(input("Please enter a number for search: "))
                start = timer()
                linearsearch(arr,len(arr),number,0)
                end = timer()
                returnvalue,proc = linearsearch(arr,len(arr),number,0)
                print("Linear search searching time : ", str(end-start))
                if returnvalue == -1:
                    print(number," cannot be found on array.")
                    print(arr)
                else:
                    print(number," found on array.")
                    print("Index of the number: ", returnvalue)
                    print("Process step counter: ", proc)
            if option == "2":
                print("Binary")
                number = int(input("Please enter a number for search: "))
                start = timer()
                binarySearch(arr, 0, len(arr)-1, number,0)
                end = timer()
                returnvalue = binarySearch(arr, 0, len(arr)-1, number,0)
                print("Binary search searching time : ", str(end-start))
                if returnvalue == -1:
                    print(number," cannot be found on array.")
                    print(arr)
                else:
                    print(number," found on array.")
                    print("Index of the number: ", returnvalue)
                    print("Process step counter: ", proc)
            if option == "3":
                print("All")
                number = int(input("Please enter a number for search: "))
                start = timer()
                linearsearch(arr,len(arr),number,0)
                end = timer()
                returnvalue,proc = linearsearch(arr,len(arr),number,0)
                print("Linear search searching time : ", str(end-start))
                if returnvalue == -1:
                    print(number," cannot be found on array.")
                    print(arr)
                else:
                    print(number," found on array.")
                    print("Index of the number: ", returnvalue)
                    print("Process step counter: ", proc)
                start = timer()
                binarySearch(arr, 0, len(arr)-1, number,0)
                end = timer()
                returnvalue,proc = binarySearch(arr, 0, len(arr)-1, number,0)
                print("Binary search searching time : ", str(end-start))
                if returnvalue == -1:
                    print(number," cannot be found on array.")
                    print(arr)
                else:
                    print(number," found on array.")
                    print("Index of the number: ", returnvalue)
                    print("Process step counter: ", proc)
            elif option == "q":
                return option
        if option == "2":
            print("Sorting")
            print("""1. Insertion
            2. Merge
            3. Heap
            4. Quick
            5. Counting
            6. Bucket
            7. Radix
            8. All
            9. Chooose what you want""")
            option = input("Select an option: ")
            if (int(option) > 9 or int(option) < 1):
                print("Wrong option")
            elif option == "1":
                print("Insertion")
                start = timer()
                insertion_sort(arr)
                end = timer()
                print("Insertion sort time: ", str(end-start))
            elif option == "2":
                print("Merge")
                start = timer()
                mergeSort(arr)
                end = timer()
                print("Merge sort time: ", str(end-start))
            elif option == "3":
                print("Heap")
                start = timer()
                heapSort(arr)
                end = timer()
                print("Heap sort time: ", str(end-start))
            elif option == "4":
                print("Quick")
                start = timer()
                quickSort(arr,0,len(arr)-1)
                end = timer()
                print("Quick sort time: ", str(end-start))
            elif option == "5":
                print("Counting")
                max_array = max(arr)
                start = timer()
                counting_sort(arr,max_array)
                end = timer()
                print("Counting sort time: ", str(end-start))
            elif option == "6":
                print("Bucket")
                start = timer()
                bucket_sort(arr)
                end = timer()
                print("Bucket sort time: ", str(end-start))
            elif option == "7":
                print("Radix")
                start = timer()
                radixSort(arr)
                end = timer()
                print("Radix sort time: ", str(end-start))
            elif option == "8":
                print("All")
                allarrays = {}
                for i in range(0,7):
                    allarrays[i] = arr.copy()
                start = timer()
                insertion_sort(allarrays[0])
                end = timer()
                print("Insertion sort time: ", str(end-start))
                start = timer()
                mergeSort(allarrays[1])
                end = timer()
                print("Merge sort time: ", str(end-start))
                start = timer()
                heapSort(allarrays[2])
                end = timer()
                print("Heap sort time: ", str(end-start))
                start = timer()
                quickSort(allarrays[3],0,len(allarrays[3])-1)
                end = timer()
                print("Quick sort time: ", str(end-start))
                max_array = max(allarrays[4])
                start = timer()
                counting_sort(allarrays[4],max_array)
                end = timer()
                print("Counting sort time: ", str(end-start))
                start = timer()
                bucket_sort(allarrays[5])
                end = timer()
                print("Bucket sort time: ", str(end-start))
                start = timer()
                radixSort(allarrays[6])
                end = timer()
                print("Radix sort time: ", str(end-start))
                return option
            elif option == "9":
                allarrays = {}
                print("Chooose what you want")    
                options = input("Sorting algorithms (ex:(1 2 5 7)): ")
                print(options.split(" "))
                listedoptions = options.split(" ")
                for i in listedoptions:
                    if ( int(i) >= 1 and int(i) <= 9 ):
                        optionFlag = True
                    else:
                        optionFlag = False
                if(optionFlag):
                    print("Options are true.")
                    for i in listedoptions:
                        allarrays[i] = arr.copy()
                    print(allarrays)
                    for i in listedoptions:
                        if i == "1":
                            start = timer()
                            insertion_sort(arr)
                            end = timer()
                            print("Insertion sort time: ", str(end-start))
                        if i == "2":
                            start = timer()
                            mergeSort(arr)
                            end = timer()
                            print("Merge sort time: ", str(end-start))
                        if i == "3":
                            print("Heap")
                            start = timer()
                            heapSort(arr)
                            end = timer()
                            print("Heap sort time: ", str(end-start))
                        if i == "4":
                            print("Quick")
                            start = timer()
                            quickSort(arr,0,len(arr)-1)
                            end = timer()
                            print("Quick sort time: ", str(end-start))
                        if i == "5":
                            max_array = max(arr)
                            start = timer()
                            counting_sort(arr,max_array)
                            end = timer()
                            print("Counting sort time: ", str(end-start))
                        if i == "6":
                            start = timer()
                            bucket_sort(arr)
                            end = timer()
                            print("Bucket sort time: ", str(end-start))
                        if i == "7":
                            start = timer()
                            radixSort(arr)
                            end = timer()
                            print("Radix sort time: ", str(end-start))
        elif option == "q":
            return option
    else:
        print("Please enter a valid input.")

while True:
    option = menu()
    if (option == "q"):
        break
