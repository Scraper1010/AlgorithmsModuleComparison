from Algorithms import Algorithms
import json, os

dir = os.path.dirname(__file__) 
with open(os.path.join(dir, 'SP_NS.json'), 'r') as f:
    student_profiles = json.load(f)

student_ids = [profile['id'] for profile in student_profiles]

algo = Algorithms(lst=student_ids, target=None)

sorted_ids = algo.QuickSort()

sorted_profiles = []
for id in sorted_ids:
    profile = next((p for p in student_profiles if p['id'] == id), None)
    if profile:
        sorted_profiles.append(profile)

with open(os.path.join(dir, 'SP_S.json'), 'w') as f:
    json.dump(sorted_profiles, f, indent=4)

print(f"Student profiles have been sorted and saved to '{os.path.join(dir, 'SP_S.json')}'")


