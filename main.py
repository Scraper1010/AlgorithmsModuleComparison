import time, threading, queue, sys, os, random
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

    def LinearSearch(self): #easy as fuck  
        pass

    def ExponentialSearch(self): #normal
        pass

    def BinarySearch(self): #easy as fuck
        low = 0
        high = len(self.lst) -1
        steps = 0
        while low <= high :
                steps += 1
                mid =(low + high) // 2
                if self.lst[mid] == self.value:
                    return self.lst[mid] , mid,-1,'Binary search' , steps 
                elif self.lst[mid] < self.value:
                    low = mid +1
                else:
                    high = mid -1
        return f'value : {self.value} not found in list'
    
    def JumpSearch(self): #normal
        
        import math
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


    def InterpolationSearch(self): #hard
        pass
    
    def BubbleSort(self): #hard #not for larg data set
        #start the timer
        for i in range(len(self.lst)-1):
            self.iteration += 1
            for j in range (len(self.lst)-i-1): # i here just to shrink the index cuz the every iteratoin will make the last element of index it the largest (just for efficiency)
                self.iteration += 1
                if self.lst[j] > self.lst[j+1]:
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]

        #stop the timer
        return self.lst , self.iteration #elapsed_time

    def InsertoinSort(self): #hard
        pass

    def QuicKSort(self): #more than hard
        pass

    def SelectionSort(self): #easy
        pass

    #timer method
    
num = 10000


lst = [i for i in range((num)+1)]
# rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]


# print("lst is created")

# lst , iteration = Algorithms(rlst).BubbleSort()
# print(f"lst : {lst}\niterations : {iteration}")

print("done")
lst=[1,2,3,4,5,6,7,8,9,10]

# value, index, elapsed_time, AlgorithmName, steps = Algorithms(lst, 11).JumpSearch()  # Updated method call and variable name
# print(f"found value {value} in index {index} with elapsed time {elapsed_time} ms with {AlgorithmName} with {steps} steps")
print(Algorithms(lst, 11).JumpSearch())
del lst
print("lst has been deleted")






