import time, threading, queue, sys, os, random, math
from PyQt5.QtWidgets import (QLabel, QLayout, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import Qt

SD = os.path.join(os.path.dirname(__file__))
def clear():os.system('cls') if os.name == 'nt' else os.system('clear')
new_SD = os.path.join(os.path.dirname(SD), 'dump')






class Algorithms:
    """A class implementing various searching and sorting algorithms with performance tracking."""
    
    def __init__(self, lst=None, value=None):
        """
        Initialize the Algorithms class.
        
        Args:
            lst (list, optional): Input list for algorithms. Defaults to None.
            value (any, optional): Search value for search algorithms. Defaults to None.
        """
        # Core attributes
        self.lst = lst.copy() if lst is not None else None  # Create a copy to prevent modifying original
        self.value = value
        self.steps = 0
        self.iteration = 0
        
        # Performance tracking
        self._setup_timer()
    
    def _setup_timer(self):
        """Setup timing mechanism for performance measurement."""
        self.timer_event = threading.Event()
        self.timer_event.set()
        self.elapsed_time = queue.Queue()
        self.timer_thread = threading.Thread(target=self.__run, daemon=True)  # Make thread daemon



    def LinearSearch(self): #easy as fuck  
        steps = 0
        self.StartTimer()
        for i in range(len(self.lst)):
            steps += 1
            # Check if the current element is the target
            if self.lst[i] == self.value:
                self.StopTimer()
                return self.lst[i] , i, self.elapsed_time.get(), 'LinearSearch', steps
            
        return -1  # Return -1 if the target is not found

    def ExponentialSearch(self):
        pass

    def BinarySearch(self):
        self.StartTimer()
        low = 0
        high = len(self.lst) -1
        steps = 0
        while low <= high :
                steps += 1
                mid =(low + high) // 2
                if self.lst[mid] == self.value:
                    self.StopTimer()
                    return self.lst[mid] , mid, self.elapsed_time.get(), 'Binary search', steps 
                elif self.lst[mid] < self.value:
                    low = mid +1
                else:
                    high = mid -1
        
        return f'value : {self.value} not found in list'
    
    def JumpSearch(self):
    
        n = len(self.lst)
        step = int(math.sqrt(n))
        prev = 0

        while self.lst[min(step, n) - 1] < self.value:
            self.steps += 1
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                break

        for i in range(prev, min(step, n)):
                self.steps += 1
                if self.lst[i] == self.value:
                    return self.value, i, -1, "JumpSearch", self.steps 
        return f"value : {self.value} not found"         


    def InterpolationSearch(self): 
        pass
    
    def BubbleSort(self):
        #start the timer
        for i in range(len(self.lst)-1):
            self.iteration += 1
            for j in range (len(self.lst)-i-1): # i here just to shrink the index cuz the every iteratoin will make the last element of index it the largest (just for efficiency)
                self.iteration += 1
                if self.lst[j] > self.lst[j+1]:
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]

        #stop the timer
        return self.lst , self.iteration

    def InsertoinSort(self):
        pass

    def QuickSort(self):
        self.iteration += 1
        self.StartTimer()
        
        def get_pivot(arr, low, high):
            mid = (low + high) // 2
            pivot = high
            if arr[low] < arr[mid]:
                if arr[mid] < arr[high]:
                    pivot = mid
            elif arr[low] < arr[high]:
                pivot = low
            return pivot

        def partition(arr, low, high):
            pivot_index = get_pivot(arr, low, high)
            pivot_value = arr[pivot_index]
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            
            store_index = low
            for i in range(low, high):
                if arr[i] <= pivot_value:
                    arr[store_index], arr[i] = arr[i], arr[store_index]
                    store_index += 1
            arr[store_index], arr[high] = arr[high], arr[store_index]
            return store_index

        def quick_sort_helper(arr, low, high):
            while low < high:
                if high - low < 10:  # Use insertion sort for small arrays
                    # Insertion sort
                    for i in range(low + 1, high + 1):
                        key = arr[i]
                        j = i - 1
                        while j >= low and arr[j] > key:
                            arr[j + 1] = arr[j]
                            j -= 1
                        arr[j + 1] = key
                    return 1
                
                pivot_index = partition(arr, low, high)
                
                # Recursively sort the smaller partition
                if pivot_index - low < high - pivot_index:
                    quick_sort_helper(arr, low, pivot_index - 1)
                    low = pivot_index + 1  # Tail recursion optimization
                else:
                    quick_sort_helper(arr, pivot_index + 1, high)
                    high = pivot_index - 1  # Tail recursion optimization
            return 1

        # Increase recursion limit as a safety measure
        old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(100000)
        
        try:
            # Create a copy of the list to sort
            arr = self.lst.copy()
            total_iter = quick_sort_helper(arr, 0, len(arr) - 1)
            self.iteration += total_iter
            
            # Stop the timer and return results
            self.StopTimer()
            return arr, self.iteration, self.elapsed_time.get()
        finally:
            # Restore the original recursion limit
            sys.setrecursionlimit(old_limit)

    def SelectionSort(self):
        for i in range(len(self.lst)):
            min_index = i
            for j in range(i + 1, len(self.lst)):
                self.iteration += 1
                if self.lst[j] < self.lst[min_index]:
                    min_index = j
            self.lst[i], self.lst[min_index] = self.lst[min_index], self.lst[i]
        return self.lst, self.iteration


    def StartTimer(self):
        self.timer_thread.start()

    def StopTimer(self):
        self.timer_event.clear()
        self.timer_thread.join()

    def __run(self):
        self.start_time = time.time()
    
        while self.timer_event.is_set():
            time.sleep((0.01)/10**10)
        elapsed_ms = float(f"{(time.time() - self.start_time) * 1000:.3f}")
        self.elapsed_time.put(elapsed_ms)






num = 100  # Reduced from 10000 for testing
lst = [i for i in range((num)+1)]
rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]






#QSM output:
sorted_list, iterations,elapsed_time = Algorithms(lst).QuickSort()
print("QSM  list:", sorted_list)
print("QSM Iterations:", iterations)
print(f"Time taken in QSM: {elapsed_time} ms")




del lst





