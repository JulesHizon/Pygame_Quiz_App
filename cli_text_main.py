from fetch_questions import QuestionBank
from question_logic import QuestionLogic

game_active = True
qb = QuestionBank()
ql = QuestionLogic(qb)

def play_game():
    cat = input("Please choose a category: 'animals', 'history', 'geography', 'sports'. ").lower()
    diff = input("Please choose a difficulty: 'easy', 'medium', 'hard'. ").lower()
    ql.qb.set_params(category=cat, difficulty=diff)
    ql.qb.get_questions()
    valid_questions()

    while ql.current_question < len(ql.qb.question_bank):
        ql.next_question()

    print(f'Quiz Complete. You got {ql.score} out of {len(ql.qb.question_bank)} correct!')
    play_again()

def valid_questions():
    if len(ql.qb.question_bank) == 0:
        print("Invalid Combination. Please try again.")
        cat = input("Please choose a category: 'animals', 'history', 'geography', 'sports'. ").lower()
        diff = input("Please choose a difficulty: 'easy', 'medium', 'hard'. ").lower()
        ql.qb.set_params(category=cat, difficulty=diff)
        ql.qb.get_questions()
        return valid_questions()

def play_again():
    response = input("Would you like to play again? 'Y' or 'N' ").upper()
    if response == "Y":
        ql.current_question = 0
        ql.score = 0
        play_game()
    else:
        print("Thank you for playing. Have a good day.")

if __name__ == "__main__":
    play_game()