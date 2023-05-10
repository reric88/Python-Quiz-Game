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