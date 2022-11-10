import os

taskNumber = input("Enter task number to run: ")
print(f"Running task #{taskNumber}\n")
os.system(f"python3 tasks/{taskNumber}/main.py")