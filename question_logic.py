class QuestionLogic():
    
    def __init__(self, qb):
        self.current_question = 0
        self.score = 0
        self.qb = qb

    def next_question(self):
        prompt = f"{self.current_question + 1}. True or False: {self.qb.question_bank[self.current_question]['question']}"
        print(prompt)
        player_answer = input("Please write 'True' or 'False': ")
        return self.is_valid_answer(player_answer)

    def check_answer(self, answer):
        if answer == self.qb.question_bank[self.current_question]['correct_answer']:
            self.score +=1
            print("Correct")
        else:
            print("Incorrect")
        self.current_question += 1

    def is_valid_answer(self, answer):
        if answer in ['True', 'False']:
            return self.check_answer(answer)
        else:
            print("Invalid Answer. Please type 'True' or 'False'.")
            return self.next_question()