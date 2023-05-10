# Step 4: Bring up question and ask user to answer it
# All of Quiz functionality will be in this file

# 4a Create a class called quiz_brain
class Quiz_Brain:
    # 4b: Create constructor to initialize the necessary attributes (variables)
    # Those attributes will be question_number and user_score which will have default values in question_list which will be passed into the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # 4c: Create a method that retrieves the question from the question list created in main.py
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # 4d lists start at 0, so to display the correct question number for the next step, increase question number by 1
        self.question_number += 1
        # 4e Show the number_text and ask for the users answer
        input(f'Q.{self.question_number}: {current_question.text}; True/False')