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

    def JumpSearch(self): #normal
        pass
    
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
rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]


print("lst is created")

lst , iteration = Algorithms(rlst).BubbleSort()
print(f"lst : {lst}\niterations : {iteration}")

print("done")

# value, index, elapsed_time, AlgorithmName, steps = Algorithms(rlst, 1000000).BubbleSort()  # Updated method call and variable name
# print(f"found value {value} in index {index} with elapsed time {elapsed_time} ms with {AlgorithmName} with {steps} steps")

del lst
print("lst has been deleted")






