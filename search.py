from Algorithms import Algorithms
import json, os

dir = os.path.dirname(__file__) 
with open(os.path.join(dir, 'SP_S.json'), 'r') as f:
    student_profiles = json.load(f)
student_ids = [profile['id'] for profile in student_profiles]

algo = Algorithms(lst=student_ids, target=224110775)

try:
    index = algo.BinarySearch()
    student_profile = student_profiles[index]
    print(f"Found student profile:")
    print(json.dumps(student_profile, indent=2))
except Exception as e:
    print(f"Error : {e}")




