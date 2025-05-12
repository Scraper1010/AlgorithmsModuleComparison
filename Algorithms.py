"""
Algorithms Module for Search and Sort Operations

This module provides a comprehensive implementation of various search and sorting algorithms
with performance monitoring capabilities. It includes both basic and advanced algorithms
for searching and sorting operations.

Search Algorithms:
    - Linear Search: O(n) time complexity, searches sequentially through the list
    - Binary Search: O(log n) time complexity, requires sorted input
    - Interpolation Search: O(log log n) average case, requires sorted input
    - Jump Search: O(√n) time complexity, requires sorted input

Sorting Algorithms:
    - Bubble Sort: O(n²) time complexity, simple but inefficient
    - Insertion Sort: O(n²) time complexity, efficient for small lists
    - Quick Sort: O(n log n) average case, uses median-of-three pivot selection
    - Selection Sort: O(n²) time complexity, performs well on small lists

Features:
    - Performance monitoring with step counting and timing
    - Debug mode for detailed algorithm analysis
    - Thread-safe timing mechanism
    - Error handling for edge cases

Usage:
    >>> from Algorithms import Algorithms
    >>> # Initialize with a list and search value
    >>> algo = Algorithms(lst=[1, 2, 3, 4, 5], value=3)
    >>> # Perform search operations
    >>> result = algo.BinarySearch()
    >>> # Perform sort operations
    >>> sorted_list = algo.QuickSort()

Note:
    - Search algorithms return the index of the found value or raise an error if not found
    - Sort algorithms return the first 5 and last 5 elements in non-debug mode
    - Debug mode provides detailed performance metrics including execution time and steps
"""

import time, threading, queue, sys, os, random, math
class Algorithms:
    """
    A class implementing various search and sorting algorithms with performance monitoring.
    
    Attributes:
        __lst (list): The input list to be searched or sorted
        __value: The value to search for in search algorithms
        __steps (int): Counter for algorithm steps
        __iteration (int): Counter for sorting iterations
        __debug (bool): Flag to enable/disable debug mode
    """
    
    def __init__(self, lst=None, target=None, debug=False):
        """
        Initialize the Algorithms class.

        Args:
            lst (list): The input list to be searched or sorted
            value: The value to search for in search algorithms
            debug (bool, optional): Enable debug mode for performance monitoring. Defaults to False.
        """
        self.__lst = lst
        self.__value = target
        self.__steps = 0
        self.__iteration = 0
        self.__debug = debug
        if self.__debug == True:
            self.__timer_event = threading.Event()
            self.__timer_event.set()
            self.__elapsed_time = queue.Queue()
            self.__timer_thread = threading.Thread(target=self.__run, daemon=True)
            

    def LinearSearch(self):
        """
        Perform a linear search on the list.

        Returns:
            If debug mode is False:
                int: Index of the found value
            If debug mode is True:
                tuple: (value, index, elapsed_time_ms, algorithm_name, steps)

        Raises:
            _Error: If the value is not found in the list
        """
        if self.__debug == True:
            self.__StartTimer()

        for i in range(len(self.__lst)):
            self.__steps += 1
            if self.__lst[i] == self.__value:
                if self.__debug == True:
                    self.__StopTimer()
                    return self.__lst[i], i, self.__elapsed_time.get(), self.LinearSearch.__name__, self.__steps
                else:
                    return i
        raise _Error(f"value:{self.__value} not found in list")


    def InterpolationSearch(self):
        """
        Perform an interpolation search on a sorted list.
        This algorithm works best on uniformly distributed sorted arrays.

        Returns:
            If debug mode is False:
                int: Index of the found value
            If debug mode is True:
                tuple: (value, index, elapsed_time_ms, algorithm_name, steps)

        Raises:
            _Error: If the value is not found in the list or if the list is empty
        """
        if self.__debug == True:
            self.__StartTimer()
        if len(self.__lst) == 0:
            raise _Error(f"value:{self.__value} not found in list")
        
        low = 0
        high = len(self.__lst) - 1
        
        while low <= high and self.__value >= self.__lst[low] and self.__value <= self.__lst[high]:
            self.__steps += 1
            pos = low + ((high - low) // (self.__lst[high] - self.__lst[low])) * (self.__value - self.__lst[low])
            
            if self.__lst[pos] == self.__value:
                if self.__debug == True:
                    self.__StopTimer()
                    return self.__lst[pos], pos, self.__elapsed_time.get(), self.InterpolationSearch.__name__, self.__steps
                else:
                    return pos
            
            if self.__lst[pos] > self.__value:
                high = pos - 1
            
            else:
                low = pos + 1
        
        raise _Error(f"value:{self.__value} not found in list")

    def BinarySearch(self):
        """
        Perform a binary search on a sorted list.
        This algorithm requires the input list to be sorted.

        Returns:
            If debug mode is False:
                int: Index of the found value
            If debug mode is True:
                tuple: (value, index, elapsed_time_ms, algorithm_name, steps)

        Raises:
            _Error: If the value is not found in the list
        """
        if self.__debug == True:
            self.__StartTimer()
        low = 0
        high = len(self.__lst) -1
        while low <= high:
            self.__steps += 1
            mid = (low + high) // 2
            if self.__lst[mid] == self.__value:
                if self.__debug == True:
                    self.__StopTimer()
                    return self.__lst[mid], mid, self.__elapsed_time.get(), self.BinarySearch.__name__, self.__steps
                else:
                    return mid
            elif self.__lst[mid] < self.__value:
                low = mid + 1
            else:
                high = mid - 1
        raise _Error(f"value:{self.__value} not found in list")
    
    def JumpSearch(self):
        """
        Perform a jump search on a sorted list.
        This algorithm works by jumping ahead by fixed steps and then performing linear search.

        Returns:
            If debug mode is False:
                int: Index of the found value
            If debug mode is True:
                tuple: (value, index, elapsed_time_ms, algorithm_name, steps)

        Raises:
            _Error: If the value is not found in the list
        """
        if self.__debug == True:
            self.__StartTimer()
        n = len(self.__lst)
        step = int(math.sqrt(n))
        prev = 0

        while self.__lst[min(step, n) - 1] < self.__value:
            self.__steps += 1
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                break

        for i in range(prev, min(step, n)):
            self.__steps += 1
            if self.__lst[i] == self.__value:
                if self.__debug == True:
                    self.__StopTimer()
                    return self.__lst[i], i, self.__elapsed_time.get(), self.JumpSearch.__name__, self.__steps
                else:
                    return i
        raise _Error(f"value:{self.__value} not found in list")        



    def BubbleSort(self):
        """
        Sort the list using bubble sort algorithm.
        This is a simple but inefficient sorting algorithm.

        Returns:
            If debug mode is False:
                list: The complete sorted list
            If debug mode is True:
                tuple: (sorted_list, iterations, algorithm_name, elapsed_time_ms)
        """
        if self.__debug == True:
            self.__StartTimer()
        result = self.__lst.copy()
        for i in range(len(result)-1):
            for j in range(len(result)-i-1): 
                
                self.__iteration += 1
                if result[j] > result[j+1]:
                    result[j], result[j+1] = result[j+1], result[j]
        if self.__debug == True:
            self.__StopTimer()
            return result, self.__iteration, self.BubbleSort.__name__, self.__elapsed_time.get()
        return result

    def InsertionSort(self):
        """
        Sort the list using insertion sort algorithm.
        This algorithm is efficient for small lists and nearly sorted lists.

        Returns:
            If debug mode is False:
                list: The complete sorted list
            If debug mode is True:
                tuple: (sorted_list, elapsed_time_ms, algorithm_name, iterations)
        """
        if self.__debug:
            self.__StartTimer()

        for i in range(1, len(self.__lst)):
            self.__iteration += 1
            key = self.__lst[i]
            j = i - 1

            while j >= 0 and self.__lst[j] > key:
                self.__iteration += 1
                self.__lst[j + 1] = self.__lst[j]  
                j -= 1
            self.__lst[j + 1] = key

        if self.__debug:
            self.__StopTimer()
            return self.__lst, self.__elapsed_time.get(), self.InsertionSort.__name__, self.__iteration
        return self.__lst

    def QuickSort(self):
        """
        Sort the list using quick sort algorithm with median-of-three pivot selection.
        This implementation includes optimization for small subarrays using insertion sort.

        Returns:
            If debug mode is False:
                list: The complete sorted list
            If debug mode is True:
                tuple: (sorted_list, steps, algorithm_name, elapsed_time_ms)

        Note:
            Temporarily increases recursion limit to handle large lists
        """
        steps = 0
        if self.__debug == True:
            self.__StartTimer()
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
            nonlocal steps
            pivot_index = get_pivot(arr, low, high)
            pivot_value = arr[pivot_index]
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            store_index = low
            for i in range(low, high):
                steps += 1
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
                        nonlocal steps
                        steps += 1
                        key = arr[i]
                        j = i - 1
                        while j >= low and arr[j] > key:
                            arr[j + 1] = arr[j]
                            j -= 1
                        arr[j + 1] = key
                    return
                
                pivot_index = partition(arr, low, high)
                
                if pivot_index - low < high - pivot_index:
                    quick_sort_helper(arr, low, pivot_index - 1)
                    low = pivot_index + 1 
                else:
                    quick_sort_helper(arr, pivot_index + 1, high)
                    high = pivot_index - 1 
        old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(100000)  # Increase recursion limit as a safety measure
        try:
            result = self.__lst.copy()
            quick_sort_helper(result, 0, len(result) - 1)
            if self.__debug == True:
                self.__StopTimer()
                return result, steps, self.QuickSort.__name__, self.__elapsed_time.get()
            return result
        finally:
            sys.setrecursionlimit(old_limit)

    def SelectionSort(self):
        """
        Sort the list using selection sort algorithm.
        This algorithm performs well on small lists and has minimal memory usage.

        Returns:
            If debug mode is False:
                tuple: (first_5_elements, last_5_elements)
            If debug mode is True:
                tuple: (sorted_list, iterations, algorithm_name, elapsed_time_ms)
        """
        if self.__debug == True:
            self.__StartTimer()
        result = self.__lst.copy()
        for i in range(len(result)):
            min_index = i
            for j in range(i + 1, len(result)):
                self.__iteration += 1
                if result[j] < result[min_index]:
                    min_index = j
            result[i], result[min_index] = result[min_index], result[i]
        if self.__debug == True:
            self.__StopTimer()
            return result, self.__iteration, self.SelectionSort.__name__,self.__elapsed_time.get()
        return result


    def __StartTimer(self):
        """
        Start the performance timer in debug mode.
        Initializes and starts the timer thread.
        """
        self.__timer_thread.start()

    def __StopTimer(self):
        """
        Stop the performance timer in debug mode.
        Clears the timer event and waits for the timer thread to complete.
        """
        self.__timer_event.clear()
        self.__timer_thread.join()

    def __run(self):
        """
        Internal method for timer thread.
        Measures elapsed time in milliseconds.
        """
        self.__start_time = time.time()
    
        while self.__timer_event.is_set():
            time.sleep((0.01)/10**10)
        elapsed_ms = float(f"{(time.time() - self.__start_time) * 1000:.3f}")
        self.__elapsed_time.put(elapsed_ms)




class _Error(Exception):
    """
    Custom exception class for algorithm-specific errors.
    
    Attributes:
        message (str): Error message describing the failure
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)




