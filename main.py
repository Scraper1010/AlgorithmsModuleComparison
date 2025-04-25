from Algorithms import Algorithms
import random

num = 100  # Reduced from 10000 for testing
lst = [i for i in range((num)+1)]
rlst = [random.randint(1, (num)+1) for _ in range((num)+1)]



# print(Algorithms(lst=lst, value=200, debug=True).LinearSearch())
public_methods = [method for method in dir(Algorithms) if callable(getattr(Algorithms, method)) and not method.startswith("_")]
print(public_methods)