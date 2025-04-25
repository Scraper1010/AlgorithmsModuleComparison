import time, threading, queue, sys, os, random, math
class Algorithms:
    
    def __init__(self, lst=None, value=None, debug=False):

        self.__lst = lst.copy() if lst is not None else None
        self.__value = value
        self.__steps = 0
        self.__iteration = 0
        self.__debug = debug
        
        if self.__debug == True:
            self.__temp = None
            self.__timer_event = threading.Event()
            self.__timer_event.set()
            self.__elapsed_time = queue.Queue()
            self.__timer_thread = threading.Thread(target=self.__run, daemon=True)

    

    def LinearSearch(self) ->int:
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

    def ExponentialSearch(self):
        pass

    def BinarySearch(self):

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


    def InterpolationSearch(self): 
        if self.__debug == True:
            self.__StartTimer()
        low = 0
        high = len(self.__lst) - 1
        while low <= high and self.__value >= self.__lst[low] and self.__value <= self.__lst[high]:
            self.__steps += 1
            pos = low + ((high - low) * (self.__value - self.__lst[low])) // (self.__lst[high] - self.__lst[low])
            if pos >= len(self.__lst):
                break
            if self.__lst[pos] == self.__value:
                if self.__debug == True:
                    self.__StopTimer()
                    return self.__lst[pos], pos, self.__elapsed_time.get(), self.InterpolationSearch.__name__, self.__steps
                else:
                    return pos
            elif self.__lst[pos] < self.__value:
                low = pos + 1
            else:
                high = pos - 1
        raise _Error(f"value:{self.__value} not found in list")
    
    def BubbleSort(self):
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

    def InsertoinSort(self):
        pass

    def QuickSort(self):
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
        self.__timer_thread.start()

    def __StopTimer(self):
        self.__timer_event.clear()
        self.__timer_thread.join()

    def __run(self):
        self.__start_time = time.time()
    
        while self.__timer_event.is_set():
            time.sleep((0.01)/10**10)
        elapsed_ms = float(f"{(time.time() - self.__start_time) * 1000:.3f}")
        self.__elapsed_time.put(elapsed_ms)



class _Error(Exception):
        def __init__(self, message):
            self.message = message
            super().__init__(self.message)



if __name__ == "__main__":
    num = 10000
    lst = [i for i in range((num)+1)]
    rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]
    print(Algorithms(lst=rlst, value=100).QuickSort())
    del rlst
