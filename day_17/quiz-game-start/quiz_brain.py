class QuesBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {q.text} (True/False): ")
        self.check_answer(ans, q.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("Thats not right.")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()
