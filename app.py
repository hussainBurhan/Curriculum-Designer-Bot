import streamlit as st
import json
import random


def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def get_activity(data, institute_type, curriculum, grade, subject, num_of_students):
    total_cost = 0
    total_duration = 0

    for entry in data.get('data', []):
        entry_type = entry.get('type')
        entry_curriculum = entry.get('curriculum')
        entry_grade = entry.get('grade')
        entry_subject = entry.get('subject')

        if entry_type == institute_type and entry_curriculum == curriculum and entry_grade == grade and entry_subject == subject:
            st.subheader(f'Topic {entry.get("topics", "")}')

            activities = entry.get('activities', [])
            if activities:
                activity = random.choice(activities)
                st.write(f"Activity Name: {activity.get('activity_name', '')}")
                st.write(f"Activity Cost: {activity['activity_cost'].get(num_of_students, 0)}")
                st.write(f"Activity Duration: {activity.get('activity_duration', 0)} session")
                st.write(f"Manual Link: {activity.get('activity_link', '')}")
                st.write("\n")
                total_cost += activity['activity_cost'].get(num_of_students, 0)
                total_duration += activity.get('activity_duration', 0)

    return total_cost, total_duration


def main():
    st.title("STEM Curriculum Designer App")

    file_path = 'Data.json'
    data = load_data(file_path)

    institute_type = st.sidebar.selectbox("Select Institute Type:", ['gov', 'pvt'])
    curriculum = st.sidebar.selectbox("Select Curriculum:", ['SNC', 'Federal'])
    subject = st.sidebar.selectbox("Select Subject:", ['Maths', 'Phy'])

    # Add sliders for grades and number of students
    grade = st.sidebar.slider("Select Grade:", min_value=5, max_value=9, step=1, value=5)
    num_of_students = st.sidebar.slider("Number of Students:", options=[10, 20, 30, 40], value=10)

    submitted = st.button("Submit")

    if submitted:
        st.subheader(f'Grade {grade}\n')

        total_cost, total_duration = get_activity(data, institute_type, curriculum, grade, subject, num_of_students)

        st.write(f"Total Cost: {total_cost}")
        st.write(f"Total Duration: {total_duration}")


if __name__ == "__main__":
    main()
