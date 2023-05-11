# Step 2: Import data list and question model from data.py
from question_model import Question
from data import question_data

# Step 5: Import Quiz_Brain from quiz_brain.py
from quiz_brain import Quiz_Brain

# Step 3: Create a question-bank using the question_data that has been imported (loops)

# Step 3a: Place to store our questions in the question bank, i.e. an empty list
question_bank = []

# Step 3b: Loop through the question_data
for question in question_data:
    # Step 3c: Get a hold of question text and question answers from the question_data lists
    question_text = question['question']
    question_answer = question['correct_answer']

    # Step 3d: Create a new question using our imported class
    new_question = Question(question_text, question_answer)

    # 3e: Add Question to the question_bank list
    question_bank.append(new_question)

# 3f: Test to see if the loop works
# for i in question_bank:     # Working, so commented out
#     print(i)

# Step 6: Create new quiz_brain object using the Quiz_Brain class and pass in the question_bank
quiz = Quiz_Brain(question_bank)
# 6a Run the next_question method on the object we just created
# quiz.next_question()


# Step 7: Create a game loop
while quiz.still_has_question():
    # 7b Move the quiz.next_question from step 6a into the while loop
    quiz.next_question()

# Step 9: Notify the user when the quiz is complete and show the final score
print('You have completed the quiz!', f'Your final score was: {quiz.score}/{quiz.question_number}')