import time, threading, queue, sys, os, random


SD = os.path.join(os.path.dirname(__file__))
def clear():os.system('cls') if os.name == 'nt' else os.system('clear')
new_SD = os.path.join(os.path.dirname(SD), 'dump')
print(new_SD)





class Algorithms:
    def __init__(self, lst=None, value=None):
        pass

    def LinearSearch(self): #easy as fuck  
        pass

    def BinarySearch(self): #easy as fuck
        pass

    def ExponentialSearch(self): #normal
        pass

    def JumpSearch(self): #normal
        pass
    
    def InterpolationSearch(self): #hard
        pass
    
    def BubbleSort(self): #hard
        pass

    def InsertoinSort(self): #hard
        pass

    def QuicKSort(self): #more than hard
        pass

    def SelectionSort(self): #easy
        pass

    #timer method
    



lst = [i for i in range((1000000)+1)]

print("lst is created")

value, index, elapsed_time, AlgorithmName, steps = Algorithms(lst, 1000000).BinarySearch()  # Updated method call and variable name
print(f"found value {value} in index {index} with elapsed time {elapsed_time} ms with {AlgorithmName} with {steps} steps")

del lst
print("lst has been deleted")
