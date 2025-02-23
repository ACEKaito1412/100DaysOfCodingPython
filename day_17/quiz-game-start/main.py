from question_model import Question
from data import question_data
from quiz_brain import QuesBrain


question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))

brain = QuesBrain(questions=question_bank)

while brain.still_has_question():
    brain.next_question()

print("You completed the quiz")
print(f"Your final score was: {brain.score}/{brain.question_number}")