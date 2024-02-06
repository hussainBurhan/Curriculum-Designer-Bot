import streamlit as st
import json
import random

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_activity(data, institute_type, curriculum, grade, subject, num_of_students):
    total_cost = 0
    total_duration = 0

    for entry in data['data']:
        if (entry['type'] == institute_type) and (entry['curriculum'] == curriculum) and (entry['grade'] == grade) and (entry['subject'] == subject):
            st.subheader(f'Topic {entry["topics"]}')
            activity = random.choice(entry['activities'])
            st.write(f"Activity Name: {activity['activity_name']}")
            st.write(f"Activity Cost: {activity['activity_cost'][num_of_students]}")
            st.write(f"Activity Duration: {activity['activity_duration']} session")
            st.write(f"Manual Link: {activity['activity_link']}")
            st.write("\n")
            total_cost += activity['activity_cost'][num_of_students]
            total_duration += activity['activity_duration']

    return total_cost, total_duration

def main():
    st.title("STEM Curriculum Designer App")

    file_path = 'Data.json'
    data = load_data(file_path)

    institute_type = st.sidebar.selectbox("Select Institute Type:", ['gov', 'pvt'])
    curriculum = st.sidebar.selectbox("Select Curriculum:", ['SNC', 'Federal'])
    grade = st.sidebar.selectbox("Select Grade:", [5, 9])
    subject = st.sidebar.selectbox("Select Subject:", ['Maths', 'Phy'])
    num_of_students = st.sidebar.number_input("Number of Students:", min_value=1, value=10)

    submitted = st.button("Submit")

    if submitted:
        st.subheader(f'Grade {grade}\n')

        total_cost, total_duration = get_activity(data, institute_type, curriculum, grade, subject, num_of_students)

        st.write(f"Total Cost: {total_cost}")
        st.write(f"Total Duration: {total_duration}")

if __name__ == "__main__":
    main()

