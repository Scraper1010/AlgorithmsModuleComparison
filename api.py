from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
import json, os
from Algorithms import Algorithms

dir = os.path.dirname(__file__) 
with open(os.path.join(dir, 'SP_S.json'), 'r') as f:
    student_profiles = json.load(f)
student_ids = [profile['id'] for profile in student_profiles]




app=FastAPI()
@app.get("/")
def getitem():
    return "start"
@app.get("/get-item/{ID}")
def getitem(ID:int):
    algo = Algorithms(lst=student_ids,target=ID)
    x=algo.BinarySearch()
    
    return student_profiles[x]

    
    
if "__main__"== "__name__":
    import uvicorn

    uvicorn.run(app,host="0.0.0.0",port=8000)
    #uvicorn api:app --reload 
