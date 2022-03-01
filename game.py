from fetch_questions import QuestionBank
from question_logic import QuestionLogic

qb = QuestionBank()
ql = QuestionLogic(qb)

class QuizGame():

    def __init__(self, question_logic):
        self.ql = question_logic
        self.prompt_num = 0
        self.score = 0

    def play_game(self):
        ql.qb.get_questions()
        # self.valid_questions()

        # while ql.current_question < len(ql.qb.question_bank):
        #     ql.next_question()

        # print(f'Quiz Complete. You got {ql.score} out of {len(ql.qb.question_bank)} correct!')
        # self.play_again()

    def valid_questions(self):
        if len(ql.qb.question_bank) == 0:
            ql.qb.get_questions()
            return self.valid_questions()

    def play_again(self):
        response = input("Would you like to play again? 'Y' or 'N' ").upper()
        if response == "Y":
            ql.current_question = 0
            ql.score = 0
            self.play_game()
        else:
            print("Thank you for playing. Have a good day.")
