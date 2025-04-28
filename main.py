from Algorithms import Algorithms
import random

num = 100000  # Reduced from 10000 for testing
# lst = [i for i in range((num)+1)]
rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]
# NOlst = [i for i in range(0, num, 2)]

Mlst = [10, 12, 23, 35, 40, 45, 50, 70, 90, 100]

# print(Algorithms(lst=lst, value=200, debug=True).BinarySearch())


# print(Algorithms(lst=lst, value=200, debug=True).LinearSearch())
# public_methods = [method for method in dir(Algorithms) if callable(getattr(Algorithms, method)) and not method.startswith("_")]
# print(public_methods)
print("algo started")
print(Algorithms(lst=rlst, value=198762 , debug=True).InsertionSort())
