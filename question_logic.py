import requests
from fetch_questions import QuestionBank

class QuestionLogic():
    
    def __init__(self, qb):
        self.current_question = 0
        self.qb = qb
        self.qb.get_questions()

    def next_question(self):
        prompt = f"{self.current_question + 1}. True or False: {self.qb.question_bank[self.current_question]['question']}"
        print(prompt)
        player_answer = input("Please write 'True' or 'False': ")
        return self.check_answer(player_answer)

    def check_answer(self, answer):
        if answer == self.qb.question_bank[self.current_question]['correct_answer']:
            print("Correct")
        else:
            print("Incorrect")
        self.current_question += 1

