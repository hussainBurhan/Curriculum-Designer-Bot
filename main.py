import numpy as np
import pandas as pd
import json
import random

with open('Data.json', 'r') as f:
    data = json.load(f)

institute_type = input("Enter gov or pvt: ")
curriculum = input("Enter curriculum SNC or Federal: ")
grade = int(input("Enter Grade 9 or 5: "))
subject = input("Enter subject Maths or Phy: ")
num_of_students = input("Number of Students")

print(f'Grade {grade}')
print("\n")

total_cost = 0
total_duration = 0
for data in data['data']:
    if (data['type'] == institute_type) and (data['curriculum'] == curriculum) and (data['grade'] == grade) and (
            data['subject'] == subject):
        print(f'Topic {data["topics"]}')
        activity = data['activities'][random.randint(0, 2)]
        print(f"Activity Name: {activity['activity_name']}")
        print(f"Activity Cost: {activity['activity_cost'][num_of_students]}")
        print(f"Activity Duration: {activity['activity_duration']} session")
        print(f"Manual Link: {activity['activity_link']}")
        print("\n")
        total_cost += activity['activity_cost'][num_of_students]
        total_duration += activity['activity_duration']

print(total_cost)
print(total_duration)