import pygame
from game import QuizGame
from question_logic import QuestionLogic
from fetch_questions import QuestionBank
import time

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_COLOUR = (255, 249, 230)
CATEGORY_COLOUR = (209, 227, 255)
EASY_COLOUR = (105, 255, 125)
MEDIUM_COLOUR = (255, 247, 105)
HARD_COLOUR = (255, 125, 105)
PLAY_COLOUR = (201, 242, 202)
BTN_WIDTH = 150
BTN_HEIGHT = 75
TEXT_SIZE_1 = 25
TEXT_SIZE_2 = 35
FPS = 30

fps_clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quizzy")

#Button Class
class Button:
    
    def __init__(self, colour, x, y, width, height, text=''):
        self.color = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window, outline=None, text_size=TEXT_SIZE_1):
        if outline:
            pygame.draw.rect(window, outline, (self.x-1, self.y-1, self.width+2, self.height+2), 0, 8)
        
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0, 8)

        if self.text != '':
            font = pygame.font.SysFont('calibri', text_size)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        
    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

#Settings Buttons

btn_animals = Button(colour=CATEGORY_COLOUR, x=40, y=150, width=BTN_WIDTH, height=BTN_HEIGHT, text='Animals')
btn_history = Button(colour=CATEGORY_COLOUR, x=230, y=150, width=BTN_WIDTH, height=BTN_HEIGHT, text='History')
btn_sports = Button(colour=CATEGORY_COLOUR, x=420, y=150, width=BTN_WIDTH, height=BTN_HEIGHT, text='Sports')
btn_geography = Button(colour=CATEGORY_COLOUR, x=610, y=150, width=BTN_WIDTH, height=BTN_HEIGHT, text='Geography')

btn_easy = Button(colour=EASY_COLOUR, x=100, y=300, width=BTN_WIDTH, height=BTN_HEIGHT, text='Easy')
btn_medium = Button(colour=MEDIUM_COLOUR, x=325, y=300, width=BTN_WIDTH, height=BTN_HEIGHT, text='Medium')
btn_hard = Button(colour=HARD_COLOUR, x=550, y=300, width=BTN_WIDTH, height=BTN_HEIGHT, text='Hard')

btn_play = Button(colour=PLAY_COLOUR, x=325, y=450, width=BTN_WIDTH, height=BTN_HEIGHT, text='Play!')

selection_text = pygame.font.SysFont('calibri', 15)
selection_text = selection_text.render('selected', 1, (0,0,0))

settings_btns = [btn_animals, btn_history, btn_sports, btn_geography, btn_easy, btn_medium, btn_hard, btn_play]
category_btns = [btn_animals, btn_history, btn_sports, btn_geography]
difficulty_btns = [btn_easy, btn_medium, btn_hard]

setting_btn_active = {
    btn_animals : False,
    btn_history : False,
    btn_sports : False,
    btn_geography : False
}

diff_btn_active = {
    btn_easy : False,
    btn_medium : False,
    btn_hard : False
}

invalid_selection = False
invalid_text = pygame.font.SysFont('calibri', 20)
invalid_text = invalid_text.render('Invalid Combination. Please try again.', 1, (0,0,0))
instruction_text = pygame.font.SysFont('calibri', 20)
instruction_text = instruction_text.render('Please choose your category and difficulty.', 1, (0,0,0))

#Setting Draw Functions

def draw_settings_buttons():
    btn_animals.draw(screen, outline=(0,0,0))
    btn_history.draw(screen, outline=(0,0,0))
    btn_sports.draw(screen, outline=(0,0,0))
    btn_geography.draw(screen, outline=(0,0,0))
    btn_easy.draw(screen, outline=(0,0,0))
    btn_medium.draw(screen, outline=(0,0,0))
    btn_hard.draw(screen, outline=(0,0,0))
    btn_play.draw(screen, outline=(0,0,0))

def draw_setting_instructions():
    if invalid_selection:
        screen.blit(invalid_text, (250, 50))
    else:
        screen.blit(instruction_text, (225, 50))

def draw_category_selection():
    for btn in category_btns:
        if setting_btn_active[btn]:
            screen.blit(selection_text, (btn.x+50, btn.y-20))

def difficulty_button_selected():
    for btn in difficulty_btns:
        if diff_btn_active[btn]:
            screen.blit(selection_text, (btn.x+50, btn.y-20))

qb = QuestionBank()
ql = QuestionLogic(qb)
quiz = QuizGame(ql)

#Pre Game Options Loop
run_options = True
run_game = False
while run_options:

    fps_clock.tick(FPS)
    screen.fill(SCREEN_COLOUR)
    draw_setting_instructions()
    draw_settings_buttons()
    draw_category_selection()
    difficulty_button_selected()

    #Display Refresh
    pygame.display.update()

    #Event Handling
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        #Quit Event
        if event.type == pygame.QUIT:
            run_options = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in category_btns:
                if btn.is_over(pos):
                    quiz.ql.qb.set_category(btn.text.lower())
                    for key in setting_btn_active.keys():
                        setting_btn_active[key] = False
                    setting_btn_active[btn] = True

            for btn in difficulty_btns:
                if btn.is_over(pos):
                    quiz.ql.qb.set_difficulty(btn.text.lower())
                    for key in diff_btn_active.keys():
                        diff_btn_active[key] = False
                    diff_btn_active[btn] = True

            if btn_play.is_over(pos):
                quiz.ql.qb.get_questions()
                if len(quiz.ql.qb.question_bank) == 0:
                    invalid_selection = True
                else:
                    run_options = False
                    run_game = True

#Main Game Buttons

btn_true = Button(colour=EASY_COLOUR, x=165, y=375, width=BTN_WIDTH, height=BTN_HEIGHT, text='TRUE')
btn_false = Button(colour=HARD_COLOUR, x=485, y=375, width=BTN_WIDTH, height=BTN_HEIGHT, text='FALSE')
answer_btns = [btn_true, btn_false]

#Main Draw Functions
def draw_main_buttons():
    btn_true.draw(screen, outline=(0,0,0), text_size=TEXT_SIZE_2)
    btn_false.draw(screen, outline=(0,0,0), text_size=TEXT_SIZE_2)

def draw_prompt(prompt_number):
    prompt = quiz.ql.qb.question_bank[prompt_number]['question']
    prompt_font = pygame.font.SysFont('calibri', 20)
    prompt_text = prompt_font.render(f"{prompt_number+1}. {prompt}", 1, (0,0,0))
    text_rect = prompt_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(prompt_text, text_rect)

def draw_score(score):
    score_font = pygame.font.SysFont('calibri', 20)
    score_text = score_font.render(f"Score: {score}", 1, (0,0,0))
    text_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, 500))
    screen.blit(score_text, text_rect)

correct_trigger = False
incorrect_trigger = False

def draw_correct():
    global correct_trigger
    if correct_trigger:
        screen.fill((174, 249, 83))
        pygame.display.update()
        time.sleep(0.1)
        correct_trigger = False

def draw_incorrect():
    global incorrect_trigger
    if incorrect_trigger:
        screen.fill((249, 99, 83))
        pygame.display.update()
        time.sleep(0.1)
        incorrect_trigger = False

#Main Game Loop
while run_game:

    while quiz.prompt_num < len(quiz.ql.qb.question_bank):

        fps_clock.tick(FPS)
        screen.fill(SCREEN_COLOUR)
        draw_main_buttons()
        draw_prompt(quiz.prompt_num)
        draw_score(quiz.score)
        draw_correct()
        draw_incorrect()

        #Display Refresh
        pygame.display.update()

        #Event Handling
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #Quit Event
            if event.type == pygame.QUIT:
                run_game = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if btn_true.is_over(pos):
                    if quiz.ql.qb.question_bank[quiz.prompt_num]['correct_answer'] == 'True':
                        quiz.score += 1
                        correct_trigger = True
                    else:
                        incorrect_trigger = True
                    quiz.prompt_num += 1

                if btn_false.is_over(pos):
                    if quiz.ql.qb.question_bank[quiz.prompt_num]['correct_answer'] == 'False':
                        quiz.score += 1
                        correct_trigger = True
                    else:
                        incorrect_trigger = True
                    quiz.prompt_num += 1    

    run_game = False
    end_game = True

def draw_final_score():
    final_score_font = pygame.font.SysFont('calibri', 40)
    final_score_text = final_score_font.render(f"Thanks for playing. Your final score is {quiz.score}/10!", 1, (0,0,0))
    text_rect = final_score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(final_score_text, text_rect)

while end_game:

    fps_clock.tick(FPS)
    screen.fill(SCREEN_COLOUR)
    draw_final_score()

    #Display Refresh
    pygame.display.update()

    #Event Handling
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        #Quit Event
        if event.type == pygame.QUIT:
            run_game = False
            pygame.quit()