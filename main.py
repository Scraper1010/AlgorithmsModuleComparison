import time, threading, queue, sys, os, random, math
from PyQt5.QtWidgets import (QLabel, QLayout, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import Qt

SD = os.path.join(os.path.dirname(__file__))
def clear():os.system('cls') if os.name == 'nt' else os.system('clear')
new_SD = os.path.join(os.path.dirname(SD), 'dump')






class Algorithms:
    def __init__(self, lst=None, value=None):
        self.lst = lst
        self.value = value
        self.steps = 0
        self.iteration = 0
        self.temp = None

        self.timer_event = threading.Event()
        self.timer_event.set()
        self.elapsed_time = queue.Queue()
        self.timer_thread = threading.Thread(target=self.__run)




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
     if len(self.lst) <= 1:
        self.StopTimer()
        return self.lst.copy(), 1  # Return both list and iteration count
    
     pivot = self.lst[-1]
     left = [x for x in self.lst[:-1] if x <= pivot]
     right = [x for x in self.lst[:-1] if x > pivot]
    
     left_sorted, left_iter = Algorithms(left).QuickSort()
     right_sorted, right_iter = Algorithms(right).QuickSort()
    
     total_iter = self.iteration + left_iter + right_iter
     if len(lst) == len(self.lst):  
        self.StopTimer()
        return left_sorted + [pivot] + right_sorted, total_iter, self.elapsed_time.get()
     else:
        return left_sorted + [pivot] + right_sorted, total_iter

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






num =10000
lst = [i for i in range((num)+1)]
rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]



print(Algorithms(rlst).SelectionSort())


#QSM output:
sorted_list, iterations,elapsed_time = Algorithms(lst).QuickSort()
print("QSM  list:", sorted_list)
print("QSM Iterations:", iterations)
print(f"Time taken in QSM: {elapsed_time} ms")




del lst





