# Step 2: Import data list and question model from data.py
from question_model import Question
from data import question_data

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

