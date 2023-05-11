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
        input(f'Q{self.question_number}: {current_question.text}; True/False')

    # Step 7? Create a method that advances the questions after the user has answered
    def still_has_question(self):
    # This method will return a boolean
        return self.question_number < len(self.question_list)

    # Step 8. Create a method that will check the answer that the user gives
    def check_answer(self, user_answer, correct_answer):
        # 8a create if/else statement that compares users and the correct answer. Be sure to account for varying cases and users answers
        if (user_answer.lower().strip() == correct_answer.lower()):
            # 8b Increase score by 1
            self.score += 1
            # 8c And let the user know they are correct
            print('Correct! 👌')
        # Create else statement for when the user gets the answer wrong
        else:
            print('Incorrect! 😒')
        # Display the correct answer
            print(f('The correct answer was: {correct_answer}'))