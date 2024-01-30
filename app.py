import streamlit as slt


slt.title("Curriculum Designer Bot")
with slt.form("my_form"):
    slt.write("What type of institute are you?")
    gov = slt.checkbox("Government")
    pvt = slt.checkbox("Private")

    slt.write("Which curriculum you want to follow?")
    curriculum1 = slt.checkbox("C1")
    curriculum2 = slt.checkbox("C2")
    curriculum3 = slt.checkbox("C3")

    slt.write("Which grade do you want to target?")
    grade = slt.slider("Grade", 3, 9)

    slt.write("Which Subjects do you want to cater?")
    subject1 = slt.checkbox("Sub 1")
    subject2 = slt.checkbox("Sub 2")
    subject3 = slt.checkbox("Sub 3")

    submitted = slt.form_submit_button("Submit")
    if submitted:
        slt.header(subject1)
        '''
        subjects = []
        for subject in [subject1, subject2, subject3]:
            if subject == True:
                subjects.append(subject)
        '''
